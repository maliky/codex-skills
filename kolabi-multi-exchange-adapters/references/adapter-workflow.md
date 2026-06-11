# Adapter Workflow

Use this reference when planning or implementing Binance, BitMEX, Kraken, or another kolabi derivatives adapter.

## Boundaries

- Keep core runtime behavior exchange-neutral: state, events, commands, pair lifecycle, and tail rules belong outside adapter code.
- Keep adapter code responsible for auth, product discovery, symbol mapping, precision, exchange payloads, response normalization, and REST or websocket client details.
- Use Kraken Futures as a baseline for local command shape, order contract expectations, and safety checks, but do not copy Kraken-only semantics into a generic layer.
- Keep the DB as the shared source of account, order, and feed-derived state. Avoid in-memory exchange side paths that make later reconciliation ambiguous.

## Capability Checks

Before changing code, identify the target exchange support for:

- perpetual or futures product naming and settlement currency
- market, limit, stop, reduce-only, post-only, and trigger orders
- quantity, price, tick, and minimum-notional precision
- client order ids, idempotency, cancel semantics, and close-all support
- public feed, private order feed, fills, balances, and sparse cancel events
- sandbox, demo, or testnet differences from production

## Implementation Procedure

1. Locate current adapter interfaces, typed order contracts, CLI grammar, and feed normalization paths.
2. Add capability evidence near the adapter boundary, not as scattered special cases in runtime code.
3. Convert exchange responses back into the existing kolabi event/account/order vocabulary.
4. Keep errors actionable for operators: include exchange, product, symbol, command kind, and adapter error.
5. Add tests around contract conversion and payload normalization before relying on live smoke checks.

## Review Questions

- Does the change preserve `State + Event -> State + Commands` ownership?
- Does the adapter expose enough capability detail for the CLI or TSV layer to reject unsupported requests early?
- Does private/public feed reconciliation still have raw evidence for debugging?
- Can the same MWE be run against another exchange by changing exchange configuration rather than rewriting strategy code?
