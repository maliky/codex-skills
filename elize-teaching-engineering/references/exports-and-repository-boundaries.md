# Exports and Repository Boundaries

Use this reference when editing Org/LaTeX setup, compiling teaching documents, validating PDFs, or changing branch-scoped Elize artifacts.

## Maintained Sources

- Org is authoritative when it generates TeX or PDF. Preserve headings, drawers, properties, tags, tables, links, blocks, raw LaTeX, setup directives, and local variables.
- Maintained assessment TeX and explicitly requested copied-TeX experiments are valid editing surfaces. Identify their role before applying the Org-source rule; never silently replace the canonical lesson with an experimental export.
- Keep prose paragraphs and list items on one logical line unless Org syntax requires otherwise.
- Respect `.dir-locals.el`, repository setup files, and the declared `#+LATEX_CLASS`. The current templates live under `/home/mlk/Templates/Elize`; inspect their current README and build scripts before choosing commands.
- Maintain template or Emacs registration changes in their own authoritative repository. In `/home/mlk/.emacs.d`, `init.org` is the source and `init.el` is generated.

## Export and Render Checks

1. Parse or lint the changed Org source and verify links, blocks, properties, and export visibility.
2. Export from maintained Org through the current shared exporter. Batch Emacs does not automatically load interactive configuration: explicitly load the controlled class/environment registrations required by the exporter, rather than assuming personal `init.el` is loaded.
3. Compile with the engine declared by the template; Elize classes commonly require LuaLaTeX, but verify the current build script rather than relying on memory.
4. Check the generated file, page count, metadata, compilation log, missing characters, unresolved references, and overfull or clipped content.
5. Render and inspect representative pages, including dense content, tables, boxes, exercise/correction boundaries, and teacher/student visibility differences.

Syntax, compilation, and visual checks prove different things. Report each check actually run and never describe an unexecuted installation or export as verified.

After a source or output rename, update loader inputs, output declarations, shell names, and references together; regenerate missing exports instead of assuming there is an artifact to move. Check the affected profile matrix for regressions. Respect explicit user limits such as no compilation or no additional checks, and report the resulting validation boundary.

## Repository and Privacy Boundaries

- Inspect the branch and complete worktree before editing. Preserve unrelated work and generated artifacts covered by `.gitignore`.
- `Graphe-prerequis/` is an explicit boundary: do not propagate programme, progression, capacity, filename, or directory changes into it unless requested.
- Treat GIFT/AMC/Moodle question-bank migrations as a separate branch-scoped project. Reuse programme provenance where relevant, but do not fold migration artifacts into ordinary lesson work automatically.
- Keep `Admin/`, student lists, correspondence, and personal documents out of logs, reports, and commits unless an exact item is required and authorized.
- Commit only when requested. Stage intended paths, inspect the staged diff, run focused validation, and leave pushing or publication to a separate explicit request.
