---
name: elize-teaching-engineering
description: "Use when working in the Elize mathematics-teaching repository on protected French programme sources, capacity maps, spiral progressions, Qxx lessons, assessments, archive reuse, Org/LaTeX teaching templates, or validated teacher and student exports."
---

# Elize Teaching Engineering

Build traceable teaching material from official programmes and maintained Org sources. Keep source, pedagogical adaptation, and generated output distinct; validate both curriculum coverage and the rendered document when either matters.

## Avoid When

- The task is generic document conversion outside the Elize teaching workflow; use `document-conversion`.
- The task only maintains a TU class or curriculum; use the relevant `tu-*` skill.
- The task is only self-hosted Git synchronization; use `self-hosted-git-operations`.
- The user asks for a current regulatory fact but has not supplied the current source; verify it before treating a repository copy as current.

## Workflow

1. Resolve the real repository root, then read its current `AGENTS.md`, branch, worktree state, `.DEV.org`, `.dir-locals.el`, and the instructions nearest the requested files.
2. Classify every input as protected official source, read-only archive evidence, maintained Org, derived teaching material, confidential administration, or generated output before editing.
3. Select the actual level, class, group, and time window from current repository evidence such as `edt.org`; do not carry snapshot-specific rosters, dates, counts, or programme status forward from memory.
4. Derive progressions, lessons, exercises, and assessments through explicit programme-capacity links. Keep facts, archive observations, pedagogical choices, and unresolved questions distinguishable.
5. Edit the authoritative source: Org for lessons and progressions, maintained TeX where explicitly authored, and native AMC LaTeX for assessments under the user's current direction. Preserve semantic properties, local setup, and task comments. For an explicitly requested copied-TeX visual experiment, preserve the canonical source and identify the copy as a separate variant.
6. Run checks proportionate to the change: Org parsing, reference and capacity coverage, sequence or calendar invariants, export, compilation, PDF metadata, and representative visual inspection.
7. Preserve branch and project boundaries. Do not regenerate `Graphe-prerequis/`, migrate question banks, commit, push, or publish unless the user requested that exact action.

## Routes

- **Official programmes, capacity maps, and progressions**: read [programmes and progressions](references/programmes-and-progressions.md).
- **Archive reuse, Qxx lessons, and assessments**: read [lessons and assessments](references/lessons-and-assessments.md).
- **Shared manuals, class progress, hour selection, and export profiles**: read [sequence workflow](references/sequence-workflow.md).
- **Native AMC questions, scoring, and project maintenance**: use `amc-assessment-engineering`; retain this skill for programme alignment.
- **Org/LaTeX exports, repository boundaries, privacy, and Git**: read [exports and repository boundaries](references/exports-and-repository-boundaries.md).

## Output Expectations

Lead with the maintained source path and the teaching outcome. State which official or archived sources were used, confirm that protected sources were not modified, summarize curriculum-coverage and export/render checks, distinguish remaining uncertainty, and identify any commit, push, publication, or deployment deliberately left undone.
