# CSRS Workflow

## Project Shape

- Main checkout: `/home/jil/csrs_report`.
- Deployed psiaka path observed on this host: `/srv/apps/psiaka/app`.
- Use `/tmp/csrs-psiaka-impl` or similar only as a temporary implementation checkout; verify against the target branch before answering file-location questions.
- The local bare remote convention is `/home/jil/git/csrs_report.git`.

## Product Rules

- Keep the classic Django UI available at `/` while React adoption is progressive.
- React is served at `/app/`; do not move the primary app shell without checking public routes.
- `/api/v1/` uses Django session authentication and CSRF, not a detached token-only API.
- Optimistic concurrency uses revision checks; treat `409 stale_revision` as expected behavior.
- Preserve weekly reporting and primary-manager validation rules unless the user explicitly changes product scope.

## User Administration

- `POST /api/v1/users/bulk-action/` routes to transactional `bulk_manage_users`.
- Lock accounts, validate `state_token`, and process the batch atomically; a concurrent update cancels the whole batch with HTTP 409.
- Disabling preserves accounts, affiliations, and history.
- Deletion requires a previously disabled account with no technical rights, groups, permissions, affiliations, or other persistent data, plus a reason and exact `SUPPRIMER` confirmation.
- `HistoricalUser` should retain actor and reason.
- The React page is `/app/administration/utilisateurs`; synchronize OpenAPI/TypeScript and test both `frontend/src/features/users/UserManagementPage.tsx` and `tests/test_user_management.py`.

## Development And Validation

- Prefer `pyenv activate csrs` or the repository `.python-version` before Python commands.
- Expected validation can include Django tests, responsive Selenium checks, Vitest/frontend builds, OpenAPI generation, Ruff, mypy, migrations, and accessibility checks.
- In development, Vite should use `/`; production builds use `/static/react/`.
- Browser fixtures may need explicit `organization_unit` setup and `WebDriverWait` for async UI state.

## Deployment And Sync

- Before a large Docker or browser run, check disk pressure; prior runs hit 100% disk during validation.
- Deploy through the existing Compose stack and rebuild only the services needed for the change.
- Preserve the database container when rebuilding web/notifier services.
- Verify public HTTPS `/app/`, React assets, and authenticated API behavior after deployment.
- To sync `dev`, fetch the remote, inspect `git rev-list --left-right --count dev...origin/dev`, then use `git merge --ff-only origin/dev` only when behind.
- For the isolated preprod stack, verify the current path before acting; observed names include `/srv/apps/csrs-preprod/app` and later durable-path work around `/srv/apps/csrs-report-preprod`.
- The isolated preprod deployment used Compose project `csrs_preprod`, web port `127.0.0.1:18008`, and public host `preprod.report.ent.koba.sarl`; recheck current values before deployment.
- Validate healthy web, `api:user-bulk-action`, authenticated HTTP 200 with `batch_capabilities` and `state_token`, HTTPS `/connexion/` 200, and a React asset 200.

## Bootstrap Scripts

- `scripts/bootstrap_env.sh` creates `.env` only if missing, generates local secrets, and preserves an existing `.env`.
- The `psiaka` branch can contain `scripts/bootstrap_env.ps1`; verify bare refs or the deployed checkout before saying the PowerShell script is absent.
- The PowerShell script accepts host, bind address, port, and project-name values and is intended for Windows/Vite-friendly local setup.
