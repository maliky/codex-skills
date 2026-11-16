---
name: kolabi-run-analysis
description: "Analyze Kolabi runs, prices, positions and balances: execution forensics, account-equity reconciliation, family PnL and exposure, and portfolio comparisons at startup prices."
---

# Kolabi Run Analysis

Analyze Kolabi bot runs from logs, DB-backed order state, and operator observations. Keep this skill focused on reporting and forensics; use `kolabi-bot-runtime` when changing reducer/runtime code.

## Workflow

1. Identify the run boundary, logged strategy snapshots, symbol, exchange, environment, and log path.
2. Separate current-run facts from prior-run leftovers and map each attempt to its accepted revision; the current file alone is not execution evidence.
3. Collect terminated pairs before partial or still-live pairs.
4. Build a compact table first, then explain anomalies below it.
5. Keep virtual confirmations separate from real fills/PnL, and label fee/net calculations approximate unless the exchange ledger or fee rows are available.
6. Do not report intentional user stops as failures; report what completed before the stop.

## Routes

- **Run reports, revision attribution, event evidence, and terminated-pair tables**: read [run reporting](references/run-reporting.md).
- **Prices, wallet/position evolution, account losses, or family results reconciled with equity**: read [account reconciliation](references/account-reconciliation.md).
- **Portfolio growth with prices held at startup values**: read [portfolio comparison](references/portfolio-comparison.md); report contributions per symbol and reconcile them to the account total.

## Output Expectations

Lead with the run scope, then provide the table, then list anomalies and confidence. Include which source was used: log lines, DB rows, exchange response, or user observation.
