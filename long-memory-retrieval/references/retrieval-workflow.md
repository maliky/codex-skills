# Retrieval Workflow

Use this reference when searching local Codex history and narrowing from indexes to transcript files.

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
5. run a forgetting pass to suppress duplicates, abandoned attempts, and one-off noise
6. summarize the result with confidence labels

## Useful commands

```bash
rg -n -i "topic words here" "$CODEX_HOME/history.jsonl"
rg -n '"session_id":"SESSION_ID"' "$CODEX_HOME/history.jsonl"
rg -n '"id":"SESSION_ID"|\"thread_name\"' "$CODEX_HOME/session_index.jsonl"
rg -n -i "topic words here" "$CODEX_HOME/sessions"
sed -n 'N,Mp' "$CODEX_HOME/history.jsonl"
```

Use these as a progression, not all at once.

## Session rename handling

- if one session id appears several times in `session_index.jsonl` with different thread names, merge them into one session record
- use the most recent `updated_at` row as the current display name
- keep older thread names as aliases when they help explain older references or user wording

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
- do not let one very long renamed session dominate the answer unless it is clearly the best source
