# CSRS ENT Workflow

## Repositories And Branches

- Current PENT/CSRS-ENT work has appeared in `/home/jil/python-ent`, `/home/jil/pent`, and `/home/jil/csrs_ent`; inspect the actual active checkout before acting.
- The PENT bare remote was `/home/jil/git/pent.git`; later rename work may move this toward CSRS-ENT naming, so verify remotes before pushing.
- Use exactly `dev`, `preprod`, and `prod` when that branch model is active. `prod` replaces the old production `master`; do not add `main` or restore `master` without explicit approval.

## Architecture Boundary

- Odoo is the business source of truth for accounts, organization, missions, tasks, progressions, agendas, permissions, transitions, attachments, and audit.
- Django must not duplicate business models or migrations. Keep Django as UI, API/session, orchestration, and gateway code.
- Centralize Odoo access under `apps/django/gateway/`; keep CSRS-specific Odoo behavior in `apps/odoo/addons/csrs_reporting/`.
- Treat `csrs_report` as a migration/source reference, not as a model to copy into Django.

## Reuse-First Rule

Before writing production code, inspect this order:

1. Existing Odoo or Django capability.
2. Configuration of that capability.
3. Framework-native extension.
4. Mature compatible OCA or Django package.
5. Custom code for the remaining gap only.

Reuse Odoo `res.users`, `hr.employee`, `hr.department`, `project.task`, `mail.thread`, `mail.activity.mixin`, ACLs, record rules, and attachments before adding custom models.

## Odoo Gateway Contracts

- Odoo 19 JSON-2 target: `POST /json/2/<model>/<method>` with bearer auth and optional `X-Odoo-Database`; one transaction per call.
- Legacy `/jsonrpc` or `call_kw` code may still exist. Inspect the current gateway before extending it.
- In Odoo 19, a public facade method without `@api.model` can be treated as recordset-style and read `args[0]` as record IDs. For abstract facade methods such as `csrs.api.api_*`, missing `@api.model` can surface as HTTP 503 with `IndexError: list index out of range`.
- For direct `odoo shell -c` checks, pass container `HOST`, `PORT`, `USER`, `PASSWORD`, and `ODOO_DB_NAME` rather than assuming a local PostgreSQL socket.

## Testing And Implementation

- Follow BDD -> TDD -> implementation -> refactoring for business slices.
- Keep the first mission slice small, such as `draft -> submitted`, with Odoo business operation/state change, mocked gateway test, Django view, then real integration test.
- Use typed, deterministic functional-core code with thin effectful boundaries.
- Expected static checks can include Django check, pytest, Ruff, mypy, Python/XML compilation, Bash syntax, Odoo post-install tests, and Compose config.

## Deployment

- This host uses `docker-compose` 1.29.2. Prefer `docker-compose --env-file ... -f infrastructure/compose/compose.yaml config --quiet`; do not assume Compose v2 syntax works.
- Planned local layout can include Django at `https://ent.koba.sarl`, Odoo at `https://odoo.ent.koba.sarl`, localhost ports `18007`, `18069`, and Odoo gevent/WebSocket `18072`; recheck current values before applying them.
- PostgreSQL should remain private. Preserve volumes and existing passwords unless the user explicitly asks to rotate or delete them.
- Safe preprod sequence: verify branch state, create a mode-600 PostgreSQL dump, fast-forward or merge into `preprod`, run the repo deploy script, then verify services, `/readyz/`, `/app/`, and direct Odoo calls.
- DNS success does not imply Nginx, TLS, WebSocket, or application readiness; use `koba-vps-webops` for those host layers.
