# Qualitative Synthesis

## Goal

Turn many local session traces into a stable summary of recurring work in the active Codex environment.

## What counts as a candidate skill

A workflow is a good skill candidate when:
- it appears in multiple sessions
- it has recognizable repeated steps
- it has recurring constraints or house rules
- it would help another agent perform similar work later

## What does not count yet

- a one-off request
- a topic mentioned once without repeated execution
- a broad theme with no clear workflow
- a failed intermediate technique that the later session explicitly replaced

## Clustering rule

Group sessions by repeated workflow, not by vague topic label.

Examples:
- policy authoring
- curriculum transformation
- memory retrieval
- IRB/research forms
- document conversion

Do not over-split early. Prefer one stable skill over several tiny overlapping ones.

## Attention hygiene

After clustering, classify each cluster:
- promote repeated stable workflows
- keep useful but narrow traces as references
- suppress duplicates, abandoned approaches, and non-recurring work
- mark generated backups or scratch files as archive candidates instead of treating them as knowledge

## Evidence types

- direct:
  - explicit user request
  - explicit earlier plan
  - explicit skill discussion

- indirect:
  - repeated similar requests across sessions
  - repeated file types, tools, or output patterns

Use both, but label inference clearly.
