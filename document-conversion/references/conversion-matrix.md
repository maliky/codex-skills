# Conversion Matrix

## Primary goals

- preserve semantic structure
- preserve authoring workflow
- preserve class/style intent where possible
- avoid irreversible flattening unless the user explicitly asks for it

## Recommended paths

### Org -> DOCX

- Best when:
  - the Org file has consistent heading structure
  - raw LaTeX is limited or can be mapped
  - tables are semantic rather than visual hacks

- Default tools:
  - pandoc
  - optional DOCX reference document
  - optional LibreOffice post-pass

- Risk points:
  - raw LaTeX blocks
  - custom macros
  - complex tables
  - PDF inclusions

### TeX -> DOCX

- Best when:
  - the TeX file is structurally simple
  - class-specific macros can be mapped or stripped safely

- Default tools:
  - pandoc for baseline conversion
  - manual mapping for metadata macros
  - LibreOffice for style cleanup if needed

- Risk points:
  - class-defined macros
  - package-dependent environments
  - PDF-only inclusions
  - cross-reference systems

### DOCX -> Org

- Best when:
  - Word styles are used consistently
  - numbering and headings are style-driven rather than manually formatted

- Default tools:
  - pandoc
  - unzip + XML inspection when needed

- Risk points:
  - direct formatting instead of named styles
  - nested tables
  - floating objects
  - ambiguous heading hierarchy

### DOCX -> LaTeX

- Best when:
  - the goal is a readable editing source, not perfect visual parity

- Default tools:
  - pandoc for first pass
  - manual refactor into class-based structure

- Risk points:
  - hardcoded Word layout
  - forms
  - page furniture
  - tracked changes

### PDF -> Org or LaTeX

- Best when:
  - the PDF has a reliable text layer
  - the goal is recovery or verification, not exact round-trip editing

- Default tools:
  - mutool
  - pdfinfo
  - manual semantic reconstruction

- Risk points:
  - scanned PDFs
  - broken reading order
  - table extraction
  - lost heading semantics

## Decision rule

Use the source with the richest semantics as the base.

Use rendered outputs only to:
- verify layout
- recover missing structure
- arbitrate export regressions
