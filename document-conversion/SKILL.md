---
name: document-conversion
description: Convert between Org, LaTeX, DOCX, and PDF while preserving structure and formatting intent. Use when a task involves org/tex to docx, docx to org/latex, Pandoc-like conversion with better fidelity, LaTeX class/style support, PDF-backed recovery, or round-tripping academic/policy/curriculum documents.
metadata:
  author: local-codex
  maturity: draft
---

# Document Conversion

Use this skill when the user wants higher-fidelity document conversion than plain Pandoc usually gives, especially where structure and house style matter more than raw text extraction.

This skill is designed for the local Codex host at `/home/mlk/.codex/skills`. It works best when `pandoc`, `soffice` or `libreoffice`, `unzip`, `zip`, `mutool`, `pdfinfo`, and a TeX engine such as `lualatex` or `pdflatex` are available. Network access is not required.

This skill is for:
- Org or LaTeX source that must become DOCX
- DOCX that must become Org or LaTeX
- documents that rely on local =.cls= or =.sty= files
- PDF files used as reference, fallback source, or formatting truth
- round-trips where semantic structure must be preserved

This skill is not for:
- trivial plain-text conversion where structure does not matter
- OCR-heavy scanned PDF recovery without a reliable text layer
- one-line format swaps that standard Pandoc can handle without custom inspection

## Workflow

1. Identify the authoritative source.
   - Prefer editable source over rendered output.
   - If both source and PDF exist, treat the PDF as formatting truth and the source as semantic truth.

2. Inventory dependencies before converting.
   - Look for =#+LATEX_CLASS=, =#+LATEX_HEADER=, =\documentclass=, =\usepackage=, local =.cls=, local =.sty=, included PDFs, and referenced assets.
   - If the source depends on a custom class, inspect that class before deciding the conversion route.

3. Choose the least-lossy path.
   - For Org/TeX -> DOCX, prefer semantic export first and style recovery second.
   - For DOCX -> Org/LaTeX, inspect Word styles and numbering before flattening the document.
   - For PDF-backed conversions, use PDF only to recover layout or verify missing structure; do not invent semantic hierarchy without evidence.

4. Preserve structure explicitly.
   - Keep headings, named blocks, lists, tables, captions, notes, appendices, metadata, and cross-reference intent.
   - Do not silently collapse custom block structure into plain paragraphs if the original distinguishes policy blocks, procedures, course descriptions, forms, or metadata tables.

5. Log fidelity gaps.
   - State what was preserved, approximated, downgraded, or left unresolved.
   - Separate verified structure from inferred structure.

## Preferred Routes

### Org or TeX to DOCX

- Start by reading:
  - [conversion matrix](references/conversion-matrix.md)
  - [Org/LaTeX preservation notes](references/org-latex-preservation.md)

- Default route:
  1. inspect Org front matter or LaTeX preamble
  2. identify custom classes, packages, and macros
  3. normalize source only if needed to expose semantics cleanly
  4. use Pandoc for the base conversion
  5. use DOCX reference styling or post-process with LibreOffice when house style matters

- If the LaTeX document uses institution-specific =.cls= or =.sty=:
  - do not assume Pandoc understands those semantics
  - map custom structures to DOCX-visible constructs explicitly
  - preserve administrative metadata as tables or labeled blocks rather than raw macro dumps

### DOCX to Org or LaTeX

- Start by reading:
  - [DOCX ingestion notes](references/docx-ingestion.md)
  - [conversion matrix](references/conversion-matrix.md)

- Default route:
  1. inspect style usage, numbering, tables, footnotes, headers, and section breaks
  2. unzip the DOCX when style behavior is unclear
  3. map Word styles to Org headings and LaTeX structures
  4. move repeated formatting into class/header conventions if the target workflow uses them
  5. keep content faithful; avoid “cleanup” that changes meaning

- For policy, curriculum, or form documents:
  - preserve named blocks and control metadata
  - preserve table semantics even if exact layout changes
  - keep unresolved ambiguities in comments rather than guessing

### PDF-Assisted Conversion

- Use PDF as:
  - formatting witness
  - fallback source for lost layout
  - verification target against regenerated outputs

- Do not use PDF as the only semantic source if editable source exists.
- If text extraction is weak, report limits instead of fabricating structure.

## Local Tooling

Prefer these local tools when available:
- =pandoc=
- =soffice= or =libreoffice=
- =unzip= and =zip=
- =pdfinfo=
- =mutool=
- =lualatex=, =pdflatex=, or =xelatex=

Use scripts later if the workflow becomes repetitive. For now this skill is instruction-led.

## House Rules For This Host

- Respect local LaTeX class and style files. They are part of the document model, not decoration.
- When working with Org export pipelines, check whether raw LaTeX is embedded via native lines, export blocks, or source blocks used as raw emitters in the local workflow.
- For curriculum and policy work, preserve structure first and typography second.
- If PDF and source disagree, say so explicitly.

## Deliverables

When using this skill, the output should usually include:
- converted target document
- any required companion class/header adjustments
- a short fidelity note listing preserved structure and unresolved losses

## References

- [conversion matrix](references/conversion-matrix.md)
- [Org/LaTeX preservation notes](references/org-latex-preservation.md)
- [DOCX ingestion notes](references/docx-ingestion.md)
