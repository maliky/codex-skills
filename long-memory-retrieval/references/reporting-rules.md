# Reporting Rules

## Always distinguish source type

When reporting recovered information, say whether it came from:
- `history.jsonl`
- `session_index.jsonl`
- `sessions/...jsonl`
- local summary files such as `skills/README.org` or `Meta/AGENTS.md`

## Confidence labels

Use these mental categories:
- high confidence:
  - directly stated in a local file
- medium confidence:
  - reconstructed from several consistent traces
- low confidence:
  - inferred from sparse evidence

## Good output shape

A good retrieval answer usually contains:
- topic summary
- matching session ids
- thread names when available
- notable repeated workflows
- brief note on evidence quality

## Guardrails

- never present inference as exact memory
- do not claim a skill is already implemented if only discussed
- when the raw files and a summary file disagree, trust the raw files
- keep the answer grounded in the local repository, not generic expectations
