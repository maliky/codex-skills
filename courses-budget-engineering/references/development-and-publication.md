# Development And Publication

## Extension And UI Work

Use `catalog/brands/` and `tests/test_typed_contracts.py` as the current concrete extension example. Change the domain command, explicit editable fields, queries, form/resource declaration and export registration together when needed. `tests/test_architecture.py` checks boundary direction. Keep generic table behaviour in `ui`; business-specific filters and rules stay with their domain. Export eligibility is explicit and independent of the visible table registry.

Maintain French product language and server-rendered forms with optional TypeScript enhancement. Source lives in `frontend/`; `static/courses/app.js` is generated. Reuse the declared columns, filters, help and resources rather than adding model-specific branches to the common table engine. Preserve combined filters/search/sort/pagination, explicit unknown-value choices, keyboard access, nearby popovers, Escape and focus restoration. Batch selection covers the explicitly selected rows, not hidden pages.

## Verification

Use the project's locked environment and an isolated PostgreSQL test database; SQLite is not a substitute for transaction/locking checks. Consult `README.org` for the current test socket and database setup rather than copying a production URL. Relevant commands include:

```bash
COURSES_TESTING=1 .venv/bin/pytest -q tests/test_architecture.py tests/test_typed_contracts.py
COURSES_TESTING=1 .venv/bin/mypy
COURSES_TESTING=1 .venv/bin/python manage.py makemigrations --check --dry-run
npm test
npm run build
```

Choose affected business tests first and use the documented Ruff checks. Test migrations on an empty and representative test database when schema changes. Browser scripts under `tests/browser_*.py` mutate synthetic fixtures: use their dedicated local instance and test credentials. Never supply the production credential file or a public URL to those fixtures.

## Production Preparation And Release

The published instance uses `scripts/courses-compose`, which selects its environment file, Compose project and OCR profile. Inspect that wrapper before operating it; a generic Compose command can select the wrong project. Production credentials are private runtime data and must not be printed.

For authorised ticket preparation, inspect `prepare_ticket_data --help`, take and verify the documented backup, run the scoped `--dry-run`, review its preview, then apply with the returned `--expect` hash and `--apply`. A changed preview/hash requires investigation before mutation. Compare business exports and original source hashes afterward. Do not treat an already applied historical preparation as a fresh task to rerun automatically.

Use `scripts/backup_restore.py` and `deploy/PUBLICATION.org` for the requested release. Backup verification covers PostgreSQL and referenced originals; restoration uses a distinct empty target. Preserve running image references and replace only the intended application services. Verify migrations, private access, HTTPS workflows, exports and source hashes before declaring publication complete. Rollback must respect additive schema/data changes; do not restore an old database over new financial facts to undo a code release.
