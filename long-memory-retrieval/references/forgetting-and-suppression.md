# Forgetting And Suppression

## Purpose

Free attention without destroying the raw local record.

Use this reference when the user asks what can be forgotten, suppressed, archived, or not promoted into skills.

## Labels

- `promote`: repeated workflow with stable steps; update or create a skill.
- `reference`: useful prior work that should be findable but not loaded by default.
- `suppress`: duplicate, stale, failed, abandoned, or one-off material that should not guide normal answers.
- `archive-candidate`: generated, backup, scratch, or redundant artifact that may be removed after explicit permission.

## Suppress By Default

- duplicate user prompts and repeated correction turns that add no new decision
- failed command attempts after a later working method was found
- abandoned regex or script fragments when the user explicitly said to drop them
- transient GUI, package, or environment debugging outside the task that needs it
- one-off app setup or deployment traces unless the same workflow recurs
- plugin/system details unless the user asks about those systems

## Keep As Reference

- final working command patterns
- reusable scripts and their constraints
- session ids connected to stable topic clusters
- decisions about source precedence, file formats, or validation
- lessons from failures when they prevent likely repetition

## Promote To Skills

Promote only when the workflow is repeated and operational:
- stable trigger phrase or task family
- recurring files, formats, or repositories
- repeated constraints or house rules
- clear validation method

Do not create a skill from a single interesting session unless the user explicitly wants a draft.

## Deletion Guardrail

Do not delete `history.jsonl`, `session_index.jsonl`, or `sessions/...jsonl` as part of forgetting.

For removable artifacts such as editor backups, generated scratch files, or obsolete exported outputs, report them as `archive-candidate` and ask or wait for explicit deletion permission if removal is destructive.
