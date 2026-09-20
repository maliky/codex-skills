# Rosters and gradebook imports

Resolve the class project's effective `options.xml` roster path and identity key before trusting associations. In Elize, maintained class lists have used `2de/203-list.csv`, `2de/211-list.csv`, and `1reST2S/1ST2S2-list.csv` with `id,nom,prenom,classe`; confirm current authority rather than adopting generated `_build/` copies or a general group list.

Compare CSV IDs with the project's actual association data, including `layout_association` when present. Inspect the current schema and supported AMC tools. Do not renumber historical IDs or replace associations to make a join appear to work. Resolve wrong-list paths before interpreting scores; route ambiguous identities to an anomaly report.

For an authorized grade import:

1. Make a dated recoverable backup of the destination. Identify exact class sheets, assessment columns, roster authority, and both scoring scales.
2. Match stable IDs where available; otherwise establish an unambiguous identity match. Report unmatched and duplicate candidates without guessing.
3. Preserve existing grades unless replacements are explicitly requested. Distinguish zero from an empty value. For the observed IS1 import the source was /10 and the destination /20, so scores were doubled; verify scales afresh for every assessment.
4. Preserve formulas, cell types, formatting, rows, and other sheets. ODS repeated rows/cells require structural handling, not blind text replacement. Use the existing validated import mechanism where available.
5. Compare changed cells with the expected import set and verify no unintended rows or values changed. Recalculate/check formulas with the office application when relevant; empty scores must not silently become zeros in averages. Keep unresolved numeric grades in a private anomaly report.

Keep rosters, association databases, scans, gradebooks, backups, and identity-bearing reports out of Git and public tool output. Report counts and validation results rather than student identities.
