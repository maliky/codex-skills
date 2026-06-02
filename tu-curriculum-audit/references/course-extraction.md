# Course Extraction

Use this reference when extracting raw course facts from clean Org tables or maintained curriculum sources.

## Extraction Targets

Capture raw facts first:
- visible course code
- visible title
- visible credits
- table family
- program, year, semester, or heading context
- source file and line or nearest heading when available

## Table Families

Use these common TU curriculum table shapes:
- 3-column course list: code | title | credits
- 6-column semester plan: code | title | credits || code | title | credits

For 6-column tables, split each row into left and right course records. Empty halves should not produce records.

## Normalization

Normalize only comparison keys:
- trim whitespace
- collapse repeated spaces
- standardize obvious dash variants in keys
- normalize credits such as `3.0` to `3` for comparison

Keep visible strings unchanged in raw outputs.

## TSV Columns

Recommended minimum columns:
- `source`
- `section`
- `table_family`
- `year`
- `semester`
- `code`
- `title`
- `credits`
- `normalized_key`
- `notes`

Add project-specific columns only when the audit needs them.
