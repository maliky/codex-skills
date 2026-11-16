# Supported Deletion And Legacy Fallback

## Current CLI

Resolve an exact authorized UUID and inspect installed `codex delete --help`. Check active writers; do not delete the current conversation or a live session without resolving ownership first. Use the supported `codex delete --force SESSION_UUID` only for that target. Do not assume a dry-run flag exists; preflight identity and counts read-only instead.

If a restricted invocation fails, distinguish daemon/socket access from a session error. Retry through the environment's permitted host-access approval mechanism when needed and already within scope. Do not disable controls or fall back to SQL merely because a command failed.

Verify the selected rollout and index entry, matching rows in `state_5.sqlite`, and any `thread_history_1.sqlite` tables. Inspect the actual schema with read-only connections; optional stores and columns vary by installed version. Inspect other stores for target ownership without removing whole databases. Row deletion may leave allocated free pages, so report measured filesystem savings rather than promising the shared database shrinks.

## Residual Prompt History

The CLI can leave `history.jsonl` entries. For the same authorized target, remove only rows whose structured `session_id` equals the UUID, preserving other bytes and formatting. A UUID mentioned inside another session's text is not a target record. Stage on the same filesystem, preserve permissions/ownership, compare original inode, size and nanosecond modification time immediately before atomic replacement, and discard/retry if they changed. With active writers, coordinate a quiescent window: a stat check alone cannot prevent a writer racing afterward. Never restore stale whole-history copies over concurrent work.

## Legacy Helper

`scripts/remove_codex_session.py` predates the multi-store layout and rejects known modern history, goals, queue and memory databases and WAL/SHM sidecars. Absence of those names alone does not establish compatibility. Use the helper only after confirming that the CLI lacks the required deletion command, the actual schema is covered, and no writer is active. Root-local copies are not alternate authority.

Legacy flags remain `--codex-home`, exactly one of `--session-id` or `--name`, and optional `--dry-run`. Mutation first creates a recoverable snapshot under `backups/session-cleanup/`; measure its cost and agree retention before using it on a full disk. Dry-run and legacy tests do not establish support for a modern runtime.

Report method, exact-ID residuals and any agreed backup location. Keep memories, skills, project assets and unrelated session records outside the deletion scope.
