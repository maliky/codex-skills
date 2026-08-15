# Storyboard Production

Use this reference for mode detection, claimed image-generation waves, durable recovery, and publication. Read [visual review and retries](visual-review-and-retries.md) before deciding generation outcomes.

## Source Authority

Read `AGENTS.md`, `RECETTES.org`, `STORYBOARDS.org`, current command help, and the active queue with its immutable receipts. `DEV.org` and `storyboard-production/README.org` provide history but may contain old counts or superseded procedures. The executable pipeline, active queue, and receipts are authoritative.

## Detect The Active Mode

From `/SCRATCH/koneMI/Cuisine`:

```bash
test -f storyboard-production/PANEL_QUEUE.tsv && test -f scripts/storyboard_panels.py
```

- If both files exist, use the native panel workflow for normal production.
- Use the legacy sheet workflow only for an explicitly requested old master, crop, migration, revalidation, archive operation, or finalization that depends on it.
- Never call `storyboard_batch.py claim-wave` while native production is active.

## Native Authority

- `PANEL_QUEUE.tsv`: panel status, phase, claim identifiers, attempt budgets, and accepted files.
- `panel-receipts/`: immutable native claim, review, and reopen transitions.
- `PANEL_ATTEMPTS.jsonl`: append-only native attempt history.
- `panel-evidence/`: rejected evidence used for targeted retries.
- `CONTINUITY_PROFILES.jsonl`: per-recipe continuity constraints.
- `assets/`: accepted panels and assembled recipe versions.

These paths are under `storyboard-production/`. Do not derive state by scanning assets.

## Native Resume Decision

At the start of every fresh or interrupted turn:

```bash
python3 -B scripts/storyboard_panels.py reconcile
python3 -B scripts/storyboard_panels.py validate
python3 -B scripts/storyboard_panels.py status --json
```

Choose exactly one next action:

- If `claimed` is non-empty, find the matching immutable claim receipt and finish that wave. Do not claim more panels.
- If there is no claim and the current phase has `pending`, claim at most four panels.
- If only `blocked` remains in the phase, report the blocked set and aggregate rejection causes. Reopen only when a specific correction is available and the user's goal requires another attempt.
- If the phase advances, rerun validation and status before its first generation.
- If every panel is accepted, use the repository's current publication or finalization path and focused tests.

## One Native Wave

```bash
python3 -B scripts/storyboard_panels.py claim --limit 4
```

The claim receipt contains the exact `wave_id`, `attempt_id`, recipe, step, and prompt. Generate one independent square image per item with that exact prompt. Do not combine panels into a sheet, rewrite the prompt ad hoc, substitute another recipe, or leave a consumed claim without a recorded result.

Inspect every image and build one result JSONL. Every row preserves the claim identifiers and includes factual `notes`. Accepted and rejected rows identify the generated image so accepted assets or rejected evidence remain traceable.

Record the complete wave:

```bash
python3 -B scripts/storyboard_panels.py review --results WAVE.jsonl
python3 -B scripts/storyboard_panels.py validate
python3 -B scripts/storyboard_panels.py status --json
```

Do not start another claim until the wave is durable and no panel remains `claimed`. After receipts are written, retain only identifiers and the status summary in conversational context; do not repeatedly reload prior images or full generation payloads.

## Native Retry And Reopen

The next claim incorporates the previous rejection note as a targeted correction. Make the note short, observable, and complete enough to identify all blocking defects.

Do not reopen a blocked panel merely to increase throughput:

```bash
python3 -B scripts/storyboard_panels.py reopen \
  --title "RECIPE" --step 1 --extra-attempts 1 \
  --reason "OBSERVABLE CORRECTION TO TEST"
```

Never edit attempt counters or statuses directly. Prefer a targeted edit of rejected evidence only when the image tool can preserve the valid composition and the receipt records a new attempt. Otherwise generate a fresh image from the immutable retry prompt.

## Legacy Sheet Workflow

Legacy state lives in `QUEUE.tsv`, `PROMPTS.jsonl`, `receipts/`, `ATTEMPTS.jsonl`, `addenda/`, and `evidence/`. Inspect `storyboard_batch.py --help` before an explicit legacy operation because native migration may disable old claim commands.

```bash
python3 scripts/storyboard_batch.py reconcile
python3 scripts/storyboard_batch.py validate
python3 scripts/storyboard_batch.py status --json
```

Use `crop` only for a reviewed legacy master. Use `finalize` only when native and legacy authorities satisfy current completeness checks. Preserve rejected masters and superseded versions; structural cropping never replaces visual approval.
