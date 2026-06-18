# Truth Rebuilds And SmartSchool Imports

Use this reference when TUSIS work rebuilds or reconciles a current source of truth from SmartSchool exports, curriculum sources, grade sheets, or mixed legacy data.

## Source Priority

- Treat the latest explicit SmartSchool export folder as the current operational source when the user identifies it as latest, such as `SmartSchoolDB_20260609`.
- Preserve raw source rows and paths in logs or witness files before normalizing names, courses, grades, or curriculum links.
- Use older spreadsheets and legacy current-student grade sheets as witnesses unless the user explicitly promotes them to source of truth.
- When `tucurricula` is mentioned for descriptions or prerequisites, treat it as a curriculum witness feeding course enrichment, not automatically as the whole database source of truth.
- Keep current-semester facts explicit. Recent operational work used vacation school semester 3 of academic year 2025-2026 as the active registration context.

## Rebuild Procedure

1. Identify the reset or import runbook, active database, source folder, and importer commands before changing data.
2. Back up or preserve student, registration, and grade data when the rebuild may replace academic structures.
3. Run bounded imports first; increase batch size only after reject categories and duplicate rates are stable.
4. Validate row counts for courses, curricula, curriculum courses, students, registrations, and grades after each major phase.
5. Keep import errors reproducible: record source file, row number, normalized key, exception class, and whether the transaction was aborted.
- After rebuilding courses and curricula, verify that course descriptions and prerequisites/correquisites are populated where a trusted TU curriculum source provides them.
- If registered credits are lower than credits with passing grades, reconstruct plausible historical registration rows from grade evidence. Perfection is not the goal; completeness and traceable inference are.

## Course And Alias Collisions

- Prefer exact course-code and normalized-title matches before fuzzy matching.
- Record known duplicates or renames as aliases instead of creating parallel courses when evidence shows they are the same course.
- Make collisions visible for review; examples from recent work include history-course title/code ambiguity and similar normalized titles across catalog revisions.
- Avoid one-off fixes inside data rows when a deterministic alias or mapping rule belongs in importer logic.
- Course-code parsing should tolerate three- or four-letter prefixes, three digits, and optional suffix letters, but must keep remedial or malformed rows reproducible when they exceed model field limits.
- College acronyms are operational data. Recent convention used CAS, CBA, EDRCE, CET, and CHS; update initialization scripts, code, docs, and DB rows together when those codes change.

## Transaction Failures

After a database error, assume the transaction may be aborted until explicitly rolled back or restarted. Isolate the failing row in a small batch, fix the mapping/parser issue, then rerun the bounded import before the full batch.
