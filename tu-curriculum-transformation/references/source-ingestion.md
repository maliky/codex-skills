# Source Ingestion

Use this reference when turning raw ODT, DOCX, or imported curriculum text into a clean Org working source.

## Goal

Turn raw curriculum source material into a clean Org working file without changing the document's meaning.

## Authoritative source order

1. ODT in `Archives/ContentSource/`
2. DOCX or other editable office export when ODT is missing
3. Existing Org file if it is already the maintained working source
4. PDF only as a witness for layout or missing joins

When ODT exists, it is the wording reference.

## Preflight

Before editing a newly imported curriculum:

1. Identify the export family.
   - `tuclgcurri` for college curricula
   - `tuunivcurri` for university-level curricula

2. Classify the file.
   - relatively clean
   - moderate import noise
   - heavy import noise

3. Inventory:
   - heading levels
   - false or blank headings
   - property drawers
   - table types and noisy spacer columns
   - course-description markers
   - visible terms for minors, emphasis areas, or specialization tracks

## Cleanup order

Do structural cleanup before table redesign.

Typical early cleanup:
- remove imported property drawers unless they are intentional
- remove blank headings and headings that are only markup residue
- demote narrative sentences that were accidentally promoted to headings
- remove leftover ODT emphasis artifacts such as raw `*...*` and `/.../`
- remove empty quote blocks and stray marker lines
- join obviously broken line wraps into normal prose

## Content-preservation rule

Do not rewrite content during cleanup except for:
- obvious spelling mistakes
- obvious punctuation breakage caused by import
- obvious line-break artifacts

If the source is internally contradictory, stop at the safest cleaned state and record the ambiguity.

## Portability rule

Do not assume the next curriculum matches the CAFS prototype exactly.

Before applying a known pattern, verify:
- whether the same heading families exist
- whether minors vs emphasis areas differ in visible terminology
- whether tables map cleanly to the same family
- whether course descriptions are grouped the same way
