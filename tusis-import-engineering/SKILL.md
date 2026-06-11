---
name: tusis-import-engineering
description: "Use when building or debugging TUSIS and Django import pipelines for curriculum, course, student, grade, schedule, SmartSchool truth rebuild, or legacy data reconciliation, including parser normalization, mapping resolution, duplicate handling, batch reliability, CurriculumCourse or Section reconciliation, and import-output validation."
---

# TUSIS Import Engineering

Keep import work traceable from source rows through normalized parser output, mapping resolution, database writes, and batch validation.

## When to Use

- Build or debug repeated TUSIS/Django import pipelines.
- Normalize messy curriculum, course, student, grade, schedule, or section data.
- Resolve mappings to existing courses, curricula, departments, or sections.
- Investigate duplicates, failed joins, or batch import reliability.
- Validate importer results against source spreadsheets or cleaned witnesses.

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

## References

- [parser and normalization](references/parser-and-normalization.md)
- [curriculum resolution](references/curriculum-resolution.md)
- [batch import reliability](references/batch-import-reliability.md)
- [truth rebuilds](references/truth-rebuilds.md)
