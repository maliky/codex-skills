---
name: long-memory-retrieval
description: "Use when recovering previous Codex work from history.jsonl, session_index.jsonl, and sessions/...jsonl, identifying prior decisions, mapping thread names and session ids, finding repeated workflows for skills, or deciding what local memory evidence should be promoted, referenced, suppressed, or archived."
---

# Long Memory Retrieval

Recover prior work from local file evidence. Search lightweight indexes first, open transcripts only when needed, and keep exact evidence separate from inference.

## When to Use

- Find sessions related to a topic, project, file, or prior decision.
- Map session ids to current and previous thread names.
- Reconstruct plans, tradeoffs, commands, or repeated workflows.
- Decide what should become a skill, remain reference-only, or be suppressed from attention.

## Avoid When

- The request is to delete sessions; use `codex-session-cleanup`.
- The task requires SQLite forensics.
- The user wants generic web research or non-local facts.
- A single current file inspection answers the question.

## Workflow

1. Search `history.jsonl` for the user's terms and close variants.
2. Resolve session ids and aliases through `session_index.jsonl`.
3. Open `sessions/...jsonl` only for prior plans, exact commands, or richer reconstruction.
4. Classify candidates as `promote`, `reference`, `suppress`, or `archive-candidate` when attention hygiene matters.
5. Report source type, confidence, and whether a conclusion is exact evidence or inference.

## Scripts

Use the bundled finder for the first pass:

```bash
python3 scripts/find_sessions.py --codex-home "$CODEX_HOME" --query "topic words"
python3 scripts/find_sessions.py --codex-home "$CODEX_HOME" --query "topic words" --json
```

The script searches `history.jsonl` and attaches aliases from `session_index.jsonl`. Open transcripts only after narrowing candidates.

## Routes

- **Find prior work**: read [sources](references/sources.md) and [retrieval workflow](references/retrieval-workflow.md).
- **Infer skills**: read [qualitative synthesis](references/qualitative-synthesis.md), then [forgetting and suppression](references/forgetting-and-suppression.md).
- **Report recovered evidence**: read [reporting rules](references/reporting-rules.md).

## Output Expectations

Include session ids, thread names or aliases, source files used, a short recovered theme, and promotion/suppression labels when requested.

## References

- [sources](references/sources.md)
- [retrieval workflow](references/retrieval-workflow.md)
- [qualitative synthesis](references/qualitative-synthesis.md)
- [forgetting and suppression](references/forgetting-and-suppression.md)
- [reporting rules](references/reporting-rules.md)
