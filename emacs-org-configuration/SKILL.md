---
name: emacs-org-configuration
description: "Maintain literate Emacs configuration in init.org, verify tangled Elisp and live settings, diagnose Org refile targets, and register Org LaTeX classes. Use for Emacs configuration work beyond mail-specific composition."
---

# Emacs Org Configuration

Inspect the running Emacs instance and the authoritative configuration before changing behavior. In this workspace, `/home/mlk/.emacs.d/init.org` is maintained source and `init.el` is tangled output; confirm this relationship and repository instructions on the current host.

## Literate configuration

- Read the affected Org blocks, tangle headers, load order, Custom settings, and buffer-local overrides. A file's value can differ from the active runtime value.
- Edit the maintained source, then use the established tangle workflow and installed Org version. Do not hard-code an old package version from a transcript.
- For a behavior-preserving cleanup, compare tangled output before and after. Preserve active symbols, including apparent misspellings, until their callers and definitions establish that a rename is safe.
- Run `check-parens` on generated Elisp, not the whole Org document. Load/test the changed definitions in an appropriate environment and inspect the effective value or command in the affected live buffer. Avoid loading the entire personal init merely for syntax checking when it launches services or changes unrelated state.
- Keep Emacs configuration edits in their own repository. Unsaved live-buffer content may differ from disk; preserve it and use undoable edits when the task concerns that buffer.

## Missing refile targets

Inspect `buffer-file-name`, `org-refile-targets`, `org-refile-use-outline-path`, `org-agenda-files`, and any target verification function in the actual source buffer. Check whether the intended target file and heading level/tag match the configured selector, whether narrowing excludes headings, and whether cached targets need refreshing after a change.

Customized `org-refile-targets` supersedes manual defaults. Do not promise all level-one headings without inspecting the effective configuration. Diagnose requests for an explanation without modifying configuration; when a fix is requested, change the smallest relevant selector and verify the target picker without moving entries as a test.

## Org LaTeX registration

Trace the Org class name through `org-latex-classes`, export options, generated TeX, and the class found by `kpsewhich`. Existing helpers such as `mk/register-org-latex-class` may centralize registration; inspect their current definitions before extending them.

Keep template source, installed TeX files, and Emacs registration distinct. A template edit is not evidence that the TeX installation changed. Validate with a minimal representative export and inspect the resulting class/options. Batch Emacs does not automatically load the interactive init; explicitly load the established shared export configuration when needed.

For Mu4e or OrgMime composition behavior, use `emacs-mu4e-mail`. For lesson content and profile selection, use `elize-teaching-engineering`.
