# Run Reporting

Use this reference when summarizing Kolabi bot runs, especially stopped/current runs and terminated-pair checkpoints.

## Evidence And Strategy Attribution

- Use canonical DB/order rows for persisted identities, fills and fees, and runtime logs for attempts, amendments, clocks, gates and accepted strategy snapshots. Compare exact identities and source times when authoritative exchange evidence disagrees with stale local state; a UI display alone cannot settle the discrepancy.
- Attribute each attempt to its accepted revision and effective parameters using `STRATEGY_BEGIN/PAIR/END`, `STRATEGY_ACCEPTED/REJECTED`, and instance records. Preserve source path, digest, effective time, family, instance and generation when present. A rejected candidate never becomes the active strategy.
- A run can contain multiple revisions, and flying attempts can retain an earlier revision after acceptance of a new one. Do not split a run at every `STRATEGY_BEGIN` or apply the latest row retroactively to all attempts. Include the revision in mixed-revision tables or adjacent attempt details.
- Current Org contents are comparison material only, even if the filename matches the logged source. If the accepted snapshot is missing, state the attribution gap rather than reconstructing it from today's file. Historical logs that omit a price-unit prefix cannot establish that prefix from the current strategy.
- Use the existing `scripts/kolabi-run-report` and inspect its current help before adding custom parsing. `--pair-regimes` adds parameter/attempt details; `--log-only` is appropriate when DB evidence is unavailable and leaves DB-only values missing. The optional `--strategy` file is explicitly labelled current-file context, not run evidence. See `strategy_snapshot.py` and `run_report.py` for versioned snapshot handling.

`HEAD_FILL` records head completion independently of tail state, including a head completed after an earlier partial fill already placed its tail. Keep its unrounded execution price, quantity and time. For older logs missing that transition, the DB-backed reporter can recover matching executions and terminal state only with consistent identities, quantities and timestamps inside the logged attempt; preserve its recovery/inconsistency notes. `--log-only` cannot recreate missing historical evidence. A `HEAD_ACK` deadline of `-` means no head deadline.

## Run Boundary

Before tabulating, identify:

- logged strategy source and log path, including whether an `orders/*.org` path resolves to a canonical file in `manalysis/strategies/`
- exchange, symbol, market type, environment, and account scope
- run start and stop time if visible
- whether the user intentionally stopped or cancelled the run
- whether the run is still live, partially live, or fully stopped

If the user asks for "current run only", exclude older attempts and stale DB rows unless explaining contamination.

## Market Maker Reporting Scope

- For a current MM status report, count executions and realised PnL from `MMBUY` and `MMSEL` unless the user requests a wider strategy scope. Show other families separately when needed to explain account exposure or an anomaly.
- Call a reconciled attempt with confirmed zero execution a "tentative expirée sans exécution" (or "expired without execution" in English). Preserve exact log event names such as `HEAD_TIMEOUT` as evidence, but do not present these attempts as losing trades or execution errors. Keep failed submissions, genuinely unresolved attempts and partial fills distinct.
- Query balance and position independently, with their own observation times and account scope. Label those figures account-wide; they cannot be attributed to the MM families merely because the run is current.

## Trigger, Fill, Cancellation And Vote Evidence

| Claim | Evidence and limits |
| --- | --- |
| Triggered | Exact private trigger/conversion evidence, or a positive fill establishing an inferred conditional trigger; virtual orders use explicit local trigger events. A public price crossing alone does not prove a real trigger. |
| Filled | Positive execution quantity for the exact order/attempt, with fill identity and price where available. A partial fill is not completion of the remaining quantity. |
| Cancelled or expired | Terminal evidence for the remaining quantity. Preserve earlier fills and exposure; cancelling a remainder is not a closing trade. A trigger record disappearing is not proof its child was cancelled. |
| Voted | The exact hook and `cFunc` evidence rule was satisfied. For `rns_quorum`, a first positive tail fill from a distinct family supplies a vote; a trigger, amendment or zero-fill cancellation does not. |
| Reconciled | Authoritative evidence resolved the identified role/order. A successful lookup, missing open-order row, or exhausted history scan alone does not establish a terminal outcome. |

Record whether a trigger was explicit or inferred. For quorum analysis, identify the selected prerequisite instances/generations, first qualifying fill times, policy validity window, and evidence available when the downstream head was admitted. Multiple clones of one family are not multiple quorum members. Keep order expiry from trigger and vote expiry from first positive fill separate, even when both use the same configured duration.

Report `execution_origin=virtual` confirmations separately from real executions. They contribute no exchange fees, account exposure or trading PnL. A strategy with virtual voters can still have real followers whose fills belong in the financial table.

## Terminated-Pair Table

For terminated pairs, use an Org table with compact headers. Common columns:

| Pair | Time | Hfill | Tfill | Amend | Hliq | Tliq | Delta | Gross | Net | Cum |

Column rules:

