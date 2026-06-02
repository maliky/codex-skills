# Sources

Use this reference when choosing which local Codex memory files to inspect and how much weight to give each source.

## Primary File-Based Memory Sources

### `history.jsonl`

- one JSON object per line
- compact, high-signal record of user requests and topic flow
- best first stop for:
  - topic discovery
  - repeated phrases
  - repeated workflows
  - quick session id collection

Weakness:
- compact only; it often lacks the richer decision context

### `session_index.jsonl`

- one JSON object per line
- maps session id to thread name and updated time
- best for:
  - attaching names to session ids
  - ordering by recency
  - recognizing thread-level clusters
  - detecting rename history when the same session id appears with different thread names

Weakness:
- lightweight only; not enough for decision reconstruction

Important note:
- do not assume one session id has one permanent thread name
- if the same id appears more than once with different `thread_name` values, treat that as rename tracking
- use the most recent name as the current label and preserve the older names as aliases when reporting

### `sessions/YYYY/MM/DD/rollout-...jsonl`

- one JSON event per line
- includes metadata, messages, tool calls, outputs, and previous plans
- best for:
  - richer reconstruction
  - understanding how a workflow was practiced
  - recovering prior plans and decisions

Weakness:
- expensive to read first; use after narrowing the search

### `skills/README.org`

- current local backlog of candidate and drafted skills
- useful for:
  - checking what has already been recognized as a stable workflow
  - grounding “what skills exist here now”

### `Meta/AGENTS.md`

- local note about memory recovery and source hierarchy
- useful as workflow guidance

Weakness:
- it is a summary, not the source of truth

## Out of scope for this skill

- `state_5.sqlite`
- `logs_1.sqlite`

They exist, but this v1 skill intentionally ignores them.
