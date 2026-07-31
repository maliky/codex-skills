---
name: kolabi-run-analysis
description: "Use for Kolabi bot run forensics and operator reports: analyze current or stopped runs, inspect logs, summarize terminated pairs, build Org tables, and explain fills, amendments, slippage, tOut, gross/net, and cumulative balance."
---

# Kolabi Run Analysis

Analyze Kolabi bot runs from logs, DB-backed order state, and operator observations. Keep this skill focused on reporting and forensics; use `kolabi-bot-runtime` when changing reducer/runtime code.

## Workflow

1. Identify the run boundary, strategy file, symbol, exchange, environment, and log path.
2. Separate current-run facts from prior-run leftovers.
3. Collect terminated pairs before partial or still-live pairs.
4. Build a compact table first, then explain anomalies below it.
5. Keep fee and net calculations approximate unless the exchange ledger or fee rows are available.
6. Do not report intentional user stops as failures; report what completed before the stop.

## Routes

- **Run reports and terminated-pair tables**: read [run reporting](references/run-reporting.md).

## Output Expectations

Lead with the run scope, then provide the table, then list anomalies and confidence. Include which source was used: log lines, DB rows, exchange response, or user observation.
