# Public Feed Handling

Use this reference when public feed behavior makes order or market visibility look stale or out of sync.

- confirm channel subscription list
- validate event order for open orders and trigger orders
- avoid changing local strategy state when only transport timing is the issue
- if needed, keep public feed handling in a minimal reproducible event window
