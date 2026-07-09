# Live Runtime Lessons

Use this reference when live or demo kolabi runs expose readiness, tail, stale-order, or operator-log behavior.

## Readiness And Gate Waiting

- Keep `GATE_WAIT` and similar readiness waits configurable. The recent live-test preference was a five-minute gate interval, but avoid hardcoding that unless the surrounding runtime already treats it as policy.
- Do not mark a pair ready only because one feed is quiet. Require enough public/private or canonical DB evidence to trust the runtime state.
- When a live run stalls, distinguish exchange unavailability, sparse private payloads, missing account state, and genuine strategy gating.
- Fresh-run requests often mean stopping bot/listener processes, purging local runtime DB files, and restarting only the services needed for the named strategy. Do not start every exchange DB when the strategy only targets one exchange or pair.
- Before live operation, report the selected DB/env labels, current position, current price, and whether open orders exist. Keep live cleanup explicit: cancel orders through the runtime path, and avoid closing positions unless the user asks.

## Latent Heads And Tail Updates

- Treat latent heads as state requiring explicit evidence before generating follow-up orders.
- A tail update should unblock when private events or canonical account state prove the relevant order state changed.
- Stale stop or tail orders should be cancelled through runtime-mediated commands, not direct adapter shortcuts.
- Preserve no-widen and directional stop constraints when amending tails.
- For repeated orders, keep `pause`, `tOut`, visibility/pruning, and pair concurrency distinct. A visibility timeout that is too short can cancel or recycle orders far earlier than the strategy's `tOut`.
- If a run appears to execute only one pair, check strategy parsing and runtime scheduling before changing exchange adapters. The runtime should handle as many pairs as the strategy defines.
- Interpret `cancel-all` output against canonical state and the exchange response shape. A response listing already-canceled orders does not prove those orders were still live on the book.

## Adaptive Strategy Functions

- Keep strategy helper code in the existing helper modules when they already express repeated pairs or row expansion; avoid creating a parallel helper layer for one strategy file.
- For ROI-driven tuning, distinguish timeout outcomes from positive or negative pair ROI before changing `tOut`, `hPrice`, or quantity.
- Use short strategy-call names when the Org/TSV row is dense, but keep the Python function names specific enough to expose the behavior.
- When tuning variants such as S1/S3/S4, update the small strategy fixture first and verify the generated rows before broadening to a live file.

## Operator Logs

- Keep logs compact enough for live monitoring, but include a legend or stable event names for order lifecycle, readiness gates, feed deltas, and admin actions.
- Suppress repeated balance/noise chatter unless it changes an operator decision.
- When reporting a live test, include the exact run command, DB/env labels, relevant order ids, and cleanup status.
- Do not print DB URLs, passwords, API keys, or private pending payload dumps. When debugging private feeds, report counts, order ids, client ids, status changes, and the minimum fields needed to explain the operator decision.
- If the user cancelled the bot intentionally, do not treat the abrupt end as a failure. Focus the report on order timing, placement, amendments, cancellations, and cleanup state.

## Verification

Prefer bounded live/demo probes, replay fixtures, or targeted command-log checks over broad unattended runs. Validate both the generated commands and the resulting state transitions.
