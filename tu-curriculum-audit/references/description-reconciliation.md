# Description Reconciliation

Use this reference when comparing course-description entries against curriculum table facts.

## Description Facts

Extract course-description entries separately from curriculum tables.

Recommended fields:
- code
- title
- credits
- prerequisites when visible
- description text
- department or source grouping
- source heading or line

## Comparison Categories

Classify each issue explicitly:
- `missing-description`: table course has no description entry
- `missing-table-entry`: description entry does not appear in curriculum tables
- `credit-mismatch`: same course key with different credits
- `title-mismatch`: same course key with materially different title
- `duplicate-code`: visible code appears more than once with different facts
- `alias`: different visible strings likely refer to the same course
- `likely-rename`: old and new names appear related but need user confirmation

## Reporting

Separate raw evidence from recommendations.

Good reports include:
- counts by category
- representative examples
- source locations
- proposed action for each class of mismatch

Do not silently update Org from a reconciliation report unless the user explicitly asks for edits.
