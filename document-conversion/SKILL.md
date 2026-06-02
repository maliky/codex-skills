---
name: document-conversion
description: "Use when converting between Org, LaTeX, DOCX, ODT, PDF, and plain text while preserving structure, document intent, house style, custom classes, tables, metadata, or recoverable layout evidence beyond a simple Pandoc pass."
---

# Document Conversion

Convert documents by preserving structure first, styling second, and raw text last. Prefer the maintained source when one exists, and use generated files as evidence rather than truth.

## When to Use

- Convert Org or LaTeX sources to DOCX, ODT, PDF, or cleaner text.
- Recover structure from DOCX, ODT, or PDF-backed sources.
- Preserve custom class behavior, metadata blocks, policy sections, curriculum tables, forms, and course descriptions.
- Diagnose conversion routes before committing to Pandoc, LibreOffice, TeX, or XML-level repair.

## Avoid When

- The task is trivial plain-text extraction.
- The task is mainly TU curriculum normalization; use `tu-curriculum-transformation`.
- The task is mainly TU class maintenance; use `tu-latex-classes`.
- The user only asks to compile an already-normalized LaTeX source.

## Workflow

1. Identify source, target, required fidelity, and whether a maintained source exists.
2. Inspect dependencies, custom classes, embedded assets, tables, comments, and generated outputs.
3. Choose the least lossy route: semantic export, office conversion, XML repair, or PDF-backed recovery.
4. Preserve source wording and structure unless the user asks for cleanup.
5. Verify the converted document against headings, tables, references, metadata, and obvious formatting constraints.

## Scripts

Use the inspection helper before a non-trivial conversion:

```bash
python3 scripts/inspect_document_stack.py SOURCE --target docx
python3 scripts/inspect_document_stack.py SOURCE --target pdf --json
```

The script inventories tools and source signals; it does not replace conversion judgment.

## Routes

- **Route choice**: read [conversion matrix](references/conversion-matrix.md) before selecting Pandoc, LibreOffice, TeX, XML, or PDF-backed recovery.
- **DOCX source**: read [docx ingestion](references/docx-ingestion.md) before flattening OOXML content.
- **Org/LaTeX source**: read [org and latex preservation](references/org-latex-preservation.md) before removing raw LaTeX or export blocks.

## Output Expectations

Return the converted artifact path, route used, skipped or unavailable tools, validation notes, and any source elements that could not be preserved safely.

## References

- [conversion matrix](references/conversion-matrix.md)
- [docx ingestion](references/docx-ingestion.md)
- [org and latex preservation](references/org-latex-preservation.md)
