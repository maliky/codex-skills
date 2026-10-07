# Shared Sequence Workflow

Use for the current multi-level manuals, class calendars, hour/group selections, and preparation, projection, printing, or student exports. Inspect the current scripts and `.DEV.org` before reusing commands: this workflow has evolved rapidly.

## Authoritative Content and Progress

- Discover the maintained manual and calendar from current exporter configuration and repository instructions. Layouts have included `<level>/Q01/manuel.org`, `<level>/manuel.org`, and `<level>/manuel_<level>.org`; do not create or edit an old path from memory. Inspect `scripts/export-sequence.py` and the `sequence_*` modules; prefer the shared exporter when present.
- Distinguish stable content identifiers, curriculum capacity codes, and actual class-hour references. One content unit may span several meetings; multiple H tags are not by themselves duplicate content.
- Class tags `203` and `211` restrict content to the tagged classes; without class tags, it is common. Check the implemented inheritance and `CLASSE`/`CLASSES` properties before changing selection.
- Keep `HORAIRE_<class>`, `REPERES`, calendar rows, hour tags, and preparation references consistent. DONE records completed teaching; exporting a document does not mark it taught. Do not infer one class's progress from another's.
- The latest numbering decision excludes the positioning test from normal teaching-hour numbering. Group meetings use references such as `H03-1A` and `H03-1B`, anchored to the prior full-class meeting. Recheck the actual calendar rather than deriving numbers from source order.
- For shared group work, preserve one preparation with distinct occurrence/bilan records and separate student sheets for each class/group. A timetable change requires checking downstream progression and assessment dates within the requested scope.

## Export Interface

The inspected interface uses `level profile --classe CLASS --du Hxx [--au Hyy]`:

```bash
python3 scripts/export-sequence.py 2de prof --classe 211 --du H03 --theme night
python3 scripts/export-sequence.py 2de all --classe 203 --du H02 --au H03
python3 scripts/export-sequence.py 2de eleve --classe 211 --du H03-1A
```

- `prepa` produces preparation and correction material; `prof` projects slides; `manuel` prints four slides on A4 landscape in top-left, bottom-left, top-right, bottom-right order; `eleve` produces student sheets. Confirm current help for `all` and supported options.
- `--du` alone selects one hour or group. Inclusive ranges must include intervening group references in pedagogical order. Level and class are different arguments; the current SPF interface accepts `105-107` as an alias for calendar class `05-07`.
- `night` applies to projection; printable/student outputs remain light. For `all --theme night`, check that printable material is derived from light slides. Preserve separate light/dark outputs and inspect graph contrast.
- Resolve output locations through the current `sequence_build.py` and exporter arguments. Older class build directories and newer per-hour directories may coexist; distinguish maintained manuals from generated sources before editing or cleanup. Follow the current hour/profile naming convention and keep dates in document metadata where established.

## Authoring and Checks

- For projection font changes, trace the effective value through Org options/properties, exporter defaults, generated `\documentclass` options and preamble, and the installed class. A generated explicit size can override the class default. Keep the requested default in the maintained configuration and preserve explicit per-document overrides; inspect generated TeX and render a representative dense slide. Check the actual TeX class resolution before editing a template copy. Do not impose one font size on all profiles.
- For screenshot corrections, map each relevant image/annotation to the maintained source passage and record whether it is applied, ambiguous, or already satisfied. Viewing every image or finding an old DONE entry does not establish that corrections were implemented; preserve originals and recheck active comments.
- For a requested simple projection with separately supplied exercises, retain the requested course/mental-calculation link and brief instructions. Do not expand it into an exercise pack. Preserve the user's new Org lines and structure, making only requested corrections and changes necessary for export.
- Keep shared Asymptote figures in discoverable asset files. Use supported Org figure/layout properties to control inclusion and column width; inspect the renderer's actual property names instead of inventing them.
- Preserve semantic roles, explicit copy-to-notebook markers, lists, corrections, and student visibility. Do not infer a copy marker solely from a nearby heading or add it to every exercise.
- Validate actual teaching time, phases, capacity coverage and first introduction, without changing the established subtheme order unless asked. Never invent textbook exercise statements or corrections when only their references are available.
- Allow student sheets to span pages. Check page/total counts per teaching hour, headers/footers, class labels, and the projection/print differences. A successful compilation does not establish absence of clipping or correction leakage.
- For changes to shared rendering or selection, exercise the affected profiles and representative full-class/group/range cases. Use existing checks, shell syntax and Elisp parsing where applicable; do not require an exhaustive rebuild for a wording-only edit or override the user's explicit validation limits.
