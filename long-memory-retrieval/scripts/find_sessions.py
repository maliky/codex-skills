#!/usr/bin/env python3
"""Find local Codex sessions whose history rows match query terms."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SESSION_ID_RE = re.compile(
    r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I
)


def default_codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search Codex history and attach aliases and workspaces."
    )
    parser.add_argument("--codex-home", default=str(default_codex_home()))
    parser.add_argument("--query", required=True, help="Case-insensitive terms to search for.")
    parser.add_argument(
        "--match",
        choices=("all", "any"),
        default="all",
        help="Require all query terms or any query term; default: all.",
    )
    parser.add_argument(
        "--term-mode",
        choices=("substring", "word"),
        default="substring",
        help=(
            "Match substrings or complete alphanumeric terms; word mode treats "
            "underscores and punctuation as boundaries."
        ),
    )
    parser.add_argument(
        "--since",
        help="Include rows at or after this UTC date/time or Unix timestamp.",
    )
    parser.add_argument(
        "--until",
        help="Include rows before this UTC date/time or Unix timestamp.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    return parser.parse_args()


def load_jsonl(path: Path) -> list[tuple[int, dict[str, Any], str]]:
    rows: list[tuple[int, dict[str, Any], str]] = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.rstrip("\n")
            if not text:
                continue
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                data = {"_raw": text}
            if isinstance(data, dict):
                rows.append((line_no, data, text))
    return rows


def aliases(index_path: Path) -> dict[str, list[str]]:
    found: dict[str, set[str]] = defaultdict(set)
    for _, row, _ in load_jsonl(index_path):
        session_id = row.get("id")
        name = row.get("thread_name")
        if session_id and name:
            found[str(session_id)].add(str(name))
    return {session_id: sorted(names) for session_id, names in found.items()}


def parse_timestamp(value: str | None) -> float | None:
    if value is None:
        return None
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


def session_workspaces(root: Path, wanted: set[str]) -> dict[str, list[str]]:
    found: dict[str, set[str]] = defaultdict(set)
    sessions_root = root / "sessions"
    if not sessions_root.exists() or not wanted:
        return {}
    for path in sessions_root.rglob("*.jsonl"):
        try:
            with path.open("r", encoding="utf-8") as handle:
                first_line = handle.readline()
            event = json.loads(first_line)
        except (OSError, json.JSONDecodeError):
            continue
        if event.get("type") != "session_meta":
            continue
        payload = event.get("payload")
        if not isinstance(payload, dict):
            continue
        session_id = payload.get("session_id") or payload.get("id")
        cwd = payload.get("cwd")
        if (
            isinstance(session_id, str)
            and session_id in wanted
            and isinstance(cwd, str)
            and cwd
        ):
            found[session_id].add(cwd)
    return {session_id: sorted(paths) for session_id, paths in found.items()}


def row_session_id(row: dict[str, Any], raw: str) -> str | None:
    for key in ("session_id", "id", "thread_id"):
        value = row.get(key)
        if isinstance(value, str) and SESSION_ID_RE.fullmatch(value):
            return value
    match = SESSION_ID_RE.search(raw)
    return match.group(0) if match else None


def compile_terms(terms: list[str], mode: str) -> list[re.Pattern[str]]:
    if mode == "word":
        return [
            re.compile(rf"(?<![^\W_]){re.escape(term)}(?![^\W_])", re.IGNORECASE)
            for term in terms
        ]
    return [re.compile(re.escape(term), re.IGNORECASE) for term in terms]


def snippet(raw: str, patterns: list[re.Pattern[str]], width: int = 180) -> str:
    positions = [match.start() for pattern in patterns if (match := pattern.search(raw))]
    start = max(min(positions) - 60, 0) if positions else 0
    text = raw[start : start + width].replace("\t", " ")
    return text + ("..." if start + width < len(raw) else "")


def main() -> int:
    args = parse_args()
    root = Path(args.codex_home).expanduser()
    history_path = root / "history.jsonl"
    index_path = root / "session_index.jsonl"
    terms = [term for term in args.query.split() if term.strip()]
    if not terms:
        raise SystemExit("--query must contain at least one non-whitespace term")
    patterns = compile_terms(terms, args.term_mode)
    try:
        since = parse_timestamp(args.since)
        until = parse_timestamp(args.until)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    if since is not None and until is not None and since >= until:
        raise SystemExit("--since must be earlier than --until")

    alias_map = aliases(index_path)
    results: dict[str, dict[str, Any]] = {}
    for line_no, row, raw in load_jsonl(history_path):
        timestamp = row.get("ts")
        if since is not None and (
            not isinstance(timestamp, (int, float)) or timestamp < since
        ):
            continue
        if until is not None and (
            not isinstance(timestamp, (int, float)) or timestamp >= until
        ):
            continue
        searchable = row.get("text") if isinstance(row.get("text"), str) else raw
        matches = [bool(pattern.search(searchable)) for pattern in patterns]
        if (args.match == "all" and not all(matches)) or (
            args.match == "any" and not any(matches)
        ):
            continue
        session_id = row_session_id(row, raw) or "<unknown>"
        item = results.setdefault(
            session_id,
            {
                "session_id": session_id,
                "aliases": alias_map.get(session_id, []),
                "workspaces": [],
                "matches": [],
            },
        )
        item["matches"].append(
            {
                "line": line_no,
                "timestamp": timestamp,
                "snippet": snippet(searchable, patterns),
            }
        )

    workspace_map = session_workspaces(root, set(results))
    for session_id, item in results.items():
        item["workspaces"] = workspace_map.get(session_id, [])

    ordered = sorted(results.values(), key=lambda item: item["matches"][0]["line"])
    if args.json:
        print(json.dumps(ordered, ensure_ascii=False, indent=2))
        return 0

    if not ordered:
        print("No matching sessions found.")
        return 0
    for item in ordered:
        print(item["session_id"])
        print("  aliases: " + (", ".join(item["aliases"]) if item["aliases"] else "<none>"))
        print(
            "  workspaces: "
            + (", ".join(item["workspaces"]) if item["workspaces"] else "<none>")
        )
        print(f"  matches: {len(item['matches'])}")
        first = item["matches"][0]
        print(f"  first: history.jsonl:{first['line']} {first['snippet']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
