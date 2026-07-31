# Cleanup Script Usage

Use this reference when running or validating the deterministic session cleanup script.

## Primary Tool

The deterministic shared cleanup tool is the script bundled with this skill:
- `codex-session-cleanup/scripts/remove_codex_session.py`

When the skill is installed under `$CODEX_HOME/skills`, that is usually:
- `$CODEX_HOME/skills/codex-session-cleanup/scripts/remove_codex_session.py`

Treat `$CODEX_HOME/scripts/remove_codex_session.py` as a host-local convenience copy, not the shared source of truth.

## Supported Invocation

Use exactly one of:

```bash
python3 "$CODEX_HOME/skills/codex-session-cleanup/scripts/remove_codex_session.py" --codex-home "$CODEX_HOME" --session-id SESSION_ID --dry-run
python3 "$CODEX_HOME/skills/codex-session-cleanup/scripts/remove_codex_session.py" --codex-home "$CODEX_HOME" --session-id SESSION_ID
python3 "$CODEX_HOME/skills/codex-session-cleanup/scripts/remove_codex_session.py" --codex-home "$CODEX_HOME" --name THREAD_ALIAS
```

## What It Removes

- Before mutation, a recoverable snapshot is written under `$CODEX_HOME/backups/session-cleanup/`.
- rollout transcript file under `sessions/...`
- matching rows in `history.jsonl`
- matching rows in `session_index.jsonl`
- matching `threads` row in `state_5.sqlite`
- thread-edge and assigned-thread references that do not cascade automatically

## Verification

After the script runs, confirm:
- the reported backup directory contains the affected JSONL, SQLite, and rollout files
- no `threads.id = SESSION_ID`
- no matching rows remain in `history.jsonl`
- no matching rows remain in `session_index.jsonl`
- no rollout file remains for the removed session
