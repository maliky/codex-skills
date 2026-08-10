from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


SCRIPT = (
    Path(__file__).parents[1]
    / "long-memory-retrieval"
    / "scripts"
    / "find_sessions.py"
)
SPEC = importlib.util.spec_from_file_location("find_sessions", SCRIPT)
assert SPEC and SPEC.loader
finder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = finder
SPEC.loader.exec_module(finder)

SESSION_A = "019e87f4-9cf1-7e50-afd4-8d73a5788538"
SESSION_B = "019e87f4-9cf1-7e50-afd4-8d73a5788539"


class FindSessionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.home = Path(self.temp.name)
        rows = (
            {"session_id": SESSION_A, "ts": 100, "text": "alpha beta"},
            {"session_id": SESSION_B, "ts": 200, "text": "alpha gamma images"},
            {"session_id": SESSION_A, "ts": 300, "text": "gamma delta"},
            {"session_id": SESSION_A, "ts": 400, "text": "PI_ contract"},
        )
        (self.home / "history.jsonl").write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8"
        )
        (self.home / "session_index.jsonl").write_text(
            json.dumps({"id": SESSION_A, "thread_name": "alpha-thread"}) + "\n",
            encoding="utf-8",
        )
        rollout = (
            self.home / "sessions" / "2026" / "01" / f"rollout-{SESSION_B}.jsonl"
        )
        rollout.parent.mkdir(parents=True)
        rollout.write_text(
            json.dumps(
                {
                    "type": "session_meta",
                    "payload": {"session_id": SESSION_B, "cwd": "/work/gamma"},
                }
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_main(self, *args: str) -> tuple[int, str]:
        argv = [str(SCRIPT), "--codex-home", str(self.home), *args]
        stdout = io.StringIO()
        with mock.patch.object(sys, "argv", argv), redirect_stdout(stdout):
            result = finder.main()
        return result, stdout.getvalue()

    def test_default_requires_all_terms(self) -> None:
        result, output = self.run_main("--query", "alpha beta")
        self.assertEqual(result, 0)
        self.assertIn(SESSION_A, output)
        self.assertNotIn(SESSION_B, output)

    def test_any_match_and_workspace_fallback(self) -> None:
        result, output = self.run_main("--query", "beta gamma", "--match", "any")
        self.assertEqual(result, 0)
        self.assertIn(SESSION_A, output)
        self.assertIn(SESSION_B, output)
        self.assertIn("workspaces: /work/gamma", output)

    def test_word_mode_avoids_short_substring_noise(self) -> None:
        result, output = self.run_main(
            "--query", "PI", "--term-mode", "word", "--json"
        )
        self.assertEqual(result, 0)
        payload = json.loads(output)
        self.assertEqual([item["session_id"] for item in payload], [SESSION_A])
        self.assertEqual(len(payload[0]["matches"]), 1)
        self.assertIn("PI_ contract", payload[0]["matches"][0]["snippet"])

    def test_since_filters_older_rows(self) -> None:
        result, output = self.run_main(
            "--query", "alpha gamma", "--match", "any", "--since", "150"
        )
        self.assertEqual(result, 0)
        self.assertNotIn("alpha beta", output)
        self.assertIn("alpha gamma", output)
        self.assertIn("gamma delta", output)

    def test_until_is_exclusive_and_filters_newer_rows(self) -> None:
        result, output = self.run_main(
            "--query", "alpha gamma", "--match", "any", "--until", "200"
        )
        self.assertEqual(result, 0)
        self.assertIn("alpha beta", output)
        self.assertNotIn("alpha gamma", output)
        self.assertNotIn("gamma delta", output)

    def test_json_includes_timestamp_and_workspace(self) -> None:
        result, output = self.run_main("--query", "gamma", "--json")
        self.assertEqual(result, 0)
        payload = json.loads(output)
        self.assertEqual(payload[0]["matches"][0]["timestamp"], 200)
        self.assertEqual(payload[0]["workspaces"], ["/work/gamma"])


if __name__ == "__main__":
    unittest.main()
