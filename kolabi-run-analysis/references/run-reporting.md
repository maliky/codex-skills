# Run Reporting

Use this reference when summarizing Kolabi bot runs, especially stopped/current runs and terminated-pair checkpoints.

## Source Order

- Prefer canonical DB/order state when available for final status, order ids, and fill rows.
- Use runtime logs for timing, attempts, amendments, tOut, gate waits, parser failures, and operator-visible event sequence.
- Use exchange REST or UI observations as witnesses, not sole truth, unless DB/log data is missing.
- Keep the strategy TSV close by, but do not assume a stopped run used the current file if the user says the running bot had an older TSV.

## Run Boundary

Before tabulating, identify:

- strategy file and log path, such as `orders/krf_ada.tsv`, `orders/bmm_ada.tsv`, `logs/bmm_ada.log`, or `bm_ada.log`
- exchange, symbol, market type, environment, and account scope
- run start and stop time if visible
- whether the user intentionally stopped or cancelled the run
- whether the run is still live, partially live, or fully stopped

If the user asks for "current run only", exclude older attempts and stale DB rows unless explaining contamination.

## Terminated-Pair Table

For terminated pairs, use an Org table with compact headers. Common columns:

| Pair | Time | Hfill | Tfill | Amend | Hliq | Tliq | Delta | Gross | Net | Cum |

Column rules:

- `Pair`: pair name plus attempt index when available.
- `Time`: tail close/final event time; use head fill time only if tail time is missing.
- `Hfill` and `Tfill`: head and tail fill prices.
- `Amend`: `A` when the tail was amended advantageously before closing; blank otherwise.
- `Hliq` and `Tliq`: maker/taker status, usually `M` or `T`.
- `Delta`: signed price movement from head fill to tail fill in the strategy's expected direction.
- `Gross`: approximate gross result before fees.
- `Net`: approximate result after fee estimate when ledger fees are unavailable.
- `Cum`: running cumulative net or gross, clearly label which one is used.

Avoid horizontal separator clutter when the user asks for compact Org output. Align columns for terminal readability.

## Calculations

- For buy-head/sell-tail cycles, positive delta normally means `tail_fill - head_fill`.
- For sell-head/buy-tail cycles, positive delta normally means `head_fill - tail_fill`.
- Gross in USD is approximately `delta * filled_qty` for linear contracts or spot-like quantity accounting. State if contract specs make this approximate.
- Net approximation should subtract maker/taker fee estimates for both legs. If exact fee rows are missing, say so and name the fee rate used.
- Cumulative values must use the same basis row to row. Do not mix gross and net in one `Cum` column.

## Maker/Taker And Slippage

- A limit order with post-only or `!` intent can still be reported as taker if it crossed, was repriced, or the exchange/fill evidence says it took liquidity. Trust fill evidence over intent.
- Negative gross after an amendment can happen when the trigger moved but the executable limit stayed stale, when slippage crossed the stop/limit range, or when the wrong side/sign was used in the strategy line.
- For stop-limit tails, check whether both trigger and limit price were updated. Updating only the trigger can leave the limit stale.

## Anomaly Checklist

Check these before proposing code changes:

- parser errors from shifted TSV columns or empty CLI values
- stale run using an older strategy file
- repeated heads without corresponding tail closes
- tail cancelled before expected `tOut`
- tail trigger on the wrong mark/last/index signal
- fill price inconsistent with expected side or tick offset
- DB locks or skipped telemetry/audit rows
- UI-visible orders that are stale, already cancelled, or display artifacts

## Report Shape

1. Scope: strategy, log, run window, exchange, symbol, environment.
2. Terminated-pair table.
3. Still-live or unresolved pairs, if relevant.
4. Anomalies and likely causes, separated from confirmed facts.
5. Suggested next check or fix only after the evidence is clear.
