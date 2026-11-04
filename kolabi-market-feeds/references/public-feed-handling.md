# Public Feed Handling

Use this reference for public market data, persisted snapshots and connection recovery. Open orders, conditional children, fills and account balances require [private feed reconciliation](private-feed-reconciliation.md).

## Price Freshness And Route Identity

- Check subscribed instruments/channels, exchange/product/environment route, event ordering, and venue, receive and persistence times. Book bid/ask, last, mark and index observations have independent timestamps; a fresh ticker does not refresh an old book.
- Trace subscription, persistence and consumer snapshots separately. A quiet transport, slow DB query, stale cached view and strategy gate are different causes. Snapshot age must continue increasing when polling stalls; preserve the runtime's deferral behaviour for missing or stale evidence.
- Keep prices tied to the exact route and selected reference. A public price crossing cannot prove a private order trigger or fill.

## Database Reads And Recovery

The latest-snapshot query must constrain the route and apply deterministic timestamp/identity ordering with SQL `LIMIT 1`. Calling `.first()` after executing an unbounded select does not itself bound the database result. Inspect the current Kraken `latest_snapshot` implementation and shared persistence engine factory before changing this path.

`pool_pre_ping` replaces dead idle PostgreSQL connections when checked out of the pool. It does not replay interrupted transactions, make uncertain writes safe to retry, or fix disk exhaustion. Diagnose storage, server restart and transaction failure separately; do not purge data or restart all feeders to mask a stale connection.

For changes, test route isolation, equal-timestamp ordering, bounded rows and dead-connection replacement against a disposable database. Terminate only test connections when reproducing failures; do not probe recovery by disrupting live account or market DBs.
