# Tables And Batch Export

## Table strategy

Use class-owned table structures and row macros where possible.

Stable table families in this workflow:
- 2-column requirements tables
- 3-column summary or course-list tables
- 4-column minor or emphasis tables
- 6-column semester tables

When a table layout is stable, prefer class environments and row macros over raw `tabularx` boilerplate in the Org file.

## Radio tables

Use radio tables when:
- the source Org table should remain readable
- the emitted LaTeX structure is repetitive
- the same family of tables will recur across colleges

When radio tables are used:
- keep senders readable in the document
- keep helper code under a `:noexport:` tree or in the shared helper file when appropriate
- use anchors to control placement for non-floating curriculum tables
- keep the mapping between sender location and receiver tree clear

## Shared helper workflow

The reference helper source is usually:
- `orgtbl_curri_helpers.el` in the TU curriculum repository root

Be comfortable with:
- `orgtbl` formatter functions
- Emacs Lisp emitters for each table family
- shared helper reuse across colleges
- batch-vs-interactive export differences

## Batch export chain

Reference workflow:
1. edit the Org source
2. refresh radio-table receivers or helper-driven output
3. export from Emacs
4. compile the exported TeX in `Export/` with `lualatex`
5. compile a second time so TOC, links, and `LastPage` settle

Interactive Emacs export is the reference behavior.

Batch checks are still important when:
- helper code changed
- class code changed
- radio tables were refactored
- the file is intended to export unattended later

## Practical validation

After table or helper changes:
- confirm the exported TeX uses the expected class environment
- inspect the PDF for overprint, truncation, and misplaced totals
- check that title columns wrap correctly
- keep the numeric cells clean
- move qualifications or notes out of overloaded `Cr` cells and into table notes
