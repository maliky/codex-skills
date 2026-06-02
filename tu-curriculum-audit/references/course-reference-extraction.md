# Course Reference Extraction

## Purpose

Use this reference when the task is extracting course references from content XML, collapsed-span text, or table-heavy imports rather than only from clean Org or prose descriptions.

## Source Families

Handle these sources differently:
- 3-column tables: may contain course references, but not every row is a course row
- 6-column tables: usually encode semester I and semester II course references in left and right halves
- non-table collapsed XML text: useful for wide code scans and sanity checks
- nearby heading or paragraph text: useful for deterministic program, level, and semester hints

## Extraction Rules

- In 3-column tables, require the row to begin with a plausible course code before treating it as a course row.
- In 6-column tables, split each row into left and right 3-cell halves.
- If the code cell is blank in a 6-column half, allow carry-forward only when the surrounding rows clearly show the same repeated table structure.
- Do not treat rows such as `Total Minor`, `Year 1`, or similar structural labels as course titles.
- When XML tag collapse removes spaces, use a wide course-code regex and clean false positives afterward.

## Context Inference

- For 6-column tables, nearby text often gives the program name and the year or level; carry it across later tables until a new program marker appears.
- For 3-column tables, inspect only a short preceding window and leave fields blank if no stable context appears.
- Normalize level outputs to the house set when required by the task, but keep the literal source label available if it helps debugging.

## AI Boundary

- Keep AI disabled by default for this workflow.
- If AI is used, restrict it to guessing program or level when deterministic cues are absent.
- Record that AI was used in an explicit flag column.
