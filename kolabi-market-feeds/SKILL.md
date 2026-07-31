---
name: kolabi-market-feeds
description: "Use when work touches kolabi public or private feed ingestion, private payload reconciliation, feed-derived order or account visibility, sparse cancel or fill events, balance/noise suppression, and operator action logging driven by websocket events."
---

# Kolabi Market Feeds

Treat feeds as state evidence. Preserve useful operator visibility while suppressing noisy balance or notice chatter unless the user asks for it.

## Avoid When

- The task is a pure reducer/runtime transition; use `kolabi-bot-runtime`.
- The task is only CLI construction or packaging; use `kolabi-kraken-futures`.
- The user asks for historical exchange docs rather than the local adapter behavior.

## Workflow

1. Capture the exact payload shape or local log evidence.
2. Identify whether the source is public feed, private feed, REST fallback, or canonical account state.
3. Normalize sparse deltas without losing raw evidence needed for debugging.
4. Keep account/order visibility consistent across feed and command surfaces.
5. Add tests or replay fixtures for the payload shapes that caused the issue.

## Routes

- **Private payloads**: read [private feed reconciliation](references/private-feed-reconciliation.md).
- **Public feed handling**: read [public feed handling](references/public-feed-handling.md).
- **Operator logs**: read [operator logging](references/operator-logging.md).

## Output Expectations

Report payload shapes handled, visibility or logging changes, tests or fixtures added, and any intentionally suppressed noisy feed output.
