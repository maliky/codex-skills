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

## Bootstrap Scripts

- `scripts/bootstrap_env.sh` creates `.env` only if missing, generates local secrets, and preserves an existing `.env`.
- The `psiaka` branch can contain `scripts/bootstrap_env.ps1`; verify bare refs or the deployed checkout before saying the PowerShell script is absent.
- The PowerShell script accepts host, bind address, port, and project-name values and is intended for Windows/Vite-friendly local setup.
