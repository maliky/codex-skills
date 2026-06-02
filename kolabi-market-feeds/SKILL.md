---
name: kolabi-market-feeds
description: Use when work touches `kolabi` public/private feed ingestion, private payload reconciliation, feed-derived order/account visibility, or operator action logging driven by feed events.
metadata:
  author: local-codex
  maturity: draft
---

# Kolabi Market Feeds

Use this skill when the task is about how kolabi observes the market and account state through websocket feeds and feed-derived logs.

This skill is for:
- debugging public websocket feed subscriptions and missed messages
- debugging private/account websocket payload interpretation
- reconciling private feed deltas with canonical persistent state
- adding or validating compact operator-facing action/notification logging
- diagnosing feed-driven mismatches before touching strategy rules

This is not for:
- command surface redesign (use `kolabi-kraken-futures`)
- runtime transition refactor (use `kolabi-bot-runtime`)
- exchange credential setup unless feed behavior is blocked by auth context

## Workflow

1. Identify feed family.
   - public feed debugging
   - private/account feed debugging
   - private-notice or action-log debugging

2. Validate message contracts.
   - inspect payload shape differences between stream and persistence
   - check for missing fields (`is_cancel`, `balances`, order ids, trigger markers)
   - prefer enrichment against canonical state for sparse payloads

3. Reconcile feed-derived state.
   - verify whether missing fields are expected or a subscription gap
   - preserve command-side safety assumptions and do not infer ownership from sparse deltas
   - keep feed-driven status views deterministic and human-readable

4. Check subscription and coverage.
   - confirm active channels cover symbols and instrument families in use
   - confirm message cadence for open orders, trigger orders, and private balance updates
   - verify no hidden duplication from multiple handlers

5. Improve operator visibility.
   - keep logs compact and action-oriented
   - include clear origin, key id, status, and command intent
   - avoid verbose balance chatter unless explicitly asked

6. Verify with bounded runtime/CLI observations.
   - run minimal commands that confirm feed observations align with visible open-order state
   - keep the verification surface minimal and reproducible

## Preferred Routes

### Public feed diagnostics

- Start by reading:
  - [public feed handling](references/public-feed-handling.md)

- Default route:
  1. identify missing or reordered events
  2. inspect subscription list and symbol filters
  3. confirm feed cadence against command output snapshots

### Private feed and feed-to-state reconciliation

- Start by reading:
  - [private feed reconciliation](references/private-feed-reconciliation.md)

- Default route:
  1. check sparse delta behavior
  2. enrich with canonical order state where needed
  3. verify feed-derived status maps only after enrichment

### Feed logging and action traces

- Start by reading:
  - [operator action logging](references/operator-logging.md)

- Default route:
  1. identify missing action categories
  2. add compact operator traces for visibility-critical paths
  3. avoid noisy status lines that reduce signal

## House Rules For This Host

- Keep feed changes observable without requiring broad runtime introspection.
- Do not claim feed correctness from sample output alone; reconcile by multiple channels.
- Preserve log brevity and compactness.
- Treat private feed payloads as potentially sparse and canonicalize before surfacing.

## Deliverables

- list of confirmed feed channels and coverage gaps
- action log update strategy if visibility was changed
- explicit payload mismatch items and expected fallback behavior
- any side effects on `Kolabi` command confidence from feed corrections

## References

- [public feed handling](references/public-feed-handling.md)
- [private feed reconciliation](references/private-feed-reconciliation.md)
- [operator logging](references/operator-logging.md)
