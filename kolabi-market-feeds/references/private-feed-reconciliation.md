# Private Feed Reconciliation

Use this reference when sparse private events, uncertain REST outcomes, or trigger conversions leave an order's state unclear. Follow evidence through the account normaliser, typed event, reducer, and Chronos family state; Kraken endpoint details belong in [Kraken order reconciliation](../../kolabi-kraken-futures/references/order-reconciliation.md).

## Identity And Sparse Evidence

- Correlate exchange, product, environment/account, symbol, role, client/exchange order IDs, and runtime instance/generation. Preserve the original client ID across an authorised retry or status lookup; never match a new attempt solely by its reused source-row name.
- Merge sparse deltas with the matching canonical state. Missing quantity/status fields are unknown, not zero fill or cancellation. Preserve positive cumulative execution through a later cancellation of the remainder and deduplicate fills by their execution identity.
- A private trigger/conversion event establishes a trigger; it does not prove that the resulting child filled, failed, or closed. A stop-limit child may still rest on the book. Stop-price amendments cease after confirmed trigger evidence; do not resume them simply because that child is live.
- A positive fill can establish a previously missing conditional trigger. Public mark/last/index crossings alone cannot establish real private execution. Keep exchange event time, local receive time, persistence time and lookup time distinct when diagnosing lag.
- Normalise currency-bucket balance payloads independently of order evidence. Retain only the raw fields needed to explain the mapping; avoid credential or full account-payload dumps.

## Uncertain Outcomes And Family Holds

An ambiguous placement response, transport interruption, unresolved trigger, missing amendment target, or repeated amendment rejection needs bounded read-only verification through the existing route/account. An order absent from open orders, a truncated history scan, or an old placement event does not establish a current terminal outcome. Missing evidence leaves the result unknown and cannot justify a replacement or a blind placement retry.

Hold only the affected family while reconciliation is pending or unresolved. Keep cancellations available, preserve queued work and reserved successors without executing held admissions, and allow unrelated families to progress. Keep the exact reconciling instance until its outcome is resolved; pruning it as idle can lose fills, capacity reservations or successor ownership. Later authoritative private evidence may release the hold. Never drop reduce-only or create a compensating order to make uncertain state appear resolved.

Use `ORDER_RECONCILIATION_PENDING`, `ORDER_RECONCILIATION_CHECK`, `ORDER_RECONCILED`, and `ORDER_RECONCILIATION_UNRESOLVED` to trace the local state machine. Report which identity, role and reason was held and what evidence resolved it. A completed verification request is not by itself a resolved order.

## Focused Verification

Replay the failing payload and late/duplicate variants before using any live command. Cover sparse trigger versus child fill, partial fill then remainder cancellation, delayed results from an obsolete attempt, unknown placement without resubmission, bounded-history exhaustion, and authoritative evidence arriving after an unresolved hold. Assert that the affected family's new execution remains blocked, unrelated families progress, known-order cancellation remains possible, and reserved successors survive reconciliation/pruning. PostgreSQL-dependent account tests need an isolated test database; a missing DB service is an infrastructure failure, not evidence that the normaliser is wrong.
