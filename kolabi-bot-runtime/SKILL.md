---
name: kolabi-bot-runtime
description: "Use when work touches typed kolabi runtime internals, including state-event-command transitions, pair-cycle lifecycle, tail tracking, Chronos dedupe, StrategyRuntime boundaries, Horus command generation, or Ogun execution boundaries."
---

# Kolabi Bot Runtime

Keep runtime work inside typed state transitions and explicit command boundaries. Separate domain decisions from adapter calls and operator-facing CLI behavior.

## When to Use

- Change reducer state, event handling, command generation, or lifecycle transitions.
- Debug tail tracking, market-tick reactions, or no-widen tail semantics.
- Adjust Chronos dedupe, StrategyRuntime flow, Horus translation, or Ogun execution boundaries.
- Review whether a behavior belongs in the reducer, runtime coordinator, CLI, or exchange adapter.

## Avoid When

- The request is only about Kraken CLI usage or operator commands; use `kolabi-kraken-futures`.
- The request is only feed parsing or account visibility; use `kolabi-market-feeds`.
- The user asks for a one-off shell command rather than code changes.

## Workflow

1. Locate the active checkout and confirm the branch before changing runtime code.
2. Map the request onto `State + Event -> State + Commands`.
3. Keep pure transition logic in reducer/domain helpers.
4. Let StrategyRuntime feed events, Horus translate intents, and Ogun execute commands.
5. Add focused tests around state transitions, generated commands, and lifecycle edge cases.

## Routes

- **State/event work**: read [state and event loop](references/state-event-loop.md).
- **Runtime placement**: read [runtime boundaries](references/runtime-boundaries.md).
- **Tail behavior**: read [tail tracking](references/tail-tracking.md).
- **Admin action safety**: read [admin action boundaries](references/admin-action-boundaries.md).

## Output Expectations

Report the runtime boundary touched, the state/event cases covered, tests run, and any operator-facing behavior that intentionally stayed unchanged.

## References

- [state and event loop](references/state-event-loop.md)
- [runtime boundaries](references/runtime-boundaries.md)
- [tail tracking](references/tail-tracking.md)
- [admin action boundaries](references/admin-action-boundaries.md)
