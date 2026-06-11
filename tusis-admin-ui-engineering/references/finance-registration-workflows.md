# Finance And Registration Workflows

Use this reference when TUSIS UI work touches finance officer dashboards, student balances, registration status, payments, invoices, course fees, or role-specific registration workflows.

## Trace The Workflow

- Start from the reported user and role, then trace student -> registration -> courses/sections -> invoices -> payments -> balance -> dashboard visibility.
- When the user reports money due without an actionable finance-officer path, inspect both backend queryset/service logic and template visibility.
- For odd course appearances, trace origin through curriculum records, section import, registration import, grade import, and alias mapping before editing code.

## Course Fees And Invoices

- Distinguish future course-fee configuration from invoices already generated for an active semester.
- When fees change, identify whether the expected behavior is recalculation, adjustment, credit/debit note, or only future invoice generation.
- Keep financial changes auditable; do not silently rewrite payments or invoice history without a clear business rule.

## Role Verification

- Verify as the exact role when practical: finance officer, registrar, enrollment officer, student, or admin.
- Check group membership, model permissions, view permissions, and template conditions separately.
- For student-facing workflows, verify that the dashboard shows both status and next action, not just raw data.

## Reporting

Report the affected role, student or account identifier, source of each course/charge, dashboard route checked, and whether the fix changed visibility, data calculation, or both.
