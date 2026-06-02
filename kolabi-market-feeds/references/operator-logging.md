# Operator Logging

Use this reference when feed behavior affects operator trust or console action visibility.

## Logging guidance

- keep action lines compact and action-focused
- include symbol, pair, event id, and effect when possible
- keep private feed noise out unless it directly impacts command safety
- prefer one-line summaries over multiline dumps

## Suggested fields

- symbol or pair
- status transition
- source (`public`, `private`, reconciliation)
- action result
