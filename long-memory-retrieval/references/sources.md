# Sources

Use this reference when choosing which local Codex memory files to inspect and how much weight to give each source.

## Primary File-Based Memory Sources

### `history.jsonl`

- compact JSONL record of user requests and topic flow
- best first stop for topic discovery, repeated workflows, timestamps, and main session ids

Weakness: active turns can lag or be absent, and decision context is compact.

### `session_index.jsonl`

- maps main session ids to thread names and update times
- useful for recency, clustering, and rename history

Weakness: it can be sparse and is insufficient for decision reconstruction. Merge repeated ids, use the newest name, and preserve older names as aliases.

### `sessions/YYYY/MM/DD/rollout-...jsonl`

- one JSON event per line with metadata, messages, tools, and plans
- best for active-session discovery and narrowed reconstruction

The first `session_meta` event is cheap to inspect. `payload.id` identifies the unique rollout; `payload.session_id` identifies the main session and may be inherited by a subagent; `parent_thread_id`, `thread_source`, and structured `source.subagent` values distinguish subagents. `cwd` recovers the workspace when the index has no alias.

Weakness: image-generation and tool-heavy sessions can be hundreds of megabytes. Filter candidates by modification time, stream one event at a time, and read only selected `response_item` message text. Never emit raw image, audio, base64, or tool-result payloads.

### `skills/README.org`

- current personal skill inventory
- useful for checking what is already recognized as a stable workflow

### `Meta/AGENTS.md`

Local workflow guidance only; it is not the source of truth.

## Out Of Scope

This skill intentionally avoids `state_5.sqlite` and `logs_1.sqlite`; use a task-specific forensic workflow when those stores are required.
