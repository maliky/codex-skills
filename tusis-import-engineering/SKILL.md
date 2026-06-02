---
name: tusis-import-engineering
description: Use when building or debugging TUSIS/Django import pipelines for curriculum/course/student/grade/schedule data, including parser normalization, mapping resolution, duplicates, and batch reconciliation.
metadata:
  author: local-codex
  maturity: draft
---

# TUSIS Import Engineering

Use this skill when the task is repeated import plumbing rather than one-off data fixes.

This skill is for:
- stable parsing and normalization of ODT/DOCX extracted text, CSV, XLSX, and other import forms
- batch import orchestration for course and grade flows
- deduplication and conflict handling for curriculum/course entities
- resilient fallback behavior when source structures vary across curricula

This skill is not for:
- curriculum content rewriting without import impact
- pure UI/report formatting without import rules
- feed or websocket issues outside Django import runtime

## Workflow

1. Classify source and target.
   - determine whether the issue is curriculum, grade, student, or schedule import.
   - identify whether parsing, mapping, or DB constraints are failing.

2. Normalize input.
   - standardize separators, code formats, and whitespace
   - preserve source labels for future traceability
   - avoid irreversible rewrites at parse stage

3. Resolve mapping.
   - build deterministic mapping from visible identifiers to internal IDs
   - keep duplicate handling explicit (`skip`, `merge`, `split`, `manual`)
   - preserve program/level hints only when confidently inferred

4. Run bounded imports.
   - use narrow test slices before full-batch imports
   - capture rejected rows and unresolved mappings
   - re-run targeted reconciliation on partial success

5. Reconcile and report.
   - compare import logs against expected counts
   - flag unresolved collisions and suspicious misses
   - keep reconciliation notes machine-readable when possible

## Preferred Routes

### Import parser stability

- Start by reading:
  - [parsing and normalization](references/parser-and-normalization.md)

- Default route:
  1. stabilize parser behavior on edge rows
  2. encode deterministic cleaning steps
  3. validate results against a known-good sample

### Course and curriculum resolution

- Start by reading:
  - [curriculum resolution rules](references/curriculum-resolution.md)

- Default route:
  1. split ambiguous matches early
  2. preserve duplicates as explicit states
  3. prefer explicit keys over fuzzy matches

### Batch import and reconciliation

- Start by reading:
  - [batch import process](references/batch-import-reliability.md)

- Default route:
  1. run in bounded windows
  2. verify rejects and duplicates before full re-run
  3. report unresolved items in a clean handoff format

## House Rules For This Host

- Do not silently coerce ambiguous IDs into existing records.
- Keep parser-specific logic isolated from business normalization rules.
- Keep import logic generic where possible so new curriculum structures can be supported.
- Keep logging compact and include deterministic identifiers.

## Deliverables

- parsing and normalization changes with rationale
- duplicate/conflict policy and resulting behavior
- batch result summary and unresolved item list

## References

- [parsing and normalization](references/parser-and-normalization.md)
- [curriculum resolution](references/curriculum-resolution.md)
- [batch import reliability](references/batch-import-reliability.md)
