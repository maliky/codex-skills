# Operator Logging

Use this reference when feed behavior affects operator trust or console action visibility.

## Logging guidance

- keep action lines compact and action-focused
- include symbol, pair, event id, and effect when possible
- keep private feed noise out unless it directly impacts command safety
- prefer one-line summaries over multiline dumps

## Suggested fields

- symbol or pair
- status transition
- source (`public`, `private`, reconciliation)
- action result

## Pressure Versus Freshness

Compare successive `REST_SUMMARY` and `REST_PRESSURE_SUMMARY` observations with timestamps. `queued` and `oldest` describe queued work; `class_wait_max` is an interval dispatch sample, not necessarily the age of all still-queued requests. `deferred_heads` is not tail/amend queue depth. Distinguish per-interval from cumulative metrics, and verify public price freshness independently before blaming exchange throttling or feed latency.

For financial inspection, record each price, balance and position observation time and completeness independently; partial deltas cannot prove zero holdings. Use [account reconciliation](../../kolabi-run-analysis/references/account-reconciliation.md) for valuation and ledger interpretation. Reporting does not authorize order recovery writes, cancellation, bot stop or restart.
