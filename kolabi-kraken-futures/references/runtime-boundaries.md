# Runtime Boundaries for Kolabi Runtime Work

Use this reference when Kraken Futures work crosses into runtime or command-generation boundaries.

## Scope

- `StrategyRuntime` should stay as a pure state transition engine.
- `Chronos` should own event timing and orchestration.
- `Ogun` should remain the command executor and side-effect boundary.
- CLI work should map cleanly to this boundary map without introducing new runtime states.

## Boundaries Checklist

- Confirm a change belongs in runtime, not in command-line parsing.
- Keep state mutation inside the runtime transition layer.
- Keep API side effects and order execution in command handlers.
- Keep bot shutdown and cancel-on-interrupt behavior in the coordinator layer, not in domain transitions.

## Escalation

- If the issue is mostly typed transitions, move to `kolabi-bot-runtime`.
- If the issue is mostly orderbook/feed visibility, move to `kolabi-market-feeds`.
