---
name: graph-bo-math-engineering
description: "Maintain the standalone Graph BO Math prerequisite graph and progression editor in /home/jil/graph-bo-math, including protected BO catalogues, pedagogical relations, immutable graph and progression saves, browser interactions, and verified publication. Use elize-teaching-engineering for lessons and source progressions in Elize."
---

# Graph BO Math Engineering

Read the repository `AGENTS.md`, the relevant parts of `README.org` and `DEV.org`, and the maintained source for the requested change. The Graph BO Math application is autonomous: importing from Élizé is explicit, and a proposal in `DEV.org` is not proof of implemented behavior.

## Workflow

1. Check the active catalogue and graph identities, current release, Git state, and any unsaved relation draft before changing the editor or library.
2. Keep official BO citations and protected transcriptions separate from local capacity codes, summaries, and proposed prerequisite relations. Edit maintained TypeScript, HTML, CSS, Org, or server sources rather than generated site artifacts.
3. Preserve the distinction between a relation draft, an immutable saved graph, a free-layout progression draft, and the calendar-based progression viewer. Validate client behavior and server-side save invariants at the affected boundary.
4. Run `npm run build`, `npm run check`, `npm test`, and the relevant `npm run test:browser` interactions. Publish only when requested, then verify the active release and actual public behavior.

For protected sources, explicit imports and the calendar viewer, read [sources and imports](references/sources-and-imports.md). For graph editing, progression persistence and browser interaction, read [graph and release](references/graph-and-release.md). Use `elize-teaching-engineering` for edits to Élizé teaching sources and the [Koba graph release workflow](../koba-vps-webops/references/graph-bo-math.md) for host publication.

## Report

State which catalogue and relation snapshot the result uses, whether changes are only local or published, and which checks ran. Keep unresolved pedagogical choices and unverified deployment claims explicit.
