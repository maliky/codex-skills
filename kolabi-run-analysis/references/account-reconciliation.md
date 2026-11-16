# Prices, Positions And Account Reconciliation

Use for a financial balance sheet, wallet/position evolution, or an explanation of account losses alongside winning pairs. Use [portfolio comparison](portfolio-comparison.md) only for the separate counterfactual that fixes prices at startup. Collect evidence read-only: a reporting request does not authorize order recovery writes, cancellations, closing positions or restarting a service. In particular, inspect current help before using an operator named `snapshot`; a pause/restart snapshot command may stop a bot and cancel orders.

## Evidence And Baseline

- Identify exchange, environment, account scope, current run boundary and timezone. Use fresh, complete account observations for current holdings, wallet currencies, positions and open orders; query these independently of bot logs and label each observation time. A partial WebSocket update or missing row does not establish a flat position or zero balance.
- Prefer an actual opening account snapshot. If it has expired, reconstruct from venue ledger/fills only to the extent supported and mark the opening state reconstructed, with its effective time and gaps. Never present a pre-first-fill reconstruction as an atomic run-start observation. Identify opening inventory and open orders, including activity from earlier revisions or outside the bot.
- Use the order database for exact execution identities and the account database/venue ledger for wallets, positions and cash movements. Match every family, generation and attempt before pairing heads and tails; repeated names do not prove duplicate orders. Use the current accepted revision for current strategy status and retain earlier revisions on existing attempts.
- For OKX, read [contracts and evidence](../../kolabi-okx-futures/references/contracts-and-evidence.md) and its operator workflow before constructing commands. For Kraken, read [CLI and operations](../../kolabi-kraken-futures/references/cli-and-operations.md). Keep shared evidence rules in those skills rather than inventing adapter-specific flags here.

## Price And Quantity Meanings

Keep execution VWAP, aggregate position average entry, mark, last, bid/ask and startup reference prices distinct, with their source times. A trigger/reference price is not a fill price. Missing accepted execution cost must stay unknown, not be replaced by a public quote or an earlier partially covered cost. Explain the intended valuation price and FX rates before calculating a comparison.

Use signed quantities and the instrument's linear/inverse payout model, multiplier and native units. Contracts are not necessarily units of the underlying asset. Leverage and notional are not owned wallet cash. Show each wallet currency's total/available amount and valuation; keep available trading collateral, reserved margin, equity, and funding/Earn wallets distinct. Do not infer collateral eligibility from a non-USD holding or add USD-equivalent totals to the underlying currency balances again.

## Reconcile The Account First

Show opening and closing wallet balances by currency, positions with signed quantity and entry basis, open-order counts, valuation prices, unrealised PnL and total equity. Separate observed values from estimates or reconstructed values.

Normalize the venue's equity and ledger definitions, then bridge opening to closing equity with external deposits/withdrawals/transfers, realised PnL, the change in unrealised PnL, fees/rebates, settled or accrued funding and FX/other adjustments. Count each item once: wallet changes can already include settled fees and funding, and some equity fields already include unrealised PnL. Reserved margin normally affects availability, not a second loss of equity. Show both raw equity change and flow-adjusted trading change when external cash moved. Display any residual and its evidence limitations rather than forcing equality by inventing an adjustment.

## Family And Attempt View

Use one row per requested family with matched quantity/net cycle result, unmatched head/tail quantity and marked exposure, observed attributable fees/funding, rejected or unresolved exits, and evidence quality. Give the denominator: all attempts, executed attempts, completed matches, partials and still-open/unresolved attempts. Keep confirmed zero-fill expiries separate from losses. Use weighted fills, matching quantities and both legs' fees; do not multiply a final quote by all executions.

Matched-cycle profit and the venue's realised inventory PnL are alternative decompositions, not additive gains. Attribute pre-existing inventory, cross-family matching, manual trades and funding only where identities and accounting evidence support it. Keep unattributed inventory and account residuals visible; a family table need not fully allocate the account. Clearly distinguish the account equity bridge, cycle economics, and any hold-inventory counterfactual.

## Synthetic Accounting Check

For a linear unit-multiplier contract, start long four units at 1,000. Sell one at 900, then buy one at 800 and value all holdings at 800, ignoring fees/funding. The sale realises -100; the final four units have average entry 950 and unrealised PnL -600. Total equity change is -700. Holding four throughout would give -800, so the sell/buyback improved the outcome by +100 despite the realised loss. Do not add that +100 again to the account bridge, or treat the lower average entry as another economic loss. It is a synthetic explanation, not a venue balance or a trading recommendation.

Also check short/flip and partial-fill cases, fees in another currency, deposits, funding already included in cash, missing opening inventory, stale snapshots and unknown fees. Leave unsupported results unavailable. Read-only inspection must never turn into a live order probe to make an accounting example complete.
