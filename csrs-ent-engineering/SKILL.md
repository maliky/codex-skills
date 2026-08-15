---
name: csrs-ent-engineering
description: "Use when working on the CSRS ENT/PENT Django-Odoo stack, including /home/jil/pent, /home/jil/python-ent, /home/jil/csrs_ent, Odoo 19 as the business source of truth, Django as a typed UI/API gateway, apps/django/gateway, apps/odoo/addons/csrs_reporting, no duplicated Django business ORM, BDD/TDD vertical slices, Odoo RPC or JSON-2 contracts, dev/preprod/prod promotion, and ent.koba.sarl deployment."
---

# CSRS ENT Engineering

Keep Odoo authoritative for business state and Django thin. Inspect the real checkout, branch model, service health, and deployment target before implementing or promoting changes.

## Avoid When

- The task is the older CSRS Report Django/React app at `/home/jil/csrs_report`; use `csrs-report-engineering`.
- The task is only DNS, Nginx, TLS, host accounts, or containers; use `koba-vps-webops` after the app boundary is clear.
- The task is only self-hosted Git synchronization; use `self-hosted-git-operations`.

## Workflow

1. Confirm the active checkout: `/home/jil/pent`, `/home/jil/python-ent`, or `/home/jil/csrs_ent`.
2. Preserve the boundary: Odoo owns users, organization, missions, tasks, progressions, permissions, transitions, and audit; Django serves UI/API/session glue and calls Odoo through `apps/django/gateway/`.
3. Before creating a model, workflow, permission layer, adapter, or form abstraction, inventory existing Odoo, Django, installed dependency, and OCA capabilities.
4. Use BDD/TDD for vertical slices: write the smallest behavior test first, implement minimally, then refactor.
5. Keep pure deterministic logic typed and small; isolate effects at gateway, HTTP, Compose, and deployment boundaries.
6. For delivery, preserve the branch model `dev -> preprod -> prod`; do not recreate `master` unless explicitly requested.
7. Before deploying, back up the database, verify branch state, run focused tests, then validate public routes and direct Odoo calls.

## Routes

- **Architecture, Odoo contracts, tests, and deployment**: read [workflow](references/workflow.md).

## Output Expectations

Report the checkout, branch relationship, Odoo/Django boundary touched, tests run, deployment path, database backup state, service health, and public route or RPC checks.
