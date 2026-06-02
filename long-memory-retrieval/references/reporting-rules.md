# Reporting Rules

Use this reference when reporting recovered memory evidence, confidence, and inference boundaries.

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
- current thread names when available
- older thread-name aliases when the same session was renamed
- notable repeated workflows
- what to promote, keep as reference, suppress, or mark as an archive candidate when relevant
- brief note on evidence quality

## Guardrails

- never present inference as exact memory
- do not claim a skill is already implemented if only discussed
- when the raw files and a summary file disagree, trust the raw files
- keep the answer grounded in the local repository, not generic expectations
- do not recommend deleting raw memory unless the user explicitly asks for destructive cleanup

## Rename-aware reporting

- if `session_index.jsonl` records several names for one session id, report one session, not several
- prefer the newest thread name as the primary label
- mention older names only as aliases or prior labels

## Failure modes

- sparse `session_index.jsonl` entries may leave some sessions unnamed
- one topic may span several thread names and several sessions
- compact `history.jsonl` records may omit the detail needed to justify a strong conclusion
- transcript files may be needed to separate exact evidence from theme-level inference
