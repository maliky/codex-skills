---
name: amc-assessment-engineering
description: "Use when authoring or maintaining native Auto Multiple Choice assessments, AMC LaTeX questions and scoring, archive-derived classes/macros, editable AMC project settings, or AMC-source conversion to GIFT and other question-bank formats, especially in the Elize repository."
---

# AMC Assessment Engineering

Keep assessments directly editable and usable in Auto Multiple Choice. Follow the user's current choice of native AMC LaTeX as the authored question source, with other formats derived through an explicit conversion contract.

## Workflow

1. Locate the actual project entrypoint, `options.xml`, included question sources, classes/macros, figures, and existing scan/association data. Read repository instructions and determine which files are authored versus generated.
2. For Elize, inspect current evaluation READMEs and the relevant 2023 archive sources when recreating the user's style. Preserve archive originals; reuse their authoring conventions without importing old dates, rosters, marks, or institution branding.
3. Keep source and parameters accessible from AMC. Preserve manual edits to existing project entrypoints and options; avoid a generated abstraction that must replace the project's authored source on every build.
4. Validate question identifiers, answer semantics, point totals, subject/correction consistency, response space, figures, and rendered output. Protect the identity and scoring of already distributed/scanned copies.
5. Treat the Haskell conversion direction as a separate implementation boundary. Verify what the current code supports before claiming a parser, converter, or lossless round trip exists.

## Routes

- **Questions, archives, project settings, and scoring**: read [native projects](references/native-projects.md).
- **AMC source and Haskell/GIFT conversion**: read [conversion boundary](references/conversion-boundary.md).
- For Elize curriculum coverage, calendars, and lessons, use `elize-teaching-engineering`. Generic document conversion alone does not require this skill.

## Output Expectations

Identify the file the user should edit, the AMC project to open, supported compilation commands, checks actually run, and any unresolved scoring/conversion limitations. Distinguish PDF compilation from AMC preparation, scan analysis, association, and marking.
