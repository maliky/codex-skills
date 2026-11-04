# Site And Release

## Catalogue And Interaction

`RECETTES.org` supplies validated text and editorial links; use `scripts/recipe_catalog.py` and the maintained `import_recipes` command rather than reconstructing recipes in templates. Inspect the import dry-run and validation results before an authorised apply. Avoid duplicate imports and preserve source traceability.

`ORIGINES-RECETTES.tsv` records the book's pictogram zone, which is distinct from a recipe's textual `ORIGINE` or a researched claim about the dish. Keep those meanings separate in filters and labels. Preserve category order and combine search with documented ingredient/duration/person filters; missing duration/person values do not become invented defaults.

Guided cooking offers ingredients, steps and the final presentation. Verify swipe, buttons and keyboard equivalents, first/last boundaries, current/total step, URL fragment reload and Escape/full-recipe return. A swipe must not interfere with ordinary scrolling or text interaction. Keep the complete recipe available without JavaScript. Reuse `scripts/check_cooking_browser.py`, including its `--all-recipes` mode when a shared step-navigation change warrants it, and the appropriate colour/ingredient browser scripts.

## Private Media And Packaging

Images and pages retain the existing Nginx authentication. Serve only allowed asset names, formats and widths; keep source photographs, generated masters, review histories and secrets out of the packaged runtime. Preserve private caching, ETags, responsive variants and validated-original fallbacks. Do not upscale a small original merely to claim higher resolution.

Follow `README.org` and `deploy/package_prototype.py` for the current build/import/package sequence and project database selection. A package build is not a service deployment. Verify package contents before the authorised switch; do not copy the whole dirty checkout or asset-production tree into the published directory.

For release work, inspect `deploy/`, the active `africa-cook` service and the current hostname/config rather than assuming source templates are installed. Verify Django checks and relevant catalogue tests first, then the changed browser interaction. After an authorised publication, verify anonymous denial, authenticated pages and media, the accepted artwork variants, and the service's actual loaded package. Host DNS/TLS changes use `koba-vps-webops` within the requested scope.
