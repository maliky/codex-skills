# Storyboard Production

Use this reference for prompt preparation, claimed image-generation waves, visual review, durable recovery, and mobile panel publication.

## Source Authority

Read these in order:

1. `RECETTES.org` for validated recipe facts.
2. `STORYBOARDS.org` for panel sequence and source guidance.
3. `AGENTS.md` for current visual fidelity rules.
4. `storyboard-production/QUEUE.tsv` for current status, prompt revision, claim identifiers, and attempt budgets.
5. `storyboard-production/PROMPTS.jsonl` for generated base prompts.
6. `storyboard-production/receipts/` for immutable claim, review, and reopen transitions.
7. `storyboard-production/ATTEMPTS.jsonl` for the append-only attempt log.
8. `storyboard-production/addenda/` and `evidence/` for targeted retries and rejected or superseded evidence.

Use `python3 scripts/storyboard_batch.py status --json` for current counts. `storyboard-production/README.org` is a prepared snapshot and may be stale.

## Claimed Generation Cycle

1. Run validation and reconcile interrupted durable transitions before selecting work:

```bash
python3 scripts/storyboard_batch.py validate
python3 scripts/storyboard_batch.py reconcile
python3 scripts/storyboard_batch.py status --json
```

2. Claim at most four eligible recipes. Use `--addenda FILE.json` only for reviewed targeted corrections:

```bash
python3 scripts/storyboard_batch.py claim-wave --limit 4 --addenda FILE.json
```

The claim changes queue rows to `in_progress`, assigns `wave_id` and `attempt_id`, and stores an immutable claim receipt containing the exact prompt. Generate one independent master per claim item without rewriting that prompt ad hoc.

3. Review every master visually. Record accepted, rejected, error, or revalidated outcomes with the claim identifiers, then process them through the explicit review command:

```bash
python3 scripts/storyboard_batch.py review --results WAVE.jsonl --jobs 4
```

`process-wave` remains compatible with older implicit waves, but do not mix explicit and implicit claims in one result set. Review receipts make interrupted transitions replayable; `reconcile` restores them into `QUEUE.tsv` and `ATTEMPTS.jsonl` and identifies stranded `in_progress` work.

4. Run `status --json` after each wave. Resume from queue and receipts, never from chat memory, generated file counts, or remembered wave numbers.

The default budget is three attempts per prompt revision. Track `revision_attempts` separately from `lifetime_attempts`. After exhaustion, retain the audit record as `failed_after_3`. Additional attempts require an explicit reason:

```bash
python3 scripts/storyboard_batch.py reopen --title "RECIPE" --extra-attempts 1 --reason "REASON"
```

Do not promote rejected masters. Keep rejected evidence and archive superseded or invalidated accepted assets; maintain one live authoritative asset version.

## Visual Review

- Require pure black-ink line art on plain white paper: no color, sepia, grayscale wash, glossy texture, text, numbers, logos, or watermark.
- Panel 1 is an exact overhead mise en place with no hands: same ingredients, countable units, weights, volumes, and first-listed alternatives; omit every optional ingredient.
- For every countable quantity above 7, group every unit into separated countable packs without changing the total, for example `24 = 4x6`, `9 = 3x3`, and `13 = 6+6+1`.
- Show a weight as one batch on a plain analog scale without digits and a volume in one neutral unmarked vessel. Do not duplicate one ingredient in several forms or containers.
- Show one dominant operation per intermediate panel. Before the finale, allow at most two coherent hands or forearms from the same chef and no face, torso, assistant, or montage action.
- Reserve the complete recurring chef for the final presentation-only panel. Preserve chef, clothing, ingredient transformation, and utensil continuity.
- Require the requested panel count, straight continuous borders, regular white gutters, no false interior borders, and a layout that can be deterministically cropped and reconstructed.

Structural crop success does not prove recipe fidelity. A visually correct sheet that fails deterministic crop validation is also rejected for production.

## Finalization

Use `crop` only for a reviewed master that needs isolated processing. Run `finalize` only when every recipe is accepted; it must fail while pending, in-progress, revalidation, or failed rows remain. Report queue totals, receipt/reconcile outcome, and focused test results after each production run.
