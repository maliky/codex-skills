# OKX Operator Workflow

Read current `scripts/kolabi-fresh-run --help`, `kolabi/bargain/cli.py`, and the OKX section of `MANUAL.org` before constructing a command. Confirm live versus demo, account scope, exact symbol, the intended command after `--`, and the selected DB lanes. Keep credential values out of terminal output and reports; demo credentials must not fall back to live credentials.

## Helper Effects

`scripts/kolabi-fresh-run --operator` loads the configured PostgreSQL environment, maps the selected account scope's DB URLs, may start PostgreSQL, initialises additive OKX identity tables, refreshes private evidence into local DBs, then runs one CLI command. It preserves existing data and listeners and does not start a strategy bot. Explain this scope before running it, even for `balance` or `position`; use `--dry-run` to preview the command sequence when needed. Check the installed script before relying on this description.

`permissions` and `check-symbol` inspect account and instrument readiness; `balance` and `position` report refreshed trading-account evidence. A trading portfolio does not cover funding or Earn wallets. If the user's question concerns funds elsewhere, inspect those account surfaces separately within the authorised read-only scope.

## Execution Boundary

- Use a market, cancel, amend or close command only within the user's explicit trading-operation scope. A code test or account inspection does not authorise a probe order. Keep `--environment` explicit for any action that can alter orders.
- A market acknowledgement does not prove a fill. Verify execution, exact identity and resulting position before a follow-up action; an opposite-side market order is not automatically reduce-only and can open a new position.
- Reconciliation may read the venue and write local evidence, but uncertainty remains unresolved when child history is incomplete, stale or conflicting. Preserve the original order identity and do not place a replacement to bypass the hold.

Report the command, environment, account scope and symbol without secret values, the helper's local effects, the evidence time and source, and any incomplete account or order evidence.
