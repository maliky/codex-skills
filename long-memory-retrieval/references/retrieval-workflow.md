# Retrieval Workflow

Use this reference when searching local Codex history and narrowing from indexes to transcript files.

## Default Search Order

1. `session_index.jsonl`
2. `history.jsonl`
3. first-line `session_meta` from recently modified rollouts
4. selected user/assistant text from narrowed rollouts

Use history for topic recall, the index for aliases, rollout metadata for active or sparse sessions, and transcript text only for deep follow-up.

## Topic Retrieval

1. Search history with the user's terms and close variants.
2. Use `--term-mode word` for short identifiers such as `PI`, `FI`, repository codes, or CLI flags that could occur inside unrelated words.
3. Collect candidate session ids and aliases.
4. If recency matters, inventory rollouts modified since the relevant cutoff.
5. Open only the best transcript candidates for exact plans or decisions.
6. Suppress duplicates, abandoned attempts, and one-off noise; summarize with confidence labels.

## Host-Wide Skill Audit

1. Inventory `history.jsonl` by session id, first/last timestamp, and request count.
2. Inventory recently modified root rollouts because active turns may not yet be represented in history.
3. Use the current skills repository commit or audit time as a cutoff, while also sampling older workflows with no matching skill.
4. Search several concrete workflow terms; use word mode for short codes and `--match any` only when intentional.
5. Attach aliases from `session_index.jsonl` and workspaces from rollout `session_meta`.
6. Distinguish `payload.id` (unique rollout), `payload.session_id` (main session, sometimes inherited by a subagent), and `parent_thread_id`.
7. Group root-session evidence by repository and repeated operational sequence. Use subagent traces only to recover implementation detail, not as independent user demand.
8. Compare each cluster against current skill descriptions and routed references, then classify it as a new skill, an update, a reference trace, or suppressed noise.

Prefer one project skill plus focused generic updates over overlapping micro-skills.

## Useful Commands

```bash
rg -n -i "topic words here" "$CODEX_HOME/history.jsonl"
rg -n '"session_id":"SESSION_ID"' "$CODEX_HOME/history.jsonl"
rg -n '"id":"SESSION_ID"|"thread_name"' "$CODEX_HOME/session_index.jsonl"
python3 scripts/find_sessions.py --codex-home "$CODEX_HOME" --query "term1 term2" --match any --since 2026-08-01
python3 scripts/find_sessions.py --codex-home "$CODEX_HOME" --query "FI PI" --match any --term-mode word
python3 scripts/inventory_rollouts.py --codex-home "$CODEX_HOME" --modified-since 2026-08-09 --json
```

## Session And Subagent Identity

- Merge repeated index rows for one main session and keep older thread names as aliases.
- Prefer the newest `updated_at` name as the display name.
- In rollout metadata, use `payload.id` as the unique rollout id.
- A subagent may inherit its parent's `payload.session_id`; report `parent_thread_id` and do not count it as another user session.
- Root rollouts normally have `thread_source=user`; subagents normally have `thread_source=subagent` or a structured `source.subagent` value.

## Search Habits

- Search multiple near-synonyms when wording is uncertain.
- Keep candidate ids before opening transcripts and stop once the answer is stable.
- Do not let one long renamed session dominate unless it is clearly the best source.
- For large or image-heavy rollouts, parse JSONL one event at a time and select only user/assistant text messages; never dump image, audio, base64, or tool payloads.
