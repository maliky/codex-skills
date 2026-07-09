# Admin UI Workflow

## Source Order

Start with these local files when they exist:
- `/home/jil/Tusis/Tusis_app/AGENTS.md`
- `/home/jil/Tusis/Tusis_app/README.org`
- `/home/jil/Tusis/Tusis_app/UX/admin-click-audit.org`
- affected `app/*/admin/`, `app/*/forms/`, `app/*/templates/`, and tests

Treat `AGENTS.md` as the repo-level contract. It includes file boundaries, lint expectations, and the rule not to edit migrations unless explicitly asked.

## Admin Filters And Changelists

- Preserve existing searchable dropdown and chained-filter patterns.
- For dependent filters, keep the broad-to-narrow order users expect, such as college -> department -> group.
- Check whether filtering is server-side, querystring-driven, or JavaScript-assisted before changing the UI.
- Watch for slow changelists caused by repeated queryset evaluation, missing `select_related`, missing `prefetch_related`, or expensive `__str__` methods.
- Prefer tests around queryset/filter choices when the behavior is deterministic.

## Admin Actions And Merge Flows

- Before adding or changing an action, identify whether it mutates data, writes logs, or should require confirmation.
- For merge-like operations, keep source and target semantics explicit.
- Preserve stdout/log behavior for admin-adjacent commands when the surrounding code already reports progress that way.
- Do not silently drop user-visible audit context.

## Role Dashboards And Permissions

- Check group/role membership, model permissions, and view-level permission gates separately.
- For visibility bugs, inspect both the template condition and the backend queryset/view logic.
- When the user reports that a role can or cannot see a link, verify as that role when practical instead of assuming from the template alone.
- If an admin page loads but an autocomplete or related-object chooser is empty, check the related model's `view_*` permission and the live user's effective permissions before changing admin queryset code.

## Click Audit Handling

- Treat `UX/admin-click-audit.org` as a triage ledger.
- Fix P0/P1 items first.
- Mark an item fixed only after verifying the affected route or workflow.
- Keep notes concise: symptom, fix, verification.
