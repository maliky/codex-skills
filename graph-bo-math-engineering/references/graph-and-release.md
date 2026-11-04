# Graph And Release

## Source And Saved State

Read [sources and imports](sources-and-imports.md) when changing the catalogue or imported calendar progressions. The three legacy transcriptions named in the repository `AGENTS.md` are models for structure, not files to update. Read the current `README.org` and `DEV.org` before treating an editing idea as a delivered capability.

The graph editor and viewer use maintained TypeScript sources such as `graph-editor.ts`, `graph-core.ts`, and `progression.ts`. The server library stores immutable catalogues and graph revisions; the progression composer stores separate immutable drafts bound to exact catalogue and relation identities. When source relations change, save their graph copy first, then bind the progression to that identity. If the second save fails, preserve the draft and reuse the graph copy on retry. Keep the free-layout composer separate from the calendar-based progression viewer.

For relation edits, verify the current graph's rules before changing them: no self-links or cycles, no unintended shortcuts through an existing indirect path, and atomic behavior for multi-selection. Save validation belongs on the server as well as in the browser. Preserve an unsaved draft after a network error and protect deliberate abandonment of that draft. Existing saved snapshots and their PDF assets must remain readable after later source changes.

## Editor Routes And Recovery

`/edition/` leads to `/edition/graphe/` and `/edition/progression/`; `niveau` selects the level and `id` opens an archived copy with its catalogue. These editors target large screens. Retain appropriate mobile checks for the public viewer; a desktop editor task does not imply a new phone editor.

IndexedDB recovery copies belong to a document and tab and retain their source identities. Resuming creates a working copy; deleting a local draft must not remove an immutable library save. Preserve in-memory work and JSON export when local storage fails. Route changes, browser history and library opens must respect unsaved work.

Check async save and focus behaviour with the current implementation: closing a library modal or opening then cancelling another dialog during a save must not discard the successful response for the same document, leave an old URL, or leave the status stuck. Responses for a different document must not overwrite the active draft. Verify focus enters the editor, covered background controls are inactive, and focus returns on exit. These are regression scenarios from review, not a claim that the current code has already fixed them.

## Browser And Publication

For menus, popovers, graph selection, drag, or zoom changes, exercise the actual mouse, keyboard, and touch paths relevant to the change. Check viewport bounds, Escape and outside-click closing, focus restoration, selection and filter retention, and the effect of panning or resizing. Use the focused browser test first, then the repository's build, check, unit, and browser suites.

Use current lockfile/environment guidance; `CHROMIUM_PATH` can select an installed browser. Report blocked browser execution separately from passing unit tests. For requested publication, follow the [Koba graph release workflow](../../koba-vps-webops/references/graph-bo-math.md), preserving the persistent library and immutable PDF assets. Verify the remote revision, both active releases, API/library access and changed public interaction.