- `Pair`: pair name plus attempt/instance identity when available; add `Rev` or an adjacent revision mapping when accepted definitions differ within the run.
- `Time`: tail close/final event time; use head fill time only if tail time is missing.
- `Hfill` and `Tfill`: head and tail fill prices.
- `Amend`: `A` when the tail was amended advantageously before closing; blank otherwise.
- `Hliq` and `Tliq`: maker/taker status, usually `M` or `T`.
- `Delta`: signed price movement from head fill to tail fill in the strategy's expected direction.
- `Gross`: result before fees, with the instrument model and evidence quality retained.
- `Net`: result after observed or explicitly estimated fees; missing fee evidence can leave net unavailable.
- `Cum`: running cumulative net or gross, clearly label which one is used.

Avoid horizontal separator clutter when the user asks for compact Org output. Align columns for terminal readability.

## Calculations

- For buy-head/sell-tail cycles, positive delta normally means `tail_fill - head_fill`.
- For sell-head/buy-tail cycles, positive delta normally means `head_fill - tail_fill`.
- Use `kolabi/bot/run_report_finance.py` for the current model. Linear PnL multiplies signed price delta by matched quantity and the instrument contract multiplier. Inverse PnL uses reciprocal entry/exit prices, preserves native base-currency PnL and converts to a USD equivalent at fill prices. Do not apply the simple linear formula to every product.
- Preserve exact, estimated, assumed and unavailable evidence labels. An unsupported model leaves finance unavailable; insufficient route/multiplier evidence must not silently become an exact linear result. Subtract observed fees where available; estimate only under explicit report options and label the rate/currency conversion used. Missing fees are not zero fees.
- ROI is return on entry notional, not on margin or leveraged capital. The report excludes funding, financing and unrelated account-ledger adjustments. Keep realised matched cycles, partial fills, remaining exposure and the account ledger distinct when explaining why winning reported cycles do not account for the whole balance change.
- Cumulative values must use the same basis row to row. Do not mix gross and net in one `Cum` column.

## Maker/Taker And Slippage

- Use actual fill/fee evidence for maker/taker attribution. If it conflicts with post-only or `!` intent, inspect the accepted revision, translated payload, acknowledgements and amendments; preserve the discrepancy instead of assuming a cause.
- Negative gross after an amendment can happen when the trigger moved but the executable limit stayed stale, when slippage crossed the stop/limit range, or when the wrong side/sign was used in the strategy line.
- For stop-limit tails, check whether both trigger and limit price were updated. Updating only the trigger can leave the limit stale.
- Compare the selected mark/last/index trigger source with the executable bid/ask at fill time, including tick rounding and data age. One-minute candle extrema cannot establish the exact live intraminute path, queue priority or latency. Separate exchange time, local receive/persist time and REST lookup time before claiming a slow trigger or missed fill.

## Anomaly Checklist

Check these before proposing code changes:

- parser errors from old field names, missing required Org columns, inherited properties, or empty CLI values
- an attempt retaining an earlier accepted revision, or a rejected reload leaving the previous revision active
- repeated heads explained by an explicit trigger/fill repeat condition, versus unintended duplicate execution
- cancellation compared with the attempt's resolved `hp`/`ht`/`tp`/`tt` clock, first placement/trigger time, and retirement reason; use [timeouts and repetition](../../kolabi-bot-runtime/references/timeouts-and-repetition.md)
- tail trigger on the wrong mark/last/index signal
- fill price inconsistent with expected side or tick offset
- DB locks or skipped telemetry/audit rows
- UI-visible orders that are stale, already cancelled, or display artifacts
- `ORDER_RECONCILIATION_PENDING`, `ORDER_RECONCILIATION_CHECK`, `ORDER_RECONCILIATION_UNRESOLVED`, and `ORDER_RECONCILED` evidence explaining a held family, retained successor, or delayed admission; absence from an open-order list is not a fill or cancellation

## Chain-Gated Legs

- Read the accepted hook expression first: `-ht`, `-tt`, `-hf`, `-tf`, and close/cancellation hooks require different evidence. A trigger-based chain can release before a tail fill; a fill-based quorum cannot.
- `-tuf` needs new positive tail execution after that attempt's runtime unblock. A historical fill reappearing in a later snapshot cannot retroactively qualify. Read [seeded cycles](../../kolabi-bot-runtime/references/seeded-cycles.md) before interpreting circular activation.
- Trace `CycleSignalAccepted` and `CycleSignalDiscarded` by source instance/attempt, condition, destination and reason. An accepted offer is not a fill; a busy, cooling or inadmissible destination discards an offer rather than saving it for later. Compatible reloads preserve consumed signals. Report waiting/no-new-signal, busy, held, discarded and completed states from evidence rather than inferring them from the current strategy graph alone.
- Narrow release evidence to exact prerequisite instances, generations and timestamps. `LEASE_CLOSED` followed by `CHAIN_READY` can explain a close-gated path when present, but is not a universal sequence for every hook.
- Check for `COOL`, `cooldown`, or `ORDER_SAFETY_BLOCKED` in the decisive window, but do not infer a cooldown block when those markers are absent.
- Prefer tight `nl -ba log | sed -n ...` slices once broad `rg`/`awk` searches become noisy.

## Report Shape

1. Scope: logged strategy revisions, log, run window, exchange, symbol, environment, and any attribution gaps.
2. Terminated-pair table.
3. Still-live or unresolved pairs and virtual confirmations, in separate sections when relevant.
4. Anomalies and likely causes, separated from confirmed facts.
5. Suggested next check or fix only after the evidence is clear.
