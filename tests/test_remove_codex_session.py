from __future__ import annotations

import importlib.util
import io
import json
import sqlite3
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock


SCRIPT = (
    Path(__file__).parents[1]
    / "codex-session-cleanup"
    / "scripts"
    / "remove_codex_session.py"
)
SPEC = importlib.util.spec_from_file_location("remove_codex_session", SCRIPT)
assert SPEC and SPEC.loader
cleanup = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cleanup
SPEC.loader.exec_module(cleanup)

SESSION_ID = "019e87f4-9cf1-7e50-afd4-8d73a5788538"
OTHER_ID = "019e87f4-9cf1-7e50-afd4-8d73a5788539"


class CleanupFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.home = Path(self.temp.name)
        self.sessions = self.home / "sessions" / "2026" / "07" / "11"
        self.sessions.mkdir(parents=True)
        self.rollout = self.sessions / f"rollout-{SESSION_ID}.jsonl"
        self.rollout.write_text('{"session": "target"}\n', encoding="utf-8")
        self.history_text = (
            json.dumps({"session_id": SESSION_ID, "text": "remove"})
            + "\n\n"
            + '{  "session_id": "' + OTHER_ID + '", "text": "preserve formatting"  }\n'
        )
        (self.home / "history.jsonl").write_text(
            self.history_text, encoding="utf-8"
        )
        (self.home / "session_index.jsonl").write_text(
            json.dumps({"id": SESSION_ID, "thread_name": "target"})
            + "\n"
            + json.dumps({"id": OTHER_ID, "thread_name": "other"})
            + "\n",
            encoding="utf-8",
        )
        with sqlite3.connect(self.home / "state_5.sqlite") as conn:
            conn.executescript(
                """
                PRAGMA foreign_keys = ON;
                CREATE TABLE threads (id TEXT PRIMARY KEY, rollout_path TEXT NOT NULL);
                CREATE TABLE thread_dynamic_tools (
                    thread_id TEXT NOT NULL,
                    position INTEGER NOT NULL,
                    PRIMARY KEY(thread_id, position),
                    FOREIGN KEY(thread_id) REFERENCES threads(id) ON DELETE CASCADE
                );
                """
            )
            conn.execute(
                "INSERT INTO threads(id, rollout_path) VALUES (?, ?)",
                (SESSION_ID, str(self.rollout)),
            )
            conn.execute(
                "INSERT INTO thread_dynamic_tools(thread_id, position) VALUES (?, 0)",
                (SESSION_ID,),
            )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_main(self, *args: str) -> tuple[int, str, str]:
        argv = [str(SCRIPT), "--codex-home", str(self.home), *args]
        stdout = io.StringIO()
        stderr = io.StringIO()
        with mock.patch.object(sys, "argv", argv), redirect_stdout(stdout), redirect_stderr(stderr):
            result = cleanup.main()
        return result, stdout.getvalue(), stderr.getvalue()

    def test_dry_run_is_read_only(self) -> None:
        result, output, error = self.run_main("--session-id", SESSION_ID, "--dry-run")
        self.assertEqual((result, error), (0, ""))
        self.assertIn("backup_dir: <none>", output)
        self.assertEqual((self.home / "history.jsonl").read_text(), self.history_text)
        self.assertTrue(self.rollout.exists())

    def test_success_preserves_unmatched_jsonl_bytes_and_creates_backup(self) -> None:
        result, output, error = self.run_main("--name", "target")
        self.assertEqual((result, error), (0, ""))
        self.assertFalse(self.rollout.exists())
        self.assertEqual(
            (self.home / "history.jsonl").read_text(),
            "\n" + '{  "session_id": "' + OTHER_ID + '", "text": "preserve formatting"  }\n',
        )
        with sqlite3.connect(self.home / "state_5.sqlite") as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM threads").fetchone()[0], 0)
            self.assertEqual(
                conn.execute("SELECT COUNT(*) FROM thread_dynamic_tools").fetchone()[0], 0
            )
        backup_line = next(line for line in output.splitlines() if line.startswith("backup_dir: "))
        self.assertTrue(Path(backup_line.removeprefix("backup_dir: ")).is_dir())

    def test_failure_restores_all_stores(self) -> None:
        with mock.patch.object(
            cleanup, "cleanup_db", side_effect=sqlite3.OperationalError("injected")
        ):
            result, _, error = self.run_main("--session-id", SESSION_ID)
        self.assertEqual(result, 1)
        self.assertIn("injected", error)
        self.assertEqual((self.home / "history.jsonl").read_text(), self.history_text)
        self.assertTrue(self.rollout.exists())
        with sqlite3.connect(self.home / "state_5.sqlite") as conn:
            self.assertEqual(conn.execute("SELECT COUNT(*) FROM threads").fetchone()[0], 1)

    def test_rollout_path_outside_sessions_is_rejected(self) -> None:
        outside = self.home / f"outside-{SESSION_ID}.jsonl"
        outside.write_text("keep\n", encoding="utf-8")
        with sqlite3.connect(self.home / "state_5.sqlite") as conn:
            conn.execute(
                "UPDATE threads SET rollout_path = ? WHERE id = ?",
                (str(outside), SESSION_ID),
            )
        result, _, error = self.run_main("--session-id", SESSION_ID, "--dry-run")
        self.assertEqual(result, 1)
        self.assertIn("outside sessions directory", error)
        self.assertTrue(outside.exists())

    def test_unknown_session_is_rejected(self) -> None:
        result, _, error = self.run_main("--session-id", "unknown", "--dry-run")
        self.assertEqual(result, 1)
        self.assertIn("No records found", error)

    def test_ambiguous_alias_is_rejected(self) -> None:
        with (self.home / "session_index.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"id": OTHER_ID, "thread_name": "target"}) + "\n")
        result, _, error = self.run_main("--name", "target", "--dry-run")
        self.assertEqual(result, 1)
        self.assertIn("Ambiguous alias", error)


if __name__ == "__main__":
    unittest.main()
