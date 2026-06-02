# Spreadsheet Reconciliation

## Purpose

Use this reference when the task merges XML-derived curriculum facts with ODS or TSV audit tables.

## Preferred Inputs

Common witness pairs:
- XML-derived course definitions or course references
- original ODS or TSV extracted from content sources
- compiled or reconciled ODS tables used for manual review

## Cleaning Before Join

- Strip empty parentheses from XML-derived titles when they are only import residue.
- Trim titles and normalize repeated whitespace.
- Normalize obvious separators in prerequisite and corequisite fields before comparison.
- Preserve the original visible title in at least one column when the cleaned join key differs.

## Join Strategy

- Default join key: college, code, cleaned title
- Use a left join when enriching the target table from a more authoritative witness
- Widen the join only when the task explicitly asks for cross-college or code-only matching

## Merge Rules

- If prerequisite or corequisite is empty on the target side and present on the source side, fill it.
- If both sides are non-empty and differ, append the missing values instead of overwriting blindly.
- Flag credit disagreements explicitly.
- Keep rows that fail to join; unresolved rows are review items, not deletion candidates.

## Outputs

- Save a merged TSV or ODS with explicit status columns such as `credit_mismatch`, `title_matched`, or equivalent audit flags.
- Print counts for matched, unmatched, and flagged rows so the reconciliation can be reviewed quickly.
