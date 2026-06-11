# Live Runtime Lessons

Use this reference when live or demo kolabi runs expose readiness, tail, stale-order, or operator-log behavior.

## Readiness And Gate Waiting

- Keep `GATE_WAIT` and similar readiness waits configurable. The recent live-test preference was a five-minute gate interval, but avoid hardcoding that unless the surrounding runtime already treats it as policy.
- Do not mark a pair ready only because one feed is quiet. Require enough public/private or canonical DB evidence to trust the runtime state.
- When a live run stalls, distinguish exchange unavailability, sparse private payloads, missing account state, and genuine strategy gating.

## Latent Heads And Tail Updates

- Treat latent heads as state requiring explicit evidence before generating follow-up orders.
- A tail update should unblock when private events or canonical account state prove the relevant order state changed.
- Stale stop or tail orders should be cancelled through runtime-mediated commands, not direct adapter shortcuts.
- Preserve no-widen and directional stop constraints when amending tails.

## Operator Logs

- Keep logs compact enough for live monitoring, but include a legend or stable event names for order lifecycle, readiness gates, feed deltas, and admin actions.
- Suppress repeated balance/noise chatter unless it changes an operator decision.
- When reporting a live test, include the exact run command, DB/env labels, relevant order ids, and cleanup status.

## Verification

Prefer bounded live/demo probes, replay fixtures, or targeted command-log checks over broad unattended runs. Validate both the generated commands and the resulting state transitions.
