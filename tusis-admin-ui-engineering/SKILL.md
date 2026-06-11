---
name: tusis-admin-ui-engineering
description: "Use when designing, auditing, debugging, or fixing TUSIS Django admin and website UI workflows, including finance officer dashboards, registration and payment visibility, admin click audits, Selenium or chromedriver checks, chained filters, admin actions, changelist performance, 500 errors from admin views, UX/admin-click-audit.org triage, P0/P1 interface bugs, and role-specific dashboard or permission visibility issues."
---

# TUSIS Admin UI Engineering

Use this skill for TUSIS interface work where the main risk is Django admin behavior, navigation, permissions, browser-visible failures, or workflow ergonomics.

Do not use it for import parser normalization, curriculum resolution, duplicate import handling, or batch data reconciliation. Use `tusis-import-engineering` for those.

## Default Workflow

1. Read `/home/jil/Tusis/Tusis_app/AGENTS.md`, then inspect the affected admin, model, form, template, or view.
2. Separate the failure class:
   - admin configuration and changelists
   - permissions and role visibility
   - frontend/admin JavaScript or CSS
   - browser navigation and 500 errors
   - performance or query explosion
3. Prefer small, local fixes that preserve the existing admin patterns.
4. For browser-facing work, verify with the narrowest practical check:
   - Django unit/admin tests for code paths
   - Selenium only when real browser behavior matters
   - direct `curl` or log checks for deployment-visible 500 errors
5. When the task references a click audit or priority list, update the audit file only after verifying the specific item.

## References

- Read [admin-ui-workflow](references/admin-ui-workflow.md) for admin filters, actions, role dashboards, and click-audit handling.
- Read [browser-and-preprod-checks](references/browser-and-preprod-checks.md) for Selenium, preprod, and 500-error triage patterns.
- Read [finance-registration-workflows](references/finance-registration-workflows.md) for finance officer, payment, invoice, registration, and role-specific workflow checks.
