# Script Sharing

Use this reference when comparing or synchronizing cleanup scripts across hosts.

## Canonical Location

- Shared cleanup tooling lives in `codex-session-cleanup/scripts/remove_codex_session.py`.
- The shareable repo boundary is `/home/mlk/.codex/skills`, not the root `/home/mlk/.codex` tree.
- Root-level files such as `/home/mlk/.codex/scripts/remove_codex_session.py` are host-local convenience copies.

## Why Root Copies Are Not Canonical

The root `.codex` tree contains host state such as auth files, sessions, caches, logs, and SQLite databases. Do not connect or publish the root tree as the shared script repo.

When comparing root and skill-local copies, preserve the portable interface:

- `--codex-home`
- exact `--session-id`
- exact `--name`
- `--dry-run`
- schema-aware optional table handling

Do not overwrite the skill-local script with a hard-coded host copy. If a root copy has a useful fix, port the fix into the skill-local script while preserving portability.
