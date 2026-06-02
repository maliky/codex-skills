# Tail Tracking and Tail Trail State

Use this reference when implementing or debugging tail lifecycle, no-widen behavior, or tail command generation.

This reference summarizes durable tail concerns for the kolabi runtime.

- Keep tail references stable across state transitions.
- Preserve rule of no widening when constraints apply.
- Preserve directional constraints for stop-style updates.
- Use `TAIL_SUBMITTED` and trailing states consistently.
- Distinguish strategy-local intent from exchange-native orders.

## Practical Checklist

- validate living-tail cleanup on interrupt paths
- validate `cancel-living-tails` behavior after partial fills
- validate `MARKET_TICK` and `AMEND_TAIL` gating when referenced
- validate any new path by bounded replay or targeted command log checks
