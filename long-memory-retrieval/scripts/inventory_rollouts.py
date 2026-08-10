#!/usr/bin/env python3
"""Inventory recently modified Codex rollout files without loading tool payloads."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TIMESTAMP_RE = re.compile(r'^\{"timestamp"\s*:\s*"([^"]+)"')
MAX_MESSAGE_CHARS = 1000
SKIP_USER_PREFIXES = (
    "<environment_context>",
    "# AGENTS.md instructions",
    "<recommended_plugins>",
)


def default_codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()


def parse_timestamp(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        pass
    normalized = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"Invalid timestamp: {value}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.timestamp()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inventory recently modified root and optional subagent rollouts."
    )
    parser.add_argument("--codex-home", default=str(default_codex_home()))
    parser.add_argument(
        "--modified-since",
        required=True,
        help="Include rollout files modified at or after this UTC time or Unix timestamp.",
    )
    parser.add_argument(
        "--include-subagents",
        action="store_true",
        help="Include subagent rollouts; root sessions are the default.",
    )
    parser.add_argument(
        "--last-user-messages",
        type=int,
        default=3,
        help="Retain this many recent real user messages per rollout; default: 3.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    return parser.parse_args()


def aliases(index_path: Path) -> dict[str, list[str]]:
    found: dict[str, set[str]] = defaultdict(set)
    if not index_path.exists():
        return {}
    with index_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(row, dict):
                continue
            session_id, name = row.get("id"), row.get("thread_name")
            if isinstance(session_id, str) and isinstance(name, str) and name:
                found[session_id].add(name)
    return {session_id: sorted(names) for session_id, names in found.items()}


def is_subagent(meta: dict[str, Any]) -> bool:
    source = meta.get("source")
    return bool(
        meta.get("thread_source") == "subagent"
        or meta.get("parent_thread_id")
        or (isinstance(source, dict) and "subagent" in source)
    )


def user_text(payload: dict[str, Any]) -> str:
    if payload.get("type") != "message" or payload.get("role") != "user":
        return ""
    parts = [
        item.get("text", "")
        for item in payload.get("content", [])
        if isinstance(item, dict) and item.get("type") == "input_text"
    ]
    text = "\n".join(part for part in parts if isinstance(part, str)).strip()
    if not text or text.startswith(SKIP_USER_PREFIXES):
        return ""
    if len(text) > MAX_MESSAGE_CHARS:
        return text[: MAX_MESSAGE_CHARS - 3] + "..."
    return text


def inspect_rollout(
    path: Path,
    codex_home: Path,
    alias_map: dict[str, list[str]],
    message_limit: int,
    include_subagents: bool,
) -> dict[str, Any] | None:
    meta: dict[str, Any] = {}
    recent: deque[str] = deque(maxlen=message_limit)
    user_message_count = 0
    last_event_at: str | None = None

    try:
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                timestamp_match = TIMESTAMP_RE.match(line)
                if timestamp_match:
                    last_event_at = timestamp_match.group(1)
                if not meta and '"session_meta"' in line:
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    payload = event.get("payload")
                    if isinstance(payload, dict):
                        meta = payload
                        if is_subagent(meta) and not include_subagents:
                            return None
                    continue
                if (
                    '"response_item"' not in line
                    or '"message"' not in line
                    or '"user"' not in line
                ):
                    continue
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") != "response_item":
                    continue
                payload = event.get("payload")
                if not isinstance(payload, dict):
                    continue
                text = user_text(payload)
                if text:
                    user_message_count += 1
                    recent.append(text.replace("\n", " "))
    except (OSError, UnicodeError):
        return None

    if not meta:
        return None
    rollout_id = str(meta.get("id") or path.stem)
    main_session_id = str(meta.get("session_id") or rollout_id)
    modified = path.stat().st_mtime
    return {
        "rollout_id": rollout_id,
        "main_session_id": main_session_id,
        "parent_thread_id": meta.get("parent_thread_id"),
        "is_subagent": is_subagent(meta),
        "thread_source": meta.get("thread_source"),
        "source": meta.get("source"),
        "aliases": alias_map.get(main_session_id, []),
        "workspace": meta.get("cwd"),
        "path": str(path.relative_to(codex_home)),
        "size_bytes": path.stat().st_size,
        "modified_at": datetime.fromtimestamp(modified, timezone.utc).isoformat(),
        "last_event_at": last_event_at,
        "user_message_count": user_message_count,
        "last_user_messages": list(recent),
    }


def main() -> int:
    args = parse_args()
    if args.last_user_messages < 0:
        raise SystemExit("--last-user-messages must be non-negative")
    try:
        cutoff = parse_timestamp(args.modified_since)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    root = Path(args.codex_home).expanduser()
    sessions_root = root / "sessions"
    alias_map = aliases(root / "session_index.jsonl")
    results: list[dict[str, Any]] = []
    if sessions_root.exists():
        for path in sessions_root.rglob("*.jsonl"):
            try:
                if path.stat().st_mtime < cutoff:
                    continue
            except OSError:
                continue
            item = inspect_rollout(
                path, root, alias_map, args.last_user_messages, args.include_subagents
            )
            if item:
                results.append(item)
    results.sort(key=lambda item: (item["modified_at"], item["path"]))

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0
    if not results:
        print("No recently modified rollouts found.")
        return 0
    for item in results:
        role = "subagent" if item["is_subagent"] else "root"
        print(f"{item['rollout_id']} ({role})")
        print(f"  main session: {item['main_session_id']}")
        if item["parent_thread_id"]:
            print(f"  parent: {item['parent_thread_id']}")
        print("  aliases: " + (", ".join(item["aliases"]) if item["aliases"] else "<none>"))
        print(f"  workspace: {item['workspace'] or '<none>'}")
        print(f"  modified: {item['modified_at']}")
        print(f"  user messages: {item['user_message_count']}")
        for message in item["last_user_messages"]:
            print(f"    - {message[:300]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
