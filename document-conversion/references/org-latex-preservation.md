# Org and LaTeX Preservation Notes

## What to preserve

- heading hierarchy
- named blocks such as policy statement, purpose, scope, definitions, metadata blocks
- list semantics
- table semantics
- captions and labels
- appendices and annexes
- explicit references to local classes and styles

## What to inspect early

- =#+LATEX_CLASS=
- =#+LATEX_CLASS_OPTIONS=
- =#+LATEX_HEADER=
- raw LaTeX lines
- export blocks
- source blocks that are intentionally used as raw LaTeX emitters in the local workflow
- =\documentclass=
- =\usepackage=
- =\input= and =\include=
- macro definitions that encode structure rather than styling

## Important warning

Custom =.cls= and =.sty= files often carry document semantics:
- metadata layout
- heading hierarchy
- named administrative blocks
- form field rendering
- running headers and footers

Do not treat them as purely cosmetic.

## Recommended practice

- preserve the semantic role of a macro even when the exact macro cannot survive in the target format
- convert metadata macros into explicit labeled content
- keep unresolved macro meaning in comments rather than dropping it silently

## Practical Note

Some local Org workflows intentionally use native LaTeX lines or blocks in ways that are valid in export even when they look unconventional. Inspect the actual export behavior before “cleaning up” those constructs.
