---
name: long-memory-retrieval
description: "Use when recovering previous Codex work from history.jsonl, session_index.jsonl, and sessions/...jsonl, inventorying recently active root or subagent rollouts, identifying prior decisions, mapping thread names and workspaces, searching short codes without substring noise, finding repeated workflows for skills, or deciding what local memory evidence should be promoted, referenced, suppressed, or archived."
---

# Long Memory Retrieval

Recover prior work from local file evidence. Search lightweight indexes first, inspect active rollout metadata when recency matters, open transcript text only when needed, and keep exact evidence separate from inference.

## Avoid When

- The request is to delete sessions; use `codex-session-cleanup`.
- The task requires SQLite forensics.
- The user wants generic web research or non-local facts.
- A single current file inspection answers the question.

## Workflow

1. Search `history.jsonl` for the user's terms and close variants, optionally bounded by time. Use word mode for short codes that would otherwise match inside unrelated words.
2. Resolve session ids and aliases through `session_index.jsonl`; use first-line `session_meta` records to recover workspaces when the index is sparse.
3. When current activity may not yet be in history, inventory recently modified rollouts and distinguish root sessions from subagents.
4. Open narrowed `sessions/...jsonl` files only for prior plans, exact commands, or richer reconstruction, and extract text roles rather than image or tool payloads.
5. For a host-wide audit, cluster by repeated workflow and repository rather than by one broad keyword.
6. Classify candidates as `promote`, `reference`, `suppress`, or `archive-candidate` and report source type, confidence, and inference boundaries.

## Scripts

```bash
python3 scripts/find_sessions.py --codex-home "$CODEX_HOME" --query "topic words"
python3 scripts/find_sessions.py --codex-home "$CODEX_HOME" --query "FI PI" --match any --term-mode word --json
python3 scripts/inventory_rollouts.py --codex-home "$CODEX_HOME" --modified-since 2026-08-09 --json
python3 scripts/inventory_rollouts.py --codex-home "$CODEX_HOME" --modified-since 2026-08-09 --include-subagents
```

`find_sessions.py` searches compact history and attaches aliases and workspaces. `inventory_rollouts.py` streams only metadata and user text from recently modified JSONL files; it excludes subagents by default. Open complete transcripts only after narrowing candidates.

## Routes

- **Find prior or active work**: read [sources](references/sources.md) and [retrieval workflow](references/retrieval-workflow.md).
- **Infer or audit skills**: read [qualitative synthesis](references/qualitative-synthesis.md), then [forgetting and suppression](references/forgetting-and-suppression.md).
- **Report recovered evidence**: read [reporting rules](references/reporting-rules.md).

## Output Expectations

Include main session and rollout ids, parent relationship for subagents, thread names or aliases, workspaces, source files used, a short recovered theme, and promotion/suppression labels when requested.
