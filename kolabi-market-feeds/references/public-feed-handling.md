# Public Feed Handling

Use this route when order visibility looks stale or out-of-sync with public channels.

- confirm channel subscription list
- validate event order for open orders and trigger orders
- avoid changing local strategy state when only transport timing is the issue
- if needed, keep public feed handling in a minimal reproducible event window
