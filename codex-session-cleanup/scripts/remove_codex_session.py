#!/usr/bin/env python3
"""Remove a local Codex session by exact id or exact thread-name alias."""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from dataclasses import dataclass
from pathlib import Path
from shutil import copy2
from typing import Any, Callable


class CleanupError(RuntimeError):
    """Raised when cleanup cannot complete safely."""


@dataclass(frozen=True)
class Paths:
    codex_home: Path
    history: Path
    session_index: Path
    sessions_dir: Path
    state_db: Path


@dataclass(frozen=True)
class Target:
    session_id: str
    aliases: tuple[str, ...]
    rollout_path: Path | None


@dataclass(frozen=True)
class Snapshot:
    directory: Path
    history: Path
    session_index: Path
    state_db: Path | None
    rollout: Path | None


def default_codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Remove one local Codex session by exact id or exact alias."
    )
    parser.add_argument(
        "--codex-home",
        default=str(default_codex_home()),
        help="Codex home directory. Defaults to $CODEX_HOME or ~/.codex.",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--session-id", help="Exact Codex session id to remove.")
    group.add_argument("--name", help="Exact thread-name alias to remove.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Resolve and report cleanup targets without deleting anything.",
    )
    return parser.parse_args()


def build_paths(codex_home: str) -> Paths:
    root = Path(codex_home).expanduser().resolve()
    return Paths(
        codex_home=root,
        history=root / "history.jsonl",
        session_index=root / "session_index.jsonl",
        sessions_dir=root / "sessions",
        state_db=root / "state_5.sqlite",
    )


def load_jsonl(path: Path, required: bool = True) -> list[dict[str, Any]]:
    if not path.exists():
        if required:
            raise CleanupError(f"Missing required file: {path}")
        return []

    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                row = json.loads(text)
            except json.JSONDecodeError as exc:
                raise CleanupError(f"Invalid JSON in {path}:{line_no}: {exc}") from exc
            if isinstance(row, dict):
                rows.append(row)
    return rows


def resolve_session_id(rows: list[dict[str, Any]], args: argparse.Namespace) -> str:
    if args.session_id:
        return args.session_id

    matches = sorted(
        {
            str(row["id"])
            for row in rows
            if str(row.get("thread_name", "")) == args.name and row.get("id")
        }
    )
    if not matches:
        raise CleanupError(f"No session matched exact thread-name alias: {args.name!r}")
    if len(matches) > 1:
        raise CleanupError(
            f"Ambiguous alias {args.name!r}; matched ids: {', '.join(matches)}"
        )
    return matches[0]


def aliases_for_session(rows: list[dict[str, Any]], session_id: str) -> tuple[str, ...]:
    return tuple(
        sorted(
            {
                str(row["thread_name"])
                for row in rows
                if str(row.get("id", "")) == session_id and row.get("thread_name")
            }
        )
    )


def sqlite_tables(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with sqlite3.connect(path) as conn:
        return {
            str(row[0])
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table'"
            ).fetchall()
        }


def rollout_from_db(paths: Paths, session_id: str, tables: set[str]) -> Path | None:
    if "threads" not in tables:
        return None
    with sqlite3.connect(paths.state_db) as conn:
        row = conn.execute(
            "SELECT rollout_path FROM threads WHERE id = ?",
            (session_id,),
        ).fetchone()
    if row and row[0]:
        rollout = Path(row[0]).expanduser().resolve()
        sessions_dir = paths.sessions_dir.resolve()
        try:
            rollout.relative_to(sessions_dir)
        except ValueError as exc:
            raise CleanupError(
                f"Refusing rollout path outside sessions directory: {rollout}"
            ) from exc
        if session_id not in rollout.name:
            raise CleanupError(
                f"Refusing rollout path that does not contain the session id: {rollout}"
            )
        return rollout
    return None


def find_rollout(paths: Paths, session_id: str, tables: set[str]) -> Path | None:
    from_db = rollout_from_db(paths, session_id, tables)
    if from_db is not None:
        return from_db
    if not paths.sessions_dir.exists():
        return None
    matches = sorted(paths.sessions_dir.rglob(f"*{session_id}*.jsonl"))
    if len(matches) > 1:
        raise CleanupError(
            f"Multiple rollout files matched {session_id}: "
            + ", ".join(str(path) for path in matches)
        )
    return matches[0] if matches else None


def resolve_target(paths: Paths, args: argparse.Namespace, tables: set[str]) -> Target:
    index_rows = load_jsonl(paths.session_index)
    session_id = resolve_session_id(index_rows, args)
    return Target(
        session_id=session_id,
        aliases=aliases_for_session(index_rows, session_id),
        rollout_path=find_rollout(paths, session_id, tables),
    )


def stage_jsonl_excluding(
    path: Path, predicate: Callable[[dict[str, Any]], bool]
) -> tuple[Path, int]:
    removed = 0
    with path.open("r", encoding="utf-8") as src, tempfile.NamedTemporaryFile(
        "w", delete=False, encoding="utf-8", dir=path.parent
    ) as tmp:
        tmp_path = Path(tmp.name)
        for line in src:
            text = line.strip()
            if not text:
                tmp.write(line)
                continue
            row = json.loads(text)
            if isinstance(row, dict) and predicate(row):
                removed += 1
                continue
            tmp.write(line)
    return tmp_path, removed


def backup_sqlite(source: Path, destination: Path) -> None:
    with sqlite3.connect(source) as src, sqlite3.connect(destination) as dst:
        src.backup(dst)


def create_snapshot(paths: Paths, target: Target) -> Snapshot:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    directory = (
        paths.codex_home / "backups" / "session-cleanup" / f"{stamp}-{target.session_id}"
    )
    directory.mkdir(parents=True, mode=0o700, exist_ok=False)
    os.chmod(directory, 0o700)

    history = directory / "history.jsonl"
    session_index = directory / "session_index.jsonl"
    copy2(paths.history, history)
    copy2(paths.session_index, session_index)

    state_db: Path | None = None
    if paths.state_db.exists():
        state_db = directory / "state_5.sqlite"
        backup_sqlite(paths.state_db, state_db)

    rollout: Path | None = None
    if target.rollout_path is not None and target.rollout_path.exists():
        rollout = directory / target.rollout_path.name
        copy2(target.rollout_path, rollout)

    for file_path in directory.iterdir():
        if file_path.is_file():
            os.chmod(file_path, 0o600)
    return Snapshot(directory, history, session_index, state_db, rollout)


def restore_snapshot(paths: Paths, target: Target, snapshot: Snapshot) -> None:
    copy2(snapshot.history, paths.history)
    copy2(snapshot.session_index, paths.session_index)
    if snapshot.state_db is not None:
        backup_sqlite(snapshot.state_db, paths.state_db)
    if snapshot.rollout is not None and target.rollout_path is not None:
        target.rollout_path.parent.mkdir(parents=True, exist_ok=True)
        copy2(snapshot.rollout, target.rollout_path)


def count_jsonl(path: Path, predicate: Callable[[dict[str, Any]], bool]) -> int:
    return sum(1 for row in load_jsonl(path, required=False) if predicate(row))


def cleanup_db(paths: Paths, session_id: str, tables: set[str]) -> dict[str, int]:
    counts = {
        "thread_spawn_edges": 0,
        "agent_job_items": 0,
        "threads": 0,
        "thread_dynamic_tools": 0,
        "stage1_outputs": 0,
    }
    if not paths.state_db.exists():
        return counts

    with sqlite3.connect(paths.state_db) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        if "thread_dynamic_tools" in tables:
            counts["thread_dynamic_tools"] = conn.execute(
                "SELECT COUNT(*) FROM thread_dynamic_tools WHERE thread_id = ?",
                (session_id,),
            ).fetchone()[0]
        if "stage1_outputs" in tables:
            counts["stage1_outputs"] = conn.execute(
                "SELECT COUNT(*) FROM stage1_outputs WHERE thread_id = ?",
                (session_id,),
            ).fetchone()[0]
        conn.execute("BEGIN IMMEDIATE")
        try:
            if "thread_spawn_edges" in tables:
                counts["thread_spawn_edges"] = conn.execute(
                    "DELETE FROM thread_spawn_edges "
                    "WHERE parent_thread_id = ? OR child_thread_id = ?",
                    (session_id, session_id),
                ).rowcount
            if "agent_job_items" in tables:
                counts["agent_job_items"] = conn.execute(
                    "DELETE FROM agent_job_items WHERE assigned_thread_id = ?",
                    (session_id,),
                ).rowcount
            if "threads" in tables:
                counts["threads"] = conn.execute(
                    "DELETE FROM threads WHERE id = ?",
                    (session_id,),
                ).rowcount
        except Exception:
            conn.rollback()
            raise
        conn.commit()
    return counts


def matching_db_counts(paths: Paths, session_id: str, tables: set[str]) -> dict[str, int]:
    counts = {
        "thread_spawn_edges": 0,
        "agent_job_items": 0,
        "threads": 0,
        "thread_dynamic_tools": 0,
        "stage1_outputs": 0,
    }
    if not paths.state_db.exists():
        return counts
    with sqlite3.connect(paths.state_db) as conn:
        if "threads" in tables:
            counts["threads"] = conn.execute(
                "SELECT COUNT(*) FROM threads WHERE id = ?",
                (session_id,),
            ).fetchone()[0]
        if "thread_spawn_edges" in tables:
            counts["thread_spawn_edges"] = conn.execute(
                "SELECT COUNT(*) FROM thread_spawn_edges "
                "WHERE parent_thread_id = ? OR child_thread_id = ?",
                (session_id, session_id),
            ).fetchone()[0]
        if "agent_job_items" in tables:
            counts["agent_job_items"] = conn.execute(
                "SELECT COUNT(*) FROM agent_job_items WHERE assigned_thread_id = ?",
                (session_id,),
            ).fetchone()[0]
        if "thread_dynamic_tools" in tables:
            counts["thread_dynamic_tools"] = conn.execute(
                "SELECT COUNT(*) FROM thread_dynamic_tools WHERE thread_id = ?",
                (session_id,),
            ).fetchone()[0]
        if "stage1_outputs" in tables:
            counts["stage1_outputs"] = conn.execute(
                "SELECT COUNT(*) FROM stage1_outputs WHERE thread_id = ?",
                (session_id,),
            ).fetchone()[0]
    return counts


def verify(paths: Paths, target: Target, tables: set[str]) -> None:
    if count_jsonl(paths.history, lambda row: str(row.get("session_id", "")) == target.session_id):
        raise CleanupError("Verification failed: history.jsonl still contains target")
    if count_jsonl(paths.session_index, lambda row: str(row.get("id", "")) == target.session_id):
        raise CleanupError("Verification failed: session_index.jsonl still contains target")
    if target.rollout_path is not None and target.rollout_path.exists():
        raise CleanupError(f"Verification failed: rollout file remains: {target.rollout_path}")
    remaining = matching_db_counts(paths, target.session_id, tables)
    live_remaining = {name: count for name, count in remaining.items() if count}
    if live_remaining:
        raise CleanupError(f"Verification failed: database rows remain: {live_remaining}")


def print_report(
    target: Target,
    history: int,
    index: int,
    rollout: int,
    db: dict[str, int],
    backup_dir: Path | None = None,
) -> None:
    print(f"session_id: {target.session_id}")
    print("aliases: " + (", ".join(target.aliases) if target.aliases else "<none>"))
    print(f"rollout_file: {target.rollout_path if target.rollout_path else '<none>'}")
    print(f"rollout_files_removed: {rollout}")
    print(f"history_rows: {history}")
    print(f"session_index_rows: {index}")
    print(f"backup_dir: {backup_dir if backup_dir else '<none>'}")
    print("state_rows: " + ", ".join(f"{key}={db[key]}" for key in sorted(db)))


def main() -> int:
    args = parse_args()
    paths = build_paths(args.codex_home)

    snapshot: Snapshot | None = None
    target: Target | None = None
    staged: list[Path] = []
    try:
        tables = sqlite_tables(paths.state_db)
        target = resolve_target(paths, args, tables)
        history_count = count_jsonl(
            paths.history,
            lambda row: str(row.get("session_id", "")) == target.session_id,
        )
        index_count = count_jsonl(
            paths.session_index,
            lambda row: str(row.get("id", "")) == target.session_id,
        )
        rollout_count = int(
            target.rollout_path is not None and target.rollout_path.exists()
        )
        db_counts = matching_db_counts(paths, target.session_id, tables)
        if not (history_count or index_count or rollout_count or any(db_counts.values())):
            raise CleanupError(f"No records found for session id: {target.session_id}")
        if args.dry_run:
            print_report(
                target, history_count, index_count, rollout_count, db_counts
            )
            return 0

        snapshot = create_snapshot(paths, target)
        history_tmp, history = stage_jsonl_excluding(
            paths.history, lambda row: str(row.get("session_id", "")) == target.session_id
        )
        staged.append(history_tmp)
        index_tmp, index = stage_jsonl_excluding(
            paths.session_index, lambda row: str(row.get("id", "")) == target.session_id
        )
        staged.append(index_tmp)
        os.replace(history_tmp, paths.history)
        staged.remove(history_tmp)
        os.replace(index_tmp, paths.session_index)
        staged.remove(index_tmp)
        rollout = 0
        if target.rollout_path is not None and target.rollout_path.exists():
            target.rollout_path.unlink()
            rollout = 1
        db = cleanup_db(paths, target.session_id, tables)
        verify(paths, target, tables)
        print_report(target, history, index, rollout, db, snapshot.directory)
        return 0
    except (CleanupError, OSError, sqlite3.Error) as exc:
        for staged_path in staged:
            staged_path.unlink(missing_ok=True)
        if snapshot is not None and target is not None:
            try:
                restore_snapshot(paths, target, snapshot)
            except (OSError, sqlite3.Error) as restore_exc:
                print(
                    f"Error restoring backup {snapshot.directory}: {restore_exc}",
                    file=sys.stderr,
                )
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
