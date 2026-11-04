# Sources, Imports And Calendar Progressions

Use for `graph-bo-math` source/data/interface work, not the older Elize `Graphe-prerequis/` output. Resolve the current checkout; known locations include `/mnt/backup/Jobs/Koba-informatique/graph-bo-math` and `/home/jil/graph-bo-math`. Read its `AGENTS.md` and `README.org` first. The app builds and runs independently of Elize; do not search or synchronize that other repository unless the task explicitly requires an import.

## Sources and Imports

- Edit maintained Org, TypeScript, HTML/CSS and authorized data sources. `site/`, `generated/` and `web/graphe-prerequis.js` are generated; rebuild rather than patching them.
- Official PDFs under `public/resources/bo/` and protected transcriptions under `data/bo/` remain verbatim, including unusual wording and faults. Preserve their hashes and distinguish official quotations, local summaries and proposed pedagogical prerequisite edges. Keep uncertain curated proposals explicit. Apply the current validation contract for each workflow: an editor's documented allowance for empty rationales does not establish evidence for a curated proposal.
- Imports are explicit, read-only with respect to Elize, and traceable by source paths and hashes. Inspect `tools/import_elize.py --help` before using `python3 tools/import_elize.py --root /actual/Elize`. For a progression-only refresh, use its `--progressions-only` option to avoid reimporting BO/resources. Review the resulting diff, provenance and protected-source hashes before accepting it.
- `data/progressions.json` is an autonomous snapshot. A weekly occurrence has its own `id` and a canonical `capacityId`; do not duplicate BO quotations or resources per occurrence. Unknown codes, repeated introductions, reprises before introduction and incomplete coverage block the import. Exclude private subtrees and assessment-only mentions, and do not invent capacities for a week with none specified.
- Keep programme quotation validation distinct from PDF text-similarity heuristics; inspect ambiguous original pages. Public resources must exclude private corrections, student data and administrative material. Retain local assets and vendored dependencies for offline use.

## Calendar Viewer

- Shared graph computations live in `graph-core.ts`; chronological projection/placement lives in `progression.ts`. BO and Progressions share capacity cards, resources and search, but retain their own selection/filter state. Inspect current behavior before changing cross-view interactions.
- Progression edges use mutually nearest chronological occurrences, not every possible pair. Same-week relations do not imply session ordering; hiding a sequence must not recompute the chronological pairs. Preserve occurrence-specific selection and navigation to later reprises.
- Browser checks should cover the changed behavior plus representative selection/Ctrl-click, group selection, reset, shared cards, filters, pinned-node stability, lens, mobile layout and local PDF links. Keep tests tied to current data rather than historical node/link/PDF counts.

For the separate editor and saved library, read [graph and release](graph-and-release.md). Host publication is covered by the [graph release workflow](../../koba-vps-webops/references/graph-bo-math.md).
