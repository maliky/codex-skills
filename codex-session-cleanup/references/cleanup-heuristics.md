# Cleanup Heuristics

## Good Removal Candidates

- dot-only sessions
- sessions with only `test`, `resume`, or similarly trivial content
- blank-title sessions with no useful alias or history
- duplicate or abandoned scratch sessions the user explicitly wants gone

## Keep But Suppress

- long sessions that are noisy but still contain important policy or curriculum decisions
- sessions with valuable class, conversion, or audit history mixed with chatter
- sessions that should become skills or references rather than be deleted

## Caution

- A row in `history.jsonl` may mention a deleted session id inside the text of another session. That is not a remaining session record.
- Several aliases in `session_index.jsonl` may belong to one session id. Remove by id, not by alias row count alone.
