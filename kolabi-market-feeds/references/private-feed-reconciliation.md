# Private Feed Reconciliation

Use this reference when private feed payloads lose fields or create false status differences.

## Likely gaps

- trigger or cancel deltas can be sparse
- order id references can be duplicated across streams
- balance payloads can arrive as currency buckets requiring normalization

## Procedure

1. normalize sparse payloads against canonical order state
2. avoid making strong status claims from one message only
3. validate any changed state path with one bounded runtime command
