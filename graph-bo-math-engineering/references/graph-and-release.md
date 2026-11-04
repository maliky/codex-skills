# Graph And Release

## Source And Saved State

The official BO PDFs and transcriptions under `data/bo/` are protected; local codes, editorial summaries, and relation proposals are separate. The three legacy transcriptions named in the repository `AGENTS.md` are models for structure, not files to update. Do not synchronise Élizé automatically. Read the current `README.org` and `DEV.org` before treating any editing or import idea as a delivered capability.

The graph editor and viewer use maintained TypeScript sources such as `graph-editor.ts`, `graph-core.ts`, and `progression.ts`. `site/`, `generated/`, and `web/graphe-prerequis.js` are generated. The server library stores immutable catalogues and graph revisions; the progression composer stores separate immutable drafts bound to exact catalogue and relation identities. A dirty or mismatched relation draft cannot silently become the source of a saved progression. Keep the free-layout composer separate from the calendar-based progression viewer.

For relation edits, verify the current graph's rules before changing them: no self-links or cycles, no unintended shortcuts through an existing indirect path, and atomic behavior for multi-selection. Save validation belongs on the server as well as in the browser. Preserve an unsaved draft after a network error and protect deliberate abandonment of that draft. Existing saved snapshots and their PDF assets must remain readable after later source changes.

## Browser And Publication

For menus, popovers, graph selection, drag, or zoom changes, exercise the actual mouse, keyboard, and touch paths relevant to the change. Check viewport bounds, Escape and outside-click closing, focus restoration, selection and filter retention, and the effect of panning or resizing. Use the focused browser test first, then the repository's build, check, unit, and browser suites.

Follow `deploy/publish.sh` and the current deployment notes only after explicit publication authorization. The persistent library and its immutable PDF assets live outside release directories; deployment must not replace them. Verify the remote commit, active release or manifest, API health and library access, and the changed public interaction. A successful local build alone is not publication proof.
