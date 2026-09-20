---
name: codex-session-cleanup
description: "Use when removing exact local Codex sessions, cleaning empty sessions, diagnosing session writer locks, or repairing session records across local indexes, rollouts, and SQLite stores."
---

# Codex Session Cleanup

Remove only local Codex session records the user explicitly targets. Treat deletion as destructive and keep reusable skill files separate from raw transcript cleanup.

For an unlock or resume repair, use the lock-recovery route below; the removal script deletes conversation records and is not an unlock operation.

## Avoid When

- The user only wants memory retrieval or prior-session context; use `long-memory-retrieval`.
- The request is about suppressing low-value material without deleting raw records.
- The target is fuzzy, guessed, or based only on a semantic similarity match.
- The request touches skills, plugins, auth state, logs, or unrelated caches.

## Workflow

1. Resolve the target exactly from the provided id or alias.
2. Inspect `history.jsonl`, `session_index.jsonl`, `sessions/...jsonl`, and `state_5.sqlite` before deletion.
3. Prefer the bundled cleanup script over manual JSONL or SQL edits.
4. Probe SQLite schema before touching optional tables.
5. Verify after deletion and report any residual references that belong to other sessions.
6. Keep the skill-local cleanup script canonical; root-level copies under `$CODEX_HOME/scripts` are host-local conveniences.

## Scripts

Use the bundled script for deterministic cleanup:

```bash
python3 scripts/remove_codex_session.py --codex-home "$CODEX_HOME" --session-id SESSION_ID --dry-run
python3 scripts/remove_codex_session.py --codex-home "$CODEX_HOME" --session-id SESSION_ID
python3 scripts/remove_codex_session.py --codex-home "$CODEX_HOME" --name THREAD_ALIAS
```

Default `--codex-home` is `$CODEX_HOME` or `~/.codex`.

## Routes

- **Locked session or failed resume**: read [session lock recovery](references/session-lock-recovery.md).
- **Exact session removal**: read [cleanup script usage](references/cleanup-script-usage.md), dry-run the script, run it, then verify all stores.
- **Empty-session cleanup**: read [cleanup heuristics](references/cleanup-heuristics.md), list ids first, delete in a bounded batch, then verify counts.
- **Script sharing or sync**: read [script sharing](references/script-sharing.md) before comparing root-local and skill-local copies.
- **Manual recovery**: inspect stores directly only when the script is missing or fails; keep edits schema-aware and minimal.

## Output Expectations

Report removed session ids, removed aliases, backup location, rollout/history/index/thread-row counts, and residual references intentionally left because they belong to another session.
