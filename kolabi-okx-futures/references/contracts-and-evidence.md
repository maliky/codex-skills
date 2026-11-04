# OKX Contracts And Evidence

Use the current `MANUAL.org`, `kolabi/shared/exchanges/okx_contracts.py`, `okx_adapter.py`, `okx_evidence.py`, `okx_store.py`, and the public/private feeder implementations as authority for the installed Kolabi revision.

## Instrument And Order Contract

- `OKXF` targets explicit European linear X-Perp instrument IDs. Check the exact instrument, product availability, settlement, account permissions and fee group against fresh account and instrument metadata. Do not substitute an ordinary dated future or global swap, guess a symbol, or roll a contract automatically.
- `A` quantities are contracts, `U` is USD notional, and percentages use eligible available USD collateral. Convert exposure with `ctVal` and `ctMult`; use the current `lotSz`, `minSz` and `tickSz` with Decimal rounding. Example instrument values are never defaults for another symbol.
- Check the supported account and net position modes before order submission. The adapter does not change account mode, leverage or collateral configuration. Preserve existing Kolabi gates, hooks, virtual execution, stop-amend thresholds and no-widen rules across this route.
- Keep original client IDs durably linked to venue client, logical, algo and triggered-child IDs. A placement or cancel receipt is not proof of execution or terminal cancellation; conditional `effective` proves activation, not child fill. Deduplicate fills by exact instrument, order and trade identity, and never blind-resubmit an uncertain role. Bounded history absence cannot establish a terminal outcome.

## Account And Financial Evidence

- `position` uses the selected instrument and shared fields: signed `qty`, `entry_price`, `leverage`, `liquidation_price` and `margin_mode`. A complete, recent REST snapshot can establish a flat selected instrument; missing, stale or partial WebSocket evidence cannot. Flat position-specific leverage and liquidation values remain null.
- `balance` is a complete trading-portfolio snapshot: all reported currencies, available amounts, equity, USD valuation, collateral flags, timestamp and venue total equity. Keep this distinct from eligible USD futures margin, which may be null even when other currencies are held. Funding and Earn wallets need separate evidence.
- Keep actual execution VWAP, fees and fee currency with their fill evidence. Apply the cached linear contract multiplier to cycle PnL; leave unconverted fees unknown and funding bills separate from pair PnL. Do not infer account balance or position from strategy logs.

For shared sparse-event rules, read [private feed reconciliation](../../kolabi-market-feeds/references/private-feed-reconciliation.md). For financial reporting, read [run reporting](../../kolabi-run-analysis/references/run-reporting.md).
