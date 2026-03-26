# DOCX Ingestion Notes

## Inspect before flattening

When DOCX is the source, inspect:
- heading styles
- list numbering
- tables
- section breaks
- footnotes and endnotes
- headers and footers
- captions
- comments or tracked changes if present

## If Pandoc output looks wrong

Unzip the DOCX and inspect:
- =word/document.xml=
- =word/styles.xml=
- =word/numbering.xml=
- =word/footnotes.xml=
- =word/header*.xml=
- =word/footer*.xml=

This helps answer:
- whether a paragraph is really a heading
- whether numbering is style-driven
- whether tables encode metadata or merely layout
- whether visual emphasis is semantic or incidental

## Mapping guidance

- Word Heading 1/2/3 -> Org headline levels unless the document shows a different local convention
- labeled metadata rows -> explicit metadata block or labeled table
- visually repeated constructs -> candidate macro or helper in LaTeX

## Guardrails

- do not merge paragraphs because they “look related” unless the source confirms it
- do not invent heading levels when the DOCX uses manual bolding only
- if styles are inconsistent, preserve content and annotate the ambiguity
