---
name: tu-curriculum-transformation
description: Extract and normalize Tubman University curriculum documents from ODT, DOCX, or imported text into Org sources that export through tuclgcurri or tuunivcurri. Use when a task involves curriculum wrangling, ODT or DOCX cleanup, structure-preserving Org conversion, course-description macro formatting, radio tables, orgtbl/Emacs Lisp curriculum helpers, or batch Org to TeX to PDF export checks.
metadata:
  author: local-codex
  maturity: draft
---

# TU Curriculum Transformation

Use this skill when the user wants to turn raw curriculum source material into clean Org curriculum files that work with the TU curriculum classes and export chain.

This skill is for:
- ODT or DOCX curriculum extraction into Org
- cleanup of imported curriculum text without changing meaning
- normalization into a reusable TU curriculum grammar
- conversion of course descriptions into the TU curriculum macro form
- normalization of requirements, summary, minor, and semester tables
- radio-table and `orgtbl` workflows backed by Emacs Lisp helpers
- batch export checks for Org -> TeX -> PDF in the curriculum repo
- curriculum-relevant catalog assembly when the goal is still clean Org/TeX curriculum output

This skill is not for:
- generic DOCX round-tripping where TU curriculum structure does not matter
- policy manuals or standalone policy workflows
- scanned PDF OCR recovery
- arbitrary LaTeX class work outside the curriculum document families
- detailed course-catalog audit, deduplication, or reconciliation reports; use `tu-curriculum-audit`

## Workflow

1. Identify the authoritative content source.
   - Prefer the ODT content source when it exists.
   - Treat DOCX or PDF as secondary witnesses unless the ODT is missing.
   - Keep wording faithful; do not silently rewrite content during cleanup.

2. Inventory the document before editing.
   - Identify whether the target is a college curriculum or university-level curriculum.
   - Record headings, program groups, minors or emphasis areas, course-description regions, and table families.
   - Detect whether the source is structurally close to the current grammar or needs heavy wrangling first.

3. Normalize structure before styling.
   - Remove import noise first: false headings, empty headings, stray property drawers, broken emphasis markers, and obvious ODT residue.
   - Do not force the CAFS structure onto a new curriculum blindly.
   - Preserve structural variations when they are semantically meaningful, then map them into the closest TU grammar slot.

4. Convert stable curriculum content into TU macro form.
   - Use the curriculum classes as the target representation, not as an afterthought.
   - Prefer `\TUCurriCrsDescEntry...` forms for course descriptions.
   - Preserve visible course codes exactly as written in the source.
   - When duplicate visible codes need unique links, disambiguate only the internal target key.

5. Normalize tables into the house families.
   - Requirements tables -> 2-column
   - Course-list or summary tables -> 3-column when appropriate
   - Minor or emphasis program tables -> 4-column
   - Semester plans -> 6-column
   - Prefer class-owned environments and row macros once a layout is stable.

6. Use radio tables and Emacs Lisp helpers deliberately.
   - Keep table emitters compatible with the shared `orgtbl_curri_helpers.el` workflow when possible.
   - Be comfortable using or updating Emacs Lisp `orgtbl` helper functions.
   - When radio tables are used, keep the source organization and noexport helper sections readable and reproducible.

7. Verify through the real export chain.
   - Interactive Emacs export is the reference workflow.
   - Batch export is still valuable and should be checked, especially after helper or class changes.
   - Compile the exported TeX with `lualatex` twice and inspect the PDF output and log.

8. Escalate audit-heavy work to the audit skill.
   - If the task is mainly comparing course tables against descriptions, generating TSVs, deduplicating aliases, or rebuilding gcode mappings, use `tu-curriculum-audit`.
   - Bring only the final reconciled decisions back into the curriculum Org source.

## Preferred Route

### Source ingestion and cleanup

- Start by reading:
  - [source ingestion](references/source-ingestion.md)
  - [curriculum grammar](references/curriculum-grammar.md)

- Default route:
  1. identify the authoritative source
  2. classify structure and difficulty
  3. clean import noise without changing meaning
  4. normalize the heading grammar
  5. move into TU macro and table forms only after the structure is stable

### Course descriptions

- Start by reading:
  - [course descriptions](references/course-descriptions.md)

- Default route:
  1. locate the true course-description region
  2. group entries by department or stable source grouping
  3. convert each description to the curriculum macro form
  4. preserve visible source inconsistencies while recording duplicate or ambiguous cases

### Radio tables and batch export

- Start by reading:
  - [tables and batch export](references/tables-and-batch-export.md)

- Default route:
  1. choose the correct table family
  2. decide whether a radio-table workflow is justified
  3. emit through shared helpers when possible
  4. verify both structure and export behavior

### Catalog and manual production

- Start by reading:
  - [catalog production](references/catalog-production.md)

- Default route:
  1. keep curriculum Org as the structural source
  2. import external DOCX/ODT material only into the appropriate Org sections
  3. use ODT/DOCX/PDF outputs as validation witnesses, not as the canonical source
  4. move course reconciliation into `tu-curriculum-audit` when it becomes the main task

## Local Sources To Respect

Prefer these local sources when they exist:
- `/mnt/backup/Jobs/TU/Academics/Curriculum/AGENTS.md`
- `/mnt/backup/Jobs/TU/Academics/Curriculum/README.org`
- `/mnt/backup/Jobs/TU/Academics/Curriculum/tuclgcurri.cls`
- `/mnt/backup/Jobs/TU/Academics/Curriculum/tuunivcurri.cls`
- `/mnt/backup/Jobs/TU/Academics/Curriculum/orgtbl_curri_helpers.el`
- `Archives/ContentSource/*.odt`

## House Rules For This Host

- Preserve wording from the source unless there is an obvious import artifact or obvious spelling break.
- If the wording is in doubt, check the ODT source before changing it.
- Treat Org as the working structural source and exported TeX as a build artifact.
- Be comfortable with raw LaTeX lines, `src latex` blocks, `orgtbl` emitters, and shared Emacs Lisp helpers.
- Support different curriculum structures across colleges; discover the grammar before normalizing.
- Keep reusable structural decisions in repo notes when working in the real curriculum repository.

## Deliverables

When using this skill, the output should usually include:
- a cleaned Org curriculum source
- normalized macro-formatted course descriptions where appropriate
- normalized table structures or radio-table senders and receivers where appropriate
- a short note on preserved wording, inferred structure, and unresolved ambiguities
- a note when audit work was delegated to or should be handled by `tu-curriculum-audit`

## References

- [source ingestion](references/source-ingestion.md)
- [curriculum grammar](references/curriculum-grammar.md)
- [course descriptions](references/course-descriptions.md)
- [tables and batch export](references/tables-and-batch-export.md)
- [catalog production](references/catalog-production.md)
