# Catalog Production

## Purpose

Use this reference when curriculum transformation work expands into TU catalog or manual production but the maintained source is still Org exported through the TU curriculum toolchain.

## Source Rules

- Treat the Org source as the maintained structural source once it exists.
- Use DOCX/ODT inputs as content witnesses for sections such as academic calendars, catalog parts, and narrative policies.
- Use PDF output as a visual/layout witness, not as the primary text source.
- Keep exported TeX, ODT, DOCX, and PDF as build products unless the user explicitly says otherwise.

## ODT/DOCX Robustness

- Prefer an ODT-first route when LibreOffice ToC or DOCX XML behavior is unstable.
- Inspect generated office XML only when the office output is wrong or corrupt.
- Keep table styles and fixed-width decisions consistent across repeated generated sections.
- Verify ToCs, annexes, title pages, chapter boundaries, and course indexes after conversion.

## Boundary With Audit Work

Move to `tu-curriculum-audit` when the main work is:
- extracting course catalogs from tables
- comparing course descriptions against table entries
- detecting duplicate or renamed courses
- generating audit TSVs or reconciliation reports
- rebuilding aliases or generated course keys

Bring only the resolved decisions back into the catalog Org source.
