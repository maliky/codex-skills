#!/usr/bin/env python3
"""Find local Codex sessions whose history rows match a query."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


SESSION_ID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I)


def default_codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search Codex history and attach session aliases.")
    parser.add_argument("--codex-home", default=str(default_codex_home()))
    parser.add_argument("--query", required=True, help="Case-insensitive terms to search for.")
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


def row_session_id(row: dict[str, Any], raw: str) -> str | None:
    for key in ("session_id", "id", "thread_id"):
        value = row.get(key)
        if isinstance(value, str) and SESSION_ID_RE.fullmatch(value):
            return value
    match = SESSION_ID_RE.search(raw)
    return match.group(0) if match else None


def snippet(raw: str, terms: list[str], width: int = 180) -> str:
    lower = raw.lower()
    positions = [lower.find(term) for term in terms if lower.find(term) >= 0]
    start = max(min(positions) - 60, 0) if positions else 0
    text = raw[start : start + width].replace("\t", " ")
    return text + ("..." if start + width < len(raw) else "")


def main() -> int:
    args = parse_args()
    root = Path(args.codex_home).expanduser()
    history_path = root / "history.jsonl"
    index_path = root / "session_index.jsonl"
    terms = [term.lower() for term in args.query.split() if term.strip()]
    alias_map = aliases(index_path)
    results: dict[str, dict[str, Any]] = {}

    for line_no, row, raw in load_jsonl(history_path):
        lower = raw.lower()
        if not all(term in lower for term in terms):
            continue
        session_id = row_session_id(row, raw) or "<unknown>"
        item = results.setdefault(
            session_id,
            {"session_id": session_id, "aliases": alias_map.get(session_id, []), "matches": []},
        )
        item["matches"].append({"line": line_no, "snippet": snippet(raw, terms)})

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
        print(f"  matches: {len(item['matches'])}")
        print(f"  first: history.jsonl:{item['matches'][0]['line']} {item['matches'][0]['snippet']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
