---
name: cuisine-book-engineering
description: "Use when working on the /SCRATCH/koneMI/Cuisine recipe-book repository, including photographed-page OCR, OCR-MANIFEST.tsv and RECETTES.org editorial reconciliation, French recipe cleanup, STORYBOARDS.org prompts, storyboard claim/review/reconcile queues, immutable production receipts, resumable image-generation waves, strict black-ink visual review, deterministic panel cropping, revalidation, or interrupted Cuisine production recovery."
---

# Cuisine Book Engineering

Treat reviewed Org sources, manifests, queues, and production receipts as operational state. Preserve source photographs and rejected evidence; publish only artifacts that pass structural and editorial or visual review.

## Avoid When

- The task is generic document conversion outside the Cuisine repository; use `document-conversion`.
- The task is a one-off image generation or edit with no Cuisine production state.
- The task concerns the future recipe web application rather than corpus or storyboard production.

## Workflow

1. Confirm the repository root, branch, worktree state, and current instructions in `AGENTS.md`.
2. Read the relevant `DEV.org` entry and the authoritative state files for the requested phase.
3. Route OCR and corpus work through the maintained scripts and manifests; never overwrite original photographs or treat raw OCR as reviewed text.
4. Start storyboard work with `storyboard_batch.py validate` and `status --json`; never infer progress from chat memory or image counts.
5. Use explicit claim, generation, visual review, receipt, crop, and publication gates. Reconcile durable receipts after interruption before claiming new work.
6. Extend an exhausted attempt budget only through the explicit `reopen` command with a recorded reason; never edit queue counters by hand.
7. Run phase-specific validation and focused tests before reporting completion or committing changes.

## Routes

- **Photographs, OCR, editorial review, and `RECETTES.org`**: read [OCR and corpus](references/ocr-and-corpus.md).
- **Storyboard claims, generation, review, receipts, recovery, and crops**: read [storyboard production](references/storyboard-production.md).

## Output Expectations

Report the authoritative state inspected, claim or wave handled, accepted/rejected/revalidated counts, validation results, and recipes left in `pending_generation`, `in_progress`, `needs_revalidation`, or `failed_after_3`.
