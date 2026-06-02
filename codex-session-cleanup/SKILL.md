---
name: codex-session-cleanup
description: Remove low-value or explicitly targeted local Codex sessions from the file-based transcript store and thread state database. Use when the user wants to delete local Codex sessions by exact session id or exact thread-name alias, clean blank or nearly empty sessions, or reconcile stale session references in history.jsonl, session_index.jsonl, sessions/...jsonl, and state_5.sqlite.
metadata:
  author: local-codex
  maturity: draft
---

# Codex Session Cleanup

Use this skill when the user explicitly wants local Codex sessions removed from the active Codex environment rather than merely suppressed from retrieval.

This skill is for:
- removing a session by exact session id
- removing a session by exact alias from `session_index.jsonl`
- cleaning clearly empty, dot-only, or test sessions
- reconciling file-based session records with `state_5.sqlite`

This skill is not for:
- general memory retrieval; use `long-memory-retrieval`
- deciding whether a session should be suppressed or promoted into a skill
- fuzzy search or semantic matching of session names
- deleting logs, auth state, plugins, or unrelated cache data

## Workflow

1. Resolve the target exactly.
   - Prefer exact `session_id` when the user provides it.
   - If the user provides a name, match exact aliases from `session_index.jsonl`.
   - Treat multiple aliases for the same id as the same session.

2. Inspect the local stores before deletion.
   - Check `history.jsonl`, `session_index.jsonl`, `sessions/...jsonl`, and `state_5.sqlite`.
   - Confirm whether the target has transcript rows, index aliases, rollout files, and thread rows.

3. Use the environment cleanup script when available.
   - The recommended deterministic tool path is:
     - `$CODEX_HOME/scripts/remove_codex_session.py`
   - Use it as the primary cleanup path rather than ad hoc manual edits.

4. Verify after deletion.
   - Confirm the rollout file is gone if it previously existed.
   - Confirm the `history.jsonl` and `session_index.jsonl` rows are gone.
   - Confirm the matching `threads` row is gone from `state_5.sqlite`.
   - Confirm thread-edge or assigned-thread references no longer point at the removed id.

## Preferred Routes

### Remove one named or identified session

- Start by reading:
  - [cleanup script usage](references/cleanup-script-usage.md)

- Default route:
  1. resolve exact id or alias
  2. run `remove_codex_session.py`
  3. verify all local stores

### Clean empty or nearly empty sessions

- Start by reading:
  - [cleanup heuristics](references/cleanup-heuristics.md)

- Default route:
  1. identify dot-only, blank-title, or test sessions
  2. list exact ids before deletion
  3. remove them one by one or in a bounded batch
  4. verify the batch with post-cleanup queries

## Operating Rules

- Deletion is destructive. Use this skill only when the user clearly asked for cleanup.
- Prefer the deterministic Python cleanup script over direct SQL or manual JSONL surgery.
- Match names exactly; do not guess.
- When a history line merely mentions a deleted session id in a different session, do not treat that as a cleanup failure.

## Deliverables

When using this skill, the output should usually include:
- the removed session ids
- aliases removed for each id when available
- whether rollout files, history rows, index rows, and thread rows were removed
- any residual references that were intentionally left because they belong to a different session

## References

- [cleanup script usage](references/cleanup-script-usage.md)
- [cleanup heuristics](references/cleanup-heuristics.md)
