---
name: tu-latex-classes
description: Use when maintaining Tubman University LaTeX class/style files (`.cls`/`.sty`) or fixing Org-to-LaTeX export regressions tied to TU class behavior.
metadata:
  author: local-codex
  maturity: draft
---

# TU LaTeX Classes

Use this skill when the request is to keep TU LaTeX class and style files production-safe while preserving house formatting constraints.

This skill is for:
- class-level changes in `tu*`, policy, curriculum, and form classes
- scoped debugging of export artifacts introduced by class-side changes
- class migration or fallback compatibility for older documents
- Org export contract checks tied to local `.cls` and `.sty` families

This skill is not for:
- general curriculum fact extraction
- full document conversion without class change intent
- unrelated codebase refactors that do not touch class behavior

## Workflow

1. Identify the active class family.
   - policy, memo, minutes, form, curriculum, or institutional support files.
   - keep edits in the minimal `.cls`/`.sty` family that owns the regression.

2. Inspect class dependencies.
   - check local package requirements
   - confirm command names and macro shape used by source Org
   - preserve naming used by existing export templates

3. Apply targeted class edits.
   - keep fixes local to that class until a shared change is confirmed
   - avoid broad style edits that are impossible to validate quickly
   - keep class-level comments and metadata coherent

4. Validate export chain.
   - run the local Org/TeX route that matches the document family
   - confirm headings, headers/footers, table blocks, and sectioning remain stable
   - keep iterative compilation artifacts out of source files

5. Update documentation paths if needed.
   - add short notes in local project docs or adjacent `.org` notes
   - include class version hints when needed for future rollback

## Preferred Routes

### Class inventory and ownership

- Start by reading:
  - [class inventory](references/class-inventory.md)

- Default route:
  1. confirm which class family owns the issue
  2. avoid editing unrelated classes for single-doc behavior
  3. apply minimal scoped edits and validate

### Export compatibility checks

- Start by reading:
  - [export compatibility](references/export-compatibility.md)

- Default route:
  1. run the real export route from source content
  2. inspect `.tex` output for macro breakage
  3. keep class defaults deterministic across versions

### Class refactors and cleanup

- Start by reading:
  - [class refactor patterns](references/class-refactor-patterns.md)

- Default route:
  1. isolate changed behavior to the class owning the regression
  2. keep old behavior stable unless intentionally breaking
  3. document fallback if old exports rely on legacy layout

## Operating Rules

- Prefer class-level fixes over post-export hacks.
- Keep document-specific overrides out of classes unless explicitly part of house policy.
- Treat `.cls` updates as interface changes; validate with actual source content.

## Deliverables

- scoped class files changed with rationale
- export validation artifacts or notes
- compatibility impact notes if class defaults were changed

## References

- [class inventory](references/class-inventory.md)
- [class refactor patterns](references/class-refactor-patterns.md)
- [export compatibility](references/export-compatibility.md)
