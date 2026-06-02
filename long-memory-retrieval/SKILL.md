---
name: long-memory-retrieval
description: Recover previous Codex work from history.jsonl, session_index.jsonl, and sessions/...jsonl. Use when a task asks what was done before on this host, which sessions or thread names covered a topic, what prior decisions should be reused, what repeated workflows should become skills, or what should be suppressed to free attention. Handle session renames by treating thread names in session_index.jsonl as aliases for the same session id. Ignore SQLite for this skill.
metadata:
  author: local-codex
  maturity: draft
---

# Long Memory Retrieval

Use this skill when the user wants to recover what happened previously on this host from the local Codex repository, especially from session history and transcript files.

This skill is for:
- finding sessions related to a topic
- mapping topic -> session ids -> thread names
- reconstructing prior decisions or prior plans
- identifying recurring workflows that should become skills
- summarizing what kinds of work have already been done on this host
- deciding what prior material should be suppressed, down-ranked, or kept only as reference

This skill is not for:
- SQLite inspection or database forensics
- recovering information not grounded in local files
- generic web research
- full-text document conversion
- deleting raw session or history files as a shortcut for attention management

## Workflow

1. Start with the lightweight indexes.
   - Use `session_index.jsonl` to find session ids, thread names, and recency.
   - Use `history.jsonl` to locate topic phrasing, repeated requests, and user terminology.

2. Narrow to candidate sessions before opening transcripts.
   - Prefer searching `history.jsonl` first for topic discovery.
   - Use `session_index.jsonl` to attach names where available.
   - Treat multiple thread names for the same session id as a rename history, not as different sessions.

3. Open `sessions/...jsonl` only for richer context.
   - Use transcript files when you need prior plans, exact reasoning context, or richer reconstruction than `history.jsonl` can provide.
   - Treat them as the qualitative deep source, not the first pass.

4. Use local meta files as guidance, not as stronger truth than the raw records.
   - `Meta/AGENTS.md` describes the intended recovery workflow.
   - `skills/README.org` describes the current local candidate skill catalog.
   - If those summaries conflict with the raw session files, trust the raw files.

5. Run a forgetting pass before reporting.
   - Mark each candidate as `promote`, `reference`, `suppress`, or `archive-candidate`.
   - Suppress duplicate prompts, abandoned attempts, failed intermediate commands, and one-off work that does not affect the current task.
   - Preserve raw memory by default; deletion requires explicit user intent.

6. Report recovered memory with source and confidence.
   - Exact evidence from `history.jsonl`
   - Indexed evidence from `session_index.jsonl`
   - Richer reconstructed evidence from `sessions/...jsonl`
   - Mark inference when clustering several traces into one skill theme

## Quick Patterns

Use these patterns to start fast:

```bash
rg -n -i "policy|curriculum|irb|skills" /home/mlk/.codex/history.jsonl
rg -n '"id":"SESSION_ID"|\"thread_name\"' /home/mlk/.codex/session_index.jsonl
rg -n -i "search phrase" /home/mlk/.codex/sessions
sed -n 'START,ENDp' /home/mlk/.codex/history.jsonl
```

Typical sequence:
1. search `history.jsonl`
2. collect session ids
3. resolve or merge thread names from `session_index.jsonl`
4. inspect matching `sessions/...jsonl` only if needed

## Preferred Retrieval Route

### Find prior work on a topic

- Start by reading:
  - [sources](references/sources.md)
  - [retrieval workflow](references/retrieval-workflow.md)

- Default route:
  1. search `history.jsonl` for the topic
  2. collect session ids
  3. attach thread names from `session_index.jsonl`, keeping rename aliases for the same id
  4. order or cluster the results
  5. open matching `sessions/...jsonl` only if needed for deeper context

### Infer candidate skills from host history

- Start by reading:
  - [qualitative synthesis](references/qualitative-synthesis.md)
  - [forgetting and suppression](references/forgetting-and-suppression.md)
  - [reporting rules](references/reporting-rules.md)

- Default route:
  1. search `history.jsonl` for repeated domains, workflows, and requests
  2. cluster related sessions by topic
  3. inspect one or two representative transcripts per cluster when needed
  4. propose skill names only when the workflow is stable and repeated

### Recover decisions, not just mentions

- Use `sessions/...jsonl` when you need:
  - prior plans
  - tool usage patterns
  - explicit tradeoffs
  - evidence that a skill or workflow was actually practiced, not only mentioned

### Free attention by suppressing stale material

- Start by reading:
  - [forgetting and suppression](references/forgetting-and-suppression.md)

- Default route:
  1. identify candidate sessions or artifacts with the normal retrieval route
  2. separate reusable decisions from noise
  3. label each item `promote`, `reference`, `suppress`, or `archive-candidate`
  4. recommend cleanup only for generated or backup artifacts, not raw history files

## Local Sources

Prioritize these local files:
- `history.jsonl`
- `session_index.jsonl`
- `sessions/YYYY/MM/DD/rollout-...jsonl`
- `skills/README.org`
- `Meta/AGENTS.md`

Ignore for this skill:
- `state_5.sqlite`
- `logs_1.sqlite`

## House Rules For This Host

- Treat local files as evidence, not memory in the human sense.
- Prefer retrieval from `history.jsonl` and `session_index.jsonl` before loading full transcripts.
- Do not claim a skill exists just because a topic appeared once.
- When the user asks about “skills done on this host”, look for repeated task families, explicit skill discussions, and recurring implementation patterns.
- Keep retrieval grounded in file paths and session ids where possible.
- If `session_index.jsonl` shows more than one thread name for the same session id, treat the newest thread name as the current label and older names as aliases.
- Forgetting means attention hygiene first: suppress or down-rank noise before considering deletion.

## Deliverables

When using this skill, the output should usually include:
- matching session ids and thread names when available
- a short summary of the recovered theme
- a note on which source types were used
- suppression or promotion labels when the user asks what to forget, keep, or turn into skills
- clear separation between exact evidence and inference

## References

- [sources](references/sources.md)
- [retrieval workflow](references/retrieval-workflow.md)
- [qualitative synthesis](references/qualitative-synthesis.md)
- [forgetting and suppression](references/forgetting-and-suppression.md)
- [reporting rules](references/reporting-rules.md)
