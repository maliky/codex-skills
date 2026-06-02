# Order Contract

Use this reference when updating Kraken Futures order support or adapter signatures.

## Current durable expectations

- The useful exchange-facing order surface includes:
  - limit
  - market
  - stop loss
  - stop loss limit
  - take profit
  - take profit limit
  - trigger entry as market or limit
- Trailing-stop behavior may exist, but the user explicitly treats some trailing behavior as strategy-managed rather than a central exchange contract.

## Rules

- Enumerate supported order types explicitly in code or docs.
- Keep stop and trigger fields separate from plain price fields.
- Do not pass adapter kwargs that the adapter signature does not accept.
- If an order family is intentionally unsupported or strategy-managed, document the boundary instead of faking support.

## Smoke-path lesson

Recent failures showed a broad smoke command can fail every order family for the same reason when a shared unsupported field is threaded into all calls. Fix the shared contract mismatch first before debugging individual order types.
