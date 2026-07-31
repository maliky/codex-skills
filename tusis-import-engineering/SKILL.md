---
name: tusis-import-engineering
description: "Use for TUSIS/Django import pipelines: SmartSchool truth rebuilds, curriculum/course/student/grade/schedule imports, normalization, mapping, duplicates, and validation."
---

# TUSIS Import Engineering

Keep import work traceable from source rows through normalized parser output, mapping resolution, database writes, and batch validation.

## Avoid When

- The task is a one-off spreadsheet cleanup with no import pipeline implication.
- The task is curriculum text transformation; use `tu-curriculum-transformation`.
- The task is catalog audit before import design; use `tu-curriculum-audit`.
- The user asks for frontend/static review rather than import logic.

## Workflow

1. Locate the active Django checkout, models, importer, and source fixture.
2. Preserve raw source rows and make normalization explicit.
3. Resolve mappings deterministically before using fuzzy or inferred matches.
4. Run small bounded batches before large imports.
5. Validate counts, duplicates, unresolved rows, and database side effects.
6. Keep environment-specific conclusions scoped to the environment tested.

## Routes

- **Parser shape**: read [parser and normalization](references/parser-and-normalization.md).
- **Mapping resolution**: read [curriculum resolution](references/curriculum-resolution.md).
- **Batch safety**: read [batch import reliability](references/batch-import-reliability.md).
- **Truth rebuilds**: read [truth rebuilds](references/truth-rebuilds.md).

## Output Expectations

Report source files, parser/mapping changes, rows imported or skipped, duplicate/unresolved categories, validation commands, and environment assumptions.
