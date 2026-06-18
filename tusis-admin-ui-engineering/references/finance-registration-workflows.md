# Finance And Registration Workflows

Use this reference when TUSIS UI work touches finance officer dashboards, student balances, registration status, payments, invoices, course fees, or role-specific registration workflows.

## Trace The Workflow

- Start from the reported user and role, then trace student -> registration -> courses/sections -> invoices -> payments -> balance -> dashboard visibility.
- When the user reports money due without an actionable finance-officer path, inspect both backend queryset/service logic and template visibility.
- For odd course appearances, trace origin through curriculum records, section import, registration import, grade import, and alias mapping before editing code.
- For a named student, compare the student dashboard, finance invoice view, finance payment view, and admin records before concluding which total is wrong.
- Treat empty payment rows, hidden amounts, missing course titles, and contradictory pending/cleared counts as workflow bugs, not cosmetic issues.

## Course Fees And Invoices

- Distinguish future course-fee configuration from invoices already generated for an active semester.
- When fees change, identify whether the expected behavior is recalculation, adjustment, credit/debit note, or only future invoice generation.
- Keep financial changes auditable; do not silently rewrite payments or invoice history without a clear business rule.
- Separate amount due, total invoice value, pending payment, cleared payment, outstanding balance, and receipt total in both UI labels and tests.
- If a fee rule changes for the active semester, check whether existing invoices need a controlled recalculation path. Do not assume updating course fees automatically rewrites historical invoices.
- Use hover-only detail for dense course lists when the user asks to reduce clutter, but keep totals and status visible without hover.

## Role Verification

- Verify as the exact role when practical: finance officer, registrar, enrollment officer, student, or admin.
- Check group membership, model permissions, view permissions, and template conditions separately.
- For student-facing workflows, verify that the dashboard shows both status and next action, not just raw data.
- Registrar and enrollment officers often need direct Django admin access to entitled tables when the role dashboard is insufficient. Add links only for models their role can actually view or change.
- When the UI has redundant chips and sidebar links, prefer the persistent sidebar and remove duplicate chips unless they expose a distinct action.
- Search and CRUD screens for students should support practical filters such as id, name, college, program, and semester when those fields exist in the data model.

## Transcript And Source Downloads

- For transcript UI work, verify both PDF and Org/source download routes. A visible download button with a 404 source route is a failure.
- Bulk transcript selection should use clear student selection controls and preserve individual transcript output. Keep semester filters only when the workflow actually prints term-bounded batches.
- Header and table layout changes are part of the user-visible workflow: check logo/contact/student-info placement, margin fit, date format, and table alignment.

## Reporting

Report the affected role, student or account identifier, source of each course/charge, dashboard route checked, and whether the fix changed visibility, data calculation, or both.
