---
name: csrs-report-engineering
description: "Use when working on the CSRS Report Django/React app or psiaka deployment workflow, including /home/jil/csrs_report, classic-Django-to-React migration, /app/ and /api/v1/ behavior, session/CSRF APIs, pyenv csrs, Vite/WhiteNoise builds, Docker Compose deployment, branch synchronization, and bootstrap_env.sh or bootstrap_env.ps1 discovery."
---

# CSRS Report Engineering

Keep CSRS product behavior, deployment state, and branch state tied together. Inspect the real checkout, deployed path, and target branch before making file-existence, sync, or deploy claims.

## Avoid When

- The issue is only DNS, Nginx, TLS, Docker host wiring, or disk triage; use `koba-vps-webops`.
- The issue is generic Django or React advice with no CSRS path, deployment, or business-rule implication.

## Workflow

1. Confirm the active path and branch: usually `/home/jil/csrs_report`, `/srv/apps/psiaka/app`, or a temporary implementation checkout.
2. Preserve the classic Django UI at `/` until the user explicitly accepts React parity.
3. Keep React at `/app/`, static React assets under `/static/react/`, and versioned APIs under `/api/v1/` with session/CSRF behavior.
4. Preserve adopted rules: one primary manager edits and validates, secondary supervisors view/comment, reporting is weekly, 100% requires manager validation, ownership transfers automatically, and competencies stay outside MVP unless reopened.
5. Use the repo Python environment: `pyenv activate csrs` or the checked-in `.python-version`.
6. Before deploy or browser-heavy validation, check disk pressure and remove only agreed temporary build/browser artifacts.
7. For branch sync, fetch first, inspect divergence, then use fast-forward merge only when the tree and branch relationship allow it.

## Routes

- **Project, deploy, and bootstrap workflow**: read [workflow](references/workflow.md).

## Output Expectations

Report the path, branch, environment, product rule touched, validation commands, deployed service changes, and any public HTTPS or authenticated API checks performed.
