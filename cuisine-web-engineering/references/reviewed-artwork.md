# Reviewed Web Artwork

## Choose The Collection

| Collection | Source and acceptance boundary |
| --- | --- |
| `assets/categories/` | Explicitly approved colour photographic category art and backgrounds; inspect its current manifest and review decisions. |
| `assets/recipe-colors/` | Colour versions of the validated final presentation drawings; preserve their composition, recipe facts and chef continuity. |
| `assets/ingredient-colors/` | Colour versions of the first mise-en-place drawings; preserve exact ingredients and the quantities specified by the source. |
| Original storyboard production | Separate monochrome editorial assets governed by `cuisine-book-engineering`; a colour website task does not authorise replacing them. |

Read the current collection queue, prompts, review files and source hashes. A dated progress total in README/DEV is not an inventory. Check whether work already exists before generating a replacement or initialising a queue. Keep approved styles specific to the collection; photographic category art is not a reason to turn all recipe drawings into photographs.

## Production And Continuation

Use the available image-generation/editing tool and its skill for bitmap work. Inspect source images before editing. Preserve recipe fidelity, required counts, anatomy and ingredient continuity from the local review instructions; apply the explicit colour/style decision for this web collection. Builders resize and package reviewed art; they do not replace visual review.

When the user authorises the remaining set, continue serially through recoverable batches until that set is complete or an actual blocker prevents progress. Do not end the task solely because one batch finished. Persist each source/prompt, output, visual decision, version and relevant hash before taking the next batch. After interruption, recover from the queue and durable reviews, resolve unfinished items, and resume without redoing accepted work. Do not impose the original book pipeline's four-panel wave limit on a different web queue.

Inspect each output against the actual source recipe and requested edit before marking it reviewed. Record a specific rejection reason and use it for the next attempt. Maintain unambiguous source/master/review mappings; do not accept an uninspected image from its filename or an earlier assistant's description.

Respect the requested retention scope. A request to remove new rejected colour retries after a corrected acceptance applies to those retries; it does not discard original monochrome sources or historical production evidence. Preserve the review decisions needed to explain acceptance and recovery.

## Disk Pressure And Generated Copies

Before another large image batch, check free space and resume from the durable queue in smaller batches if earlier runs filled the disk. A generated file under Codex's `generated_images/` is an output candidate, not an accepted project master; its filename or tool hint does not establish review status.

For an authorised cleanup, identify the current source/master/queue/review mapping and confirm the active deployed release uses retained assets. Preview exact paths, counts, and bytes. Compare generated copies with retained accepted masters by SHA-256; remove only copies proven identical, zero-byte failed outputs, or other specifically authorised rejects and caches. Keep original sources, accepted masters, review receipts, queues, and served derivatives. Recheck the queue, retained hashes, and free space afterward. Honour an explicit request not to make extra backups, while preserving the existing authoritative files.

## Build And Verify

Inspect `scripts/build_category_images.py`, `build_recipe_colors.py`, `build_ingredient_colors.py` and `catalog/recipe_colors.py` for the active collection's contract. Check source and master hashes plus the actual review evidence before building. The builders enforce different subsets of these checks; a successful resize alone does not certify editorial acceptance.

The current web derivatives use WebP widths 320/640/960. Only approved entries with current source fingerprints belong in the served manifest. Verify that stale or absent colour derivatives fall back to the validated original and that the matching asset/version is selected. Masters, queue files and review histories are production state, not public media. Source changes invalidate their derived acceptance until checked again.

## Recovering Missing Binaries

Reviewed queues and manifests do not prove the image binaries exist; this checkout can exclude them from Git. Recheck after the user reports a transfer. If originals are missing, an existing release can supply them only after verifying each candidate's SHA-256 against the current authoritative source manifest. Copy only verified matches; do not weaken checks or regenerate an original merely because its exact deployed copy is absent locally. A manifest label can identify an unavailable photograph, but disclose that metadata identification is not visual inspection.
