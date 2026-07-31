---
name: tu-curriculum-audit
description: "Use when auditing or reconciling Tubman University curriculum and course-catalog data from Org, DOCX or ODT text, tables, spreadsheets, or descriptions, including program inventories, deduplicated offerings by college, course-code extraction, credits, prerequisites, aliases, duplicates, mismatches, TSV witnesses, and gcode or course-key regeneration plans."
---

# TU Curriculum Audit

Extract facts before editing sources. Keep visible course strings separate from normalized comparison keys, and prefer reviewable TSV/report outputs before source patches.

## Avoid When

- The task is first-pass curriculum source cleanup; use `tu-curriculum-transformation`.
- The task is generic conversion; use `document-conversion`.
- The user expects silent source edits before an audit is stable.

## Workflow

1. Identify the maintained source and audit type: table-only, description-only, table-vs-description, or witness merge.
2. Extract raw facts with source location and preserve visible strings.
3. Normalize only for comparison; keep aliases and generated keys explicit.
4. Classify mismatches before recommending edits.
5. Produce TSV or report artifacts with traceable rows.
6. Patch maintained Org only after the audit is stable and the user accepts the mapping.

## Scripts

Use the course-reference extractor for a first deterministic pass:

```bash
python3 scripts/extract_course_refs.py SOURCE --tsv course_refs.tsv
python3 scripts/extract_course_refs.py SOURCE
```

The script extracts candidate course references. It does not decide aliases, credits, or curriculum correctness.

## Routes

- **Table extraction**: read [course extraction](references/course-extraction.md).
- **Program inventory**: read [program inventory](references/program-inventory.md).
- **Collapsed text/XML witnesses**: read [course reference extraction](references/course-reference-extraction.md).
- **Description reconciliation**: read [description reconciliation](references/description-reconciliation.md).
- **Gcode and aliases**: read [gcode and aliases](references/gcode-and-aliases.md).
- **Spreadsheet reconciliation**: read [spreadsheet reconciliation](references/spreadsheet-reconciliation.md).

## Output Expectations

Report source sections audited, extraction counts, mismatch categories, TSV/report paths, and explicit assumptions for aliases, duplicates, and generated keys.
