---
name: codex-session-cleanup
description: "Use when removing exact local Codex sessions, cleaning empty sessions, diagnosing session writer locks, or repairing session records across local indexes, rollouts, and SQLite stores."
---

# Codex Session Cleanup

Remove only local Codex session records the user explicitly targets. Treat deletion as destructive and keep reusable skill files separate from raw transcript cleanup.

For an unlock or resume repair, use the lock-recovery route below; the removal script deletes conversation records and is not an unlock operation.

## Avoid When

- Codex cannot initialize any session, or the problem concerns daemon readiness or shared-storage SQLite failures; use [Codex Runtime Recovery](../codex-runtime-recovery/SKILL.md).
- The user only wants memory retrieval or prior-session context; use `long-memory-retrieval`.
- The request is about suppressing low-value material without deleting raw records.
- The target is fuzzy, guessed, or based only on a semantic similarity match.
- The request touches skills, plugins, auth state, logs, or unrelated caches.

## Workflow

1. Resolve the exact authorized UUID from the index and metadata; identify active writers before removal.
2. Read the installed `codex delete --help` and current storage layout. Prefer the supported CLI over direct JSONL/SQL deletion; read [supported deletion and legacy fallback](references/cleanup-script-usage.md).
3. Inventory only relevant counts and sizes. Agree any backup policy rather than automatically copying shared databases or oversized transcripts onto a full disk.
4. After deletion, verify the transcript, exact index entry, current SQLite stores and exact-ID prompt-history rows independently with read-only, schema-aware inspection.
5. Preserve other sessions, references inside their text, shared databases, skills and assets. Do not remove a shared database to reclaim one conversation.

## Commands

After exact-target authorization and checking current help:

```bash
codex delete --force SESSION_UUID
```

`--force` suppresses the CLI prompt; it does not replace user authorization. Do not assume a dry-run flag exists. The bundled script is a legacy-only fallback and rejects known modern stores before database access. Host-local copies can be stale; never use them to bypass that guard.

## Routes

- **Locked session or failed resume**: read [session lock recovery](references/session-lock-recovery.md).
- **Exact session removal**: read [supported deletion and legacy fallback](references/cleanup-script-usage.md), use the CLI, then verify all stores.
- **Empty-session cleanup**: read [cleanup heuristics](references/cleanup-heuristics.md), list ids first, delete in a bounded batch, then verify counts.
- **Script sharing or sync**: read [script sharing](references/script-sharing.md) before comparing root-local and skill-local copies.
- **Manual recovery**: diagnose CLI failure before considering any separately reviewed direct-store procedure; failure is not authorization for SQL deletion.

## Output Expectations

Report the exact target, deletion method, verified residual counts, backup policy actually used and measured space change. Distinguish transcripts from shared databases, logs and caches.
