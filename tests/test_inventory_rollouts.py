from __future__ import annotations

import importlib.util
import io
import json
import os
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
    / "inventory_rollouts.py"
)
SPEC = importlib.util.spec_from_file_location("inventory_rollouts", SCRIPT)
assert SPEC and SPEC.loader
inventory = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = inventory
SPEC.loader.exec_module(inventory)

SESSION_A = "019e87f4-9cf1-7e50-afd4-8d73a5788538"
ROLLOUT_B = "019e87f4-9cf1-7e50-afd4-8d73a5788539"


def message(timestamp: str, role: str, text: str) -> dict[str, object]:
    return {
        "timestamp": timestamp,
        "type": "response_item",
        "payload": {
            "type": "message",
            "role": role,
            "content": [{"type": "input_text", "text": text}],
        },
    }


class InventoryRolloutsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.home = Path(self.temp.name)
        sessions = self.home / "sessions" / "2026" / "01"
        sessions.mkdir(parents=True)
        (self.home / "session_index.jsonl").write_text(
            json.dumps({"id": SESSION_A, "thread_name": "root-thread"}) + "\n",
            encoding="utf-8",
        )

        self.root_rollout = sessions / f"rollout-{SESSION_A}.jsonl"
        self.write_events(
            self.root_rollout,
            [
                {
                    "timestamp": "2026-01-01T00:00:00Z",
                    "type": "session_meta",
                    "payload": {
                        "id": SESSION_A,
                        "session_id": SESSION_A,
                        "cwd": "/work/root",
                        "source": "cli",
                        "thread_source": "user",
                    },
                },
                message("2026-01-01T00:00:01Z", "user", "<environment_context>ignored"),
                message("2026-01-01T00:00:02Z", "user", "real request"),
                {
                    "timestamp": "2026-01-01T00:00:03Z",
                    "type": "response_item",
                    "payload": {"type": "tool_result", "data": "image payload"},
                },
            ],
        )
        os.utime(self.root_rollout, (200, 200))

        self.subagent_rollout = sessions / f"rollout-{ROLLOUT_B}.jsonl"
        self.write_events(
            self.subagent_rollout,
            [
                {
                    "timestamp": "2026-01-01T00:01:00Z",
                    "type": "session_meta",
                    "payload": {
                        "id": ROLLOUT_B,
                        "session_id": SESSION_A,
                        "parent_thread_id": SESSION_A,
                        "cwd": "/work/root",
                        "source": {"subagent": {"depth": 1}},
                        "thread_source": "subagent",
                    },
                },
                message("2026-01-01T00:01:01Z", "user", "implement the plan"),
            ],
        )
        os.utime(self.subagent_rollout, (300, 300))

    def tearDown(self) -> None:
        self.temp.cleanup()

    @staticmethod
    def write_events(path: Path, events: list[dict[str, object]]) -> None:
        path.write_text(
            "".join(json.dumps(event) + "\n" for event in events),
            encoding="utf-8",
        )

    def run_main(self, *args: str) -> tuple[int, str]:
        argv = [str(SCRIPT), "--codex-home", str(self.home), *args]
        stdout = io.StringIO()
        with mock.patch.object(sys, "argv", argv), redirect_stdout(stdout):
            result = inventory.main()
        return result, stdout.getvalue()

    def test_default_includes_only_root_and_real_user_text(self) -> None:
        result, output = self.run_main("--modified-since", "100", "--json")
        self.assertEqual(result, 0)
        payload = json.loads(output)
        self.assertEqual(len(payload), 1)
        self.assertEqual(payload[0]["rollout_id"], SESSION_A)
        self.assertEqual(payload[0]["aliases"], ["root-thread"])
        self.assertEqual(payload[0]["user_message_count"], 1)
        self.assertEqual(payload[0]["last_user_messages"], ["real request"])
        self.assertEqual(payload[0]["last_event_at"], "2026-01-01T00:00:03Z")

    def test_include_subagents_preserves_parent_identity(self) -> None:
        result, output = self.run_main(
            "--modified-since", "100", "--include-subagents", "--json"
        )
        self.assertEqual(result, 0)
        payload = json.loads(output)
        subagent = next(item for item in payload if item["is_subagent"])
        self.assertEqual(subagent["rollout_id"], ROLLOUT_B)
        self.assertEqual(subagent["main_session_id"], SESSION_A)
        self.assertEqual(subagent["parent_thread_id"], SESSION_A)

    def test_user_text_is_bounded(self) -> None:
        payload = message("2026-01-01T00:02:00Z", "user", "x" * 1500)["payload"]
        text = inventory.user_text(payload)
        self.assertEqual(len(text), inventory.MAX_MESSAGE_CHARS)
        self.assertTrue(text.endswith("..."))

    def test_modified_since_filters_by_file_mtime(self) -> None:
        result, output = self.run_main(
            "--modified-since", "250", "--include-subagents", "--json"
        )
        self.assertEqual(result, 0)
        payload = json.loads(output)
        self.assertEqual([item["rollout_id"] for item in payload], [ROLLOUT_B])


if __name__ == "__main__":
    unittest.main()
