# Retrieval Workflow

## Default search order

1. `session_index.jsonl`
2. `history.jsonl`
3. `sessions/...jsonl`

In practice:
- use `history.jsonl` for topic recall
- use `session_index.jsonl` to name and order sessions
- use `sessions/...jsonl` for deep follow-up only

## Topic retrieval

When asked about a domain such as policy, curriculum, forms, or skills:

1. search `history.jsonl` with the user’s terms and close variants
2. collect candidate session ids
3. resolve thread names via `session_index.jsonl`
4. if needed, open one or more `sessions/...jsonl` files for the best candidates
5. summarize the result with confidence labels

## Recovering prior decisions

Use transcript files when you need:
- exact earlier plans
- earlier tradeoffs
- confirmation that a workflow was repeated enough to justify a skill

Do not start there unless the compact sources are insufficient.

## Search habits

- prefer `rg` for discovery
- search multiple near-synonyms when the user may not remember exact wording
- keep a list of candidate session ids before opening transcripts
- stop expanding context once the answer is stable
