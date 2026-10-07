# Recipe mappings and catalog imports

Keep `RECETTES.org` authoritative. Resolve the actual Cuisine checkout and inspect `scripts/link_vignettes.py`, `scripts/recipe_catalog.py`, and the `catalog` management command before reusing commands. Discover the working Python environment; a previous `.cache/django-deps` installation is not a portable prerequisite.

## Link reviewed recipes and panels

- `VIGNETTES_MANIFEST` selects the recipe's manifest; `VIGNETTES_ETAPES` records explicit recipe-step/panel associations. Use the existing linker to edit those properties without rewriting reviewed prose. Preview with `python3 scripts/link_vignettes.py` and inspect weak matches with `--review` before an authorized `--write`.
- Resolve active accepted versions from production queues and the sample manifest, not the newest-looking asset directory. Validate titles, panel order, existing paths, SHA-256 hashes, and native accepted-image paths against `PANEL_QUEUE.tsv` and its visual-review status.
- Permit several recipe steps to share a panel and steps with no intermediate image. Text similarity supplies candidate mappings, not visual approval. Review weak mappings explicitly; do not force one image per step to remove warnings.
- Preserve recipes expressed as an Org cross-reference rather than numbered preparation as a navigable application step. Verify that the link remains meaningful after import.

## Import and verify

Run `python3 scripts/recipe_catalog.py` with hash checks enabled, then `python3 manage.py import_recipes --dry-run` in the established environment. The dry run validates inputs without writing database rows. Apply migrations only when the target database and requested work require them.

For an authorized import, use the existing transactional `import_recipes` command. Repeated imports must update stable recipe identities without duplicates. Whole recipes absent from the incoming corpus must remain in the database. Within an imported recipe, the current implementation reconciles obsolete ingredients, steps, panels, and step/media links; preserve that distinction rather than claiming the importer never deletes any rows.

Exercise `python3 manage.py test catalog` and relevant corpus/mapping tests in an isolated test database. Meaningful cases include repeat imports, an existing recipe absent from the incoming corpus, obsolete children of an imported recipe, invalid hashes/paths, shared or absent step images, and cross-reference recipes. A failed validation must not leave a partial import. Never use a live catalog merely to demonstrate idempotency.
