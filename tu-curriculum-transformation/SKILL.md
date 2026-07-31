---
name: tu-curriculum-transformation
description: "Use when extracting and normalizing Tubman University curriculum documents from ODT, DOCX, or imported text into Org sources that export through tuclgcurri or tuunivcurri, including structure-preserving cleanup, course-description macros, radio tables, orgtbl or Emacs Lisp helpers, and Org-to-TeX-to-PDF export checks."
---

# TU Curriculum Transformation

Turn raw curriculum material into maintained Org sources while preserving meaning, local vocabulary, and TU curriculum export contracts.

## Avoid When

- The task is mainly audit/reconciliation after sources exist; use `tu-curriculum-audit`.
- The task is generic document conversion; use `document-conversion`.
- The task is class-side LaTeX maintenance; use `tu-latex-classes`.
- The user asks not to compile or export.

## Workflow

1. Identify the source family and preserve the original witness.
2. Build a clean Org structure before polishing wording.
3. Normalize tables and course descriptions into the local TU curriculum macro style.
4. Keep generated TeX/PDF as build artifacts unless the user says otherwise.
5. Verify through the real export chain when export behavior matters.
6. Hand table-vs-description conflicts to `tu-curriculum-audit`.

## Scripts

Use the Emacs helper for batch curriculum exports when the source is ready:

```bash
emacs --batch --quick --load scripts/export_org_curriculum.el -- SOURCE.org
```

Interactive Emacs export remains the reference behavior when local configuration matters.

## Routes

- **Source ingestion**: read [source ingestion](references/source-ingestion.md).
- **Target grammar**: read [curriculum grammar](references/curriculum-grammar.md).
- **Course descriptions**: read [course descriptions](references/course-descriptions.md).
- **Tables and exports**: read [tables and batch export](references/tables-and-batch-export.md).
- **Catalog/manual work**: read [catalog production](references/catalog-production.md).

## Output Expectations

Return maintained Org source paths, normalized macro/table changes, export validation notes, and unresolved audit questions that should be handled separately.
