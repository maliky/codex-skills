---
name: cuisine-book-engineering
description: "Use for the Cuisine recipe-book repository: photographed-page OCR, RECETTES.org editorial review, storyboard production and recovery, recipe-step image mappings, and validated Django catalog imports. Applies to local and remote Cuisine checkouts."
---

# Cuisine Book Engineering

Treat reviewed Org sources, manifests, queues, and production receipts as operational state. Prefer the repository's current commands over remembered workflow details. Preserve source photographs and rejected evidence; publish only artifacts that pass structural and editorial or visual review.

## Avoid When

- The task is generic document conversion outside the Cuisine repository; use `document-conversion`.
- The task is a one-off image generation or edit with no Cuisine production state.
- The task concerns unrelated web-application features outside Cuisine corpus, storyboard, or catalog-import workflows.

## Workflow

1. Confirm the repository root, branch, worktree state, and current instructions in `AGENTS.md`.
2. Read the relevant `DEV.org` entry, current command help, and authoritative state files. A prepared README or this skill may lag behind the executable pipeline.
3. Route OCR and corpus work through the maintained scripts and manifests; never overwrite original photographs or treat raw OCR as reviewed text.
   For recipe-image mappings or catalog imports, use the catalog-import route below; the following claim/generation steps apply only to storyboard production.
4. Detect storyboard mode before acting. If `storyboard-production/PANEL_QUEUE.tsv` and `scripts/storyboard_panels.py` exist, use native per-panel production. Use `storyboard_batch.py` only for an explicitly requested legacy sheet, archive, migration, or finalization operation.
5. Resume native production with `reconcile`, `validate`, and `status --json`. Resolve every existing `claimed` panel from its immutable claim receipt before making another claim; never infer progress from chat memory, image counts, or wave numbers.
6. Process at most one four-panel wave at a time: claim, generate the exact receipt prompts, inspect every output, record review outcomes, and report the new authoritative status. Keep images and large tool payloads out of later context once their receipts are durable.
7. Base a retry on the previous rejection note. Extend an exhausted panel budget only through `storyboard_panels.py reopen` with the exact title, step, extra-attempt count, and a durable reason; never edit queue counters by hand.
8. Run phase-specific validation and focused tests before reporting completion or committing changes.

## Routes

- **Photographs, OCR, editorial review, and `RECETTES.org`**: read [OCR and corpus](references/ocr-and-corpus.md).
- **Storyboard mode detection, native claims, generation, receipts, recovery, legacy operations, and publication**: read [storyboard production](references/storyboard-production.md).
- **Visual acceptance decisions and targeted retry design**: read [visual review and retries](references/visual-review-and-retries.md).
- **Recipe-step image mappings and Django catalog imports**: read [catalog imports](references/catalog-imports.md).

## Output Expectations

For native production, report the current phase, claim or wave handled, accepted/rejected/blocked counts, validation result, and panels left in `pending` or `claimed`. For legacy production, report accepted/rejected/revalidated counts and recipes left in `pending_generation`, `in_progress`, `needs_revalidation`, or `failed_after_3`. When work remains, state the exact next recoverable action instead of relying on conversational context.

For imports, report mapping/hash validation, unresolved weak matches, dry-run or actual-import status, and idempotency checks. Do not infer visual acceptance from text alignment or file existence.
