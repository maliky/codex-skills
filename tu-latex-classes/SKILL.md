---
name: tu-latex-classes
description: "Use when maintaining Tubman University LaTeX class or style files, including .cls and .sty behavior, Org-to-LaTeX export regressions, class inventories, TU house formatting, macro refactors, header spacing, memo or letter alignment, forms, minutes, policies, and curriculum class compatibility."
---

# TU LaTeX Classes

Keep TU class edits scoped, class-aware, and export-tested. Prefer class-level fixes over generated-output patches.

## When to Use

- Modify TU `.cls` or `.sty` files.
- Fix Org-to-LaTeX export regressions tied to TU class behavior.
- Align memo, letter, policy, form, minutes, beamer, or curriculum formatting.
- Decide which class-local `tucommon.sty` or macro layer owns a fix.

## Avoid When

- The task is document conversion without class changes; use `document-conversion`.
- The task is curriculum source normalization; use `tu-curriculum-transformation`.
- The user only asks for wording edits in an Org source.

## Workflow

1. Identify the actual class/style file used by the document or export path.
2. Inspect related class-local copies before assuming a shared fix propagates.
3. Make the minimal class-side change that preserves existing names and export templates.
4. Validate with the real Org/LaTeX route or a focused direct TeX example.
5. Report exact control points when the user asks for a knob or spacing variable.

## Routes

- **Class ownership**: read [class inventory](references/class-inventory.md).
- **Macro/layout refactor**: read [class refactor patterns](references/class-refactor-patterns.md).
- **Export regression**: read [export compatibility](references/export-compatibility.md).

## Output Expectations

Report files changed, class family affected, validation route, compile/export results, and any legacy fallback that stayed in place.

## References

- [class inventory](references/class-inventory.md)
- [class refactor patterns](references/class-refactor-patterns.md)
- [export compatibility](references/export-compatibility.md)
