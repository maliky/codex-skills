# Cleanup Script Usage

## Primary Tool

The deterministic cleanup tool is usually:
- `$CODEX_HOME/scripts/remove_codex_session.py`

## Supported Invocation

Use exactly one of:

```bash
python3 "$CODEX_HOME/scripts/remove_codex_session.py" --session-id SESSION_ID
python3 "$CODEX_HOME/scripts/remove_codex_session.py" --name THREAD_ALIAS
```

## What It Removes

- rollout transcript file under `sessions/...`
- matching rows in `history.jsonl`
- matching rows in `session_index.jsonl`
- matching `threads` row in `state_5.sqlite`
- thread-edge and assigned-thread references that do not cascade automatically

## Verification

After the script runs, confirm:
- no `threads.id = SESSION_ID`
- no matching rows remain in `history.jsonl`
- no matching rows remain in `session_index.jsonl`
- no rollout file remains for the removed session
