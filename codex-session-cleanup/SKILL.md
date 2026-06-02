---
name: codex-session-cleanup
description: "Use when removing local Codex sessions by exact session id or exact thread-name alias, cleaning blank or nearly empty sessions, or reconciling history.jsonl, session_index.jsonl, sessions/...jsonl, and state_5.sqlite without touching skills, plugins, logs, or unrelated cache data."
---

# Codex Session Cleanup

Remove only local Codex session records the user explicitly targets. Treat deletion as destructive and keep reusable skill files separate from raw transcript cleanup.

## When to Use

- Delete one session by exact id or exact `session_index.jsonl` alias.
- Clean bounded dot-only, blank-title, or test sessions after listing ids.
- Reconcile file-based session records with `state_5.sqlite`.
- Verify that a cleanup removed transcript, history, index, and thread rows together.

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

## Scripts

Use the bundled script for deterministic cleanup:

```bash
python3 scripts/remove_codex_session.py --codex-home "$CODEX_HOME" --session-id SESSION_ID --dry-run
python3 scripts/remove_codex_session.py --codex-home "$CODEX_HOME" --session-id SESSION_ID
python3 scripts/remove_codex_session.py --codex-home "$CODEX_HOME" --name THREAD_ALIAS
```

Default `--codex-home` is `$CODEX_HOME` or `~/.codex`.

## Routes

- **Exact session removal**: read [cleanup script usage](references/cleanup-script-usage.md), dry-run the script, run it, then verify all stores.
- **Empty-session cleanup**: read [cleanup heuristics](references/cleanup-heuristics.md), list ids first, delete in a bounded batch, then verify counts.
- **Manual recovery**: inspect stores directly only when the script is missing or fails; keep edits schema-aware and minimal.

## Output Expectations

Report removed session ids, removed aliases, rollout/history/index/thread-row counts, and residual references intentionally left because they belong to another session.

## References

- [cleanup script usage](references/cleanup-script-usage.md)
- [cleanup heuristics](references/cleanup-heuristics.md)
