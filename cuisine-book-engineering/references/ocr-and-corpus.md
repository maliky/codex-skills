# OCR And Corpus

Use this reference for photographed-page ingestion, OCR review, and maintained recipe text in the Cuisine repository.

## Source Authority

- `Sources/` contains immutable source photographs.
- `.cache/ocr/` contains reproducible machine evidence, not maintained prose.
- `OCR-MANIFEST.tsv` records source hashes, intrinsic page type, inclusion decisions, visual content, labels, and review notes.
- `RECETTES.org` is the reviewed recipe corpus.
- `DEV.org` records decisions and execution evidence but does not override the manifest or reviewed corpus.

Do not infer that a generated draft is editorially complete. Do not move, rename, crop, or rewrite source photographs during OCR work.

## Pipeline

Run from `/SCRATCH/koneMI/Cuisine`:

```bash
python3 scripts/build_recettes.py benchmark --sources Sources --work-dir .cache/ocr --reference tests/fixtures/ocr_reference.tsv --max-side 2400 --jobs auto
python3 scripts/build_recettes.py all --sources Sources --work-dir .cache/ocr --manifest OCR-MANIFEST.tsv --jobs auto
python3 scripts/build_recettes.py validate --org RECETTES.org --manifest OCR-MANIFEST.tsv --sources Sources
```

- Benchmark representative pages before choosing reduced resolution; do not assume smaller images preserve OCR quality.
- Let `--jobs auto` bound process concurrency from CPU and memory. Each OCR/ImageMagick worker is internally single-threaded to avoid oversubscription.
- Reuse hash- and profile-keyed caches. Parent-only atomic publication keeps parallel runs deterministic.
- Preserve reviewed manifest columns when rerunning OCR or migrating the manifest schema.

## Editorial Gate

- Treat machine `page_type` and category suggestions as starting points only.
- Keep intrinsic page type separate from `corpus_action=include|exclude`.
- Require an exclusion reason for every excluded source and a visual label for non-text visual content.
- Keep mixed recipe/photo pages when recipe text is included; record the visual classification rather than deleting evidence.
- Allow one photographed page to map to several Org entries when the page contains several recipes.
- Fence raw OCR as literal evidence so numbered recipe instructions cannot corrupt Org structure.
- Correct French against the source page and reconcile recipe headings with the photographed index before declaring the corpus complete.

## Verification

Run focused repository tests, `build_recettes.py validate`, and `org-lint` when Emacs is available. Confirm source count and hashes, manifest coverage, inclusion/exclusion rules, category ordering, Org source links, and the absence of unresolved editorial rows.
