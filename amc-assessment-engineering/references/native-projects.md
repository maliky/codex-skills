# Native AMC Projects

## Locate the Authored Surface

- Inspect `options.xml` for the configured TeX source and follow its includes. An existing `source.tex` may import shared questions; do not assume the PDF basename identifies the editable file.
- In Elize, look for `<level>/Evals/README.org`, class AMC directories such as `211-amc/`, and the repository's `latex/` classes/styles. Verify the current layout; it is in transition from shared `items.tex` wrappers toward native AMC authoring.
- Reuse the user's actual archive macros/classes where compatible with the requested task. The latest assessment direction excludes the academy logo; do not reintroduce it from an older DS template.
- Keep hand-edited project entrypoints and settings intact during export. Generate missing scaffold files only when that is part of the requested project setup; do not overwrite existing options to enforce script defaults.

## Questions and Scoring

- Preserve stable, unique question identifiers, especially after distribution or scanning. Check shared and class-specific sources so a change intended for one class does not alter another unnoticed.
- Inspect open-answer and multiple-choice scoring through the actual macro definitions and AMC-generated scoring data. Check correct, incorrect, blank, multiple-selected, and partial-credit cases where supported; never infer scoring solely from printed point labels.
- Confirm the requested assessment total from current metadata. Existing IS/DS defaults are not universal scoring requirements.
- Allocate enough answer space for justifications and inspect the compiled subject and correction. Maintain smooth Asymptote curves where requested, with readable axes and consistent class variants.
- Keep teacher scoring areas distinct from student response areas using the existing house labels and layout. Prefer targeted changes to the shared class/style for repeated formatting issues.

## Comparable Elize Variants

- When copying an assessment between classes, preserve the requested difficulty, question structure, printed numbering, and point total. Vary numerical data only as requested and recompute the correction from the new data. For cross-tables, verify all row/column totals, complements, and the denominators of conditional proportions with exact arithmetic; keep any user-fixed totals.
- Inspect the current Elize project instructions and style before importing archive formatting. Preserve Elize geometry and per-question scores; do not add scores to section titles or replace printed `Question 1/2...` labels without a request. Use the project's `\unit` convention for quantities and percentages where specified.
- For the Elize `Réservé` grids that omit a printed zero, retain positive credit tiers and verify that an unselected grid scores zero. A legacy test selecting a removed choice must be updated to match the real grid; only test multiple selections when more than one choice exists. Do not restore a zero box to satisfy an obsolete fixture.
- When using the shared `elize@openlines` customization, check `lines=0` separately from positive line counts. Source-level arithmetic checks and a PDF compiled from an older dataset do not establish that the current subject/correction renders correctly. Report previews or compilation as unverified when the user declines those checks.

## Validation and Existing Exam Data

- Read the current help and implementation of existing tools such as `scripts/export-evaluations.py`, `scripts/validate-amc.py`, and `scripts/test-amc-scoring.pl` before execution. Some validation commands invoke AMC preparation and write project data; they are not read-only diagnostics.
- Exercise source compilation and relevant scoring checks in a fresh or isolated test project when existing copies, scans, or marking data could be affected. Use synthetic candidates for fixtures.
- Never replace or merge live AMC databases, scans, copy identifiers, or associations as a side effect of a layout change. For a requested change to an exam already in use, preserve a recoverable project copy and establish which existing copies must remain valid.
- Keep roster CSVs, nominated copies, marks, and associations private. Do not import nearby class lists automatically; compile anonymous copies unless nominated output is part of the request.
- Respect user limits on compilation or additional testing and state the resulting verification boundary. PDF compilation alone does not validate AMC association or scoring.
