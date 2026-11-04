# Kraken Order Reconciliation

Use this reference for the local Futures implementation in `kolabi/shared/exchanges/kraken_reconciliation.py`, `kraken_adapter.py`, and the typed `VerifyOrderCommand`/`OrderVerificationResult` contract. Read [private feed reconciliation](../../kolabi-market-feeds/references/private-feed-reconciliation.md) for identity, trigger and family-hold invariants; keep exchange-specific request details here.

## Bounded Evidence Sources

The current adapter checks `/orders/status` for the requested exchange ID or original client ID, then matching `/openorders` evidence and deduplicated `/fills` since the attempt. Full cumulative fills can establish completion when the requested quantity is known. Historical fallback scans `/api/history/v3/orders` and `/api/history/v3/triggers`, newest first, at most two pages of 100 entries per endpoint per check. Check the implementation before changing these bounds or pagination.

- Use the existing adapter for the exact route/environment/account; do not probe another account or product because an order is missing.
- Match the order identity and validate any supplied symbol. A status without quantity and cumulative execution evidence cannot be treated as a zero-fill terminal state.
- Trigger retirement is not cancellation of the child. The verifier rejects an unfilled `triggered`/`stopOrderTriggered` record as proof of termination.
- Historical placement/update events cannot prove that an order remains live now. The history fallback accepts authoritative terminal evidence; incomplete, empty or exhausted scans remain unknown.
- Preserve the source and lookup timestamps in evidence. Do not turn a transport error or missing row into a fabricated cancellation.

## Retry And Authentication Boundaries

Futures signing omits the optional nonce; Spot still uses its required nonce and separate signing path. In the current Futures request helper, explicit `nonceBelowThreshold`/`nonceDuplicate` rejections have a bounded retry budget (default at most three attempts), retaining the original request and client order ID. Reconciliation lookups explicitly use one request attempt. Distinguish this definite rejection from a timeout, transport failure or ambiguous placement response: those do not authorise blind `/sendorder` retries.

When changing authentication, inspect both bot and private-feeder call paths. A source edit does not update already running processes; deployment/restart belongs to the user's operational scope.

## Runtime Integration And Verification

The current runtime schedules verification at 0, 2 and 5 seconds subject to REST capacity, with a 30-second overall deadline. Confirm current policy constants when diagnosing timing. Exhausting the deadline leaves the affected family blocked, while later authoritative private evidence can resolve it. A repeated fault after one recovery blocks further automatic recovery for that order attempt; do not extend retries indefinitely.

Use adapter fixtures and `tests/bot/test_order_reconciliation.py` for exact-ID matching, missing quantities, triggered-but-unfilled children, duplicate fills, old placement history, pagination exhaustion, explicit nonce rejection with a stable client ID, and ambiguous placement without duplicate submission. Pair these with Chronos/repetition tests for retained successors and family-scoped blocking. Do not infer broad runtime health from adapter tests alone.
