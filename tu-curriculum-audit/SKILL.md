---
name: tu-curriculum-audit
description: Audit and reconcile Tubman University curriculum/course catalog data from Org, DOCX/ODT-derived text, tables, spreadsheets, and course-description sections. Use when a task asks to extract course codes, titles, credits, prerequisites, corequisites, semester or level hints, or program labels; compare curriculum tables against descriptions; detect duplicates, aliases, credit mismatches, renamed courses, or missing entries; generate TSV audit files; merge spreadsheet or extracted-text witnesses; or plan safe course-key/gcode regeneration for TU curricula.
metadata:
  author: local-codex
  maturity: draft
---

# TU Curriculum Audit

Use this skill when the task is primarily about verifying, reconciling, or reporting course catalog data inside TU curriculum material.

This skill is for:
- extracting course codes, titles, credits, and descriptions from Org or imported text
- parsing 3-column course lists and 6-column semester tables
- comparing table courses against course-description entries
- finding duplicate visible codes, aliases, title variants, credit mismatches, and missing descriptions
- generating TSV or plain-text audit reports
- reconciling TSV, ODS, or other extracted witnesses against maintained audit tables
- filling or flagging prerequisites and corequisites during deterministic merges
- planning safe course-key, alias, or gcode regeneration

This skill is not for:
- first-pass curriculum source cleanup; use `tu-curriculum-transformation`
- generic document conversion; use `document-conversion`
- policy formatting or policy manuals
- changing source content silently to make audits pass

## Workflow

1. Establish the audit target.
   - Identify the maintained Org source or imported text file.
   - Determine whether the audit is table-only, description-only, or table-vs-description.
   - Record whether outputs should be reports, patches, or both.

2. Extract facts before changing files.
   - Pull course code, title, credits, semester/year position, program hints, and source section.
   - Preserve visible source strings exactly in the first extraction.
   - Keep generated normalized keys separate from visible codes.
   - Distinguish source families early: descriptions, 3-column tables, 6-column tables, and spreadsheet witnesses.

3. Normalize only for comparison.
   - Normalize whitespace, punctuation, and obvious code separators in comparison keys.
   - Do not rewrite the visible course title or code unless the user asks for a correction pass.
   - Keep aliases explicit when one visible course maps to several internal keys.

4. Reconcile tables and descriptions.
   - Compare course tables against course-description entries.
   - Classify mismatches as missing description, missing table entry, credit mismatch, title mismatch, duplicate code, alias, or likely rename.
   - Prefer reports over automatic edits until the conflict is understood.

5. Reconcile audit witnesses.
   - Use deterministic joins before considering AI guesses.
   - Prefer exact joins on college, code, and cleaned title.
   - Fill empty prerequisite or corequisite fields without overwriting non-empty target values.
   - Flag credit disagreements instead of silently choosing one side.

6. Generate reviewable outputs.
   - Use TSV for machine-readable audit artifacts.
   - Include enough columns to trace each row back to source section and line or heading.
   - Keep final recommendations separate from raw extracted facts.

7. Patch only after the audit is stable.
   - Apply source edits in the maintained Org file, not generated TeX.
   - Regenerate course keys or gcodes only from an explicit mapping plan.
   - Re-run the extraction after edits and compare before/after counts.

## Preferred Routes

### Table extraction

- Start by reading:
  - [course extraction](references/course-extraction.md)

- Default route:
  1. identify table family: 3-column list or 6-column semester plan
  2. extract raw rows with source location
  3. split left and right semester halves in 6-column tables
  4. infer semester and level only from nearby deterministic context when possible
  5. normalize comparison keys
  6. write or summarize TSV output

### Extracted-text witness handling

- Start by reading:
  - [course reference extraction](references/course-reference-extraction.md)

- Default route:
  1. use this route only when the needed facts are not available cleanly from Org, tables, or spreadsheets
  2. strip or collapse markup into a deterministic text view when needed
  3. treat 3-column and 6-column table witnesses differently
  4. extract wide course-code candidates first, then clean false positives
  5. carry forward program, year, and semester hints from nearby headings or prior 6-column context
  6. leave unresolved program or level fields blank rather than inventing them

### Description reconciliation

- Start by reading:
  - [description reconciliation](references/description-reconciliation.md)

- Default route:
  1. extract description entries as raw facts
  2. compare against table extraction
  3. classify mismatches
  4. propose safe edits or alias mappings

### Gcode and alias regeneration

- Start by reading:
  - [gcode and aliases](references/gcode-and-aliases.md)

- Default route:
  1. freeze the visible course strings
  2. build an explicit old-key -> new-key mapping
  3. detect collisions before editing
  4. regenerate only after the mapping is reviewable

### Spreadsheet reconciliation

- Start by reading:
  - [spreadsheet reconciliation](references/spreadsheet-reconciliation.md)

- Default route:
  1. load extracted and original ODS or TSV witnesses as separate tables
  2. clean titles and code formatting before joins
  3. left join on college, code, and cleaned title unless the task explicitly wants a wider join
  4. append missing prerequisite or corequisite information without crushing non-empty values
  5. save merged outputs with flags for credit disagreements and unresolved joins

## House Rules For This Host

- Org is the maintained source once it exists.
- Table facts and course-description facts are separate witnesses until reconciled.
- Preserve source wording in raw audit outputs.
- Failed one-liners or abandoned extraction attempts should be suppressed; keep only final reusable patterns.
- Use deterministic shell, Perl, Python, or Emacs Lisp helpers where they make the audit reproducible.
- Use AI only as a bounded fallback for program or level guesses; do not let it override deterministic extraction when the local context is sufficient.

## Deliverables

When using this skill, the output should usually include:
- the source files or sections audited
- raw extraction counts by table or section
- mismatch categories and representative examples
- TSV paths or report paths when files are generated
- explicit assumptions for aliases, duplicates, and generated keys

## References

- [course extraction](references/course-extraction.md)
- [course reference extraction](references/course-reference-extraction.md)
- [description reconciliation](references/description-reconciliation.md)
- [gcode and aliases](references/gcode-and-aliases.md)
- [spreadsheet reconciliation](references/spreadsheet-reconciliation.md)
