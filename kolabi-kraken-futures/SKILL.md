---
name: kolabi-kraken-futures
description: "Use when building, debugging, or operating the local kolabi Kraken Futures workflow, including CLI behavior, order contracts, uncertain order reconciliation, bounded status/history lookups, cancel/close/list operations, smoke probes, and packaging fixes."
---

# Kolabi Kraken Futures

Work from the repo's actual CLI grammar and order contract. Prefer concrete smoke commands and local code evidence over generic exchange advice.

## Avoid When

- The task is internal reducer/runtime design; use `kolabi-bot-runtime`.
- The task is only websocket payload normalisation or feed logging; use `kolabi-market-feeds`. Use both skills when private evidence and Kraken REST verification interact.
- The request concerns a different exchange adapter unless the Kraken path is the comparison baseline.

## Workflow

1. Confirm the checkout, branch, package install state, and relevant CLI entrypoint.
2. Read the command grammar and examples before constructing commands.
3. Trace intent through CLI parsing, order building, runtime command generation, and adapter calls.
4. Prefer bounded smoke/probe commands before live operations.
5. Keep operator safety explicit for cancel, close, and market actions.

## Routes

- **CLI and operations**: read [cli and operations](references/cli-and-operations.md).
- **Order contract**: read [order contract](references/order-contract.md).
- **Uncertain placement, triggered children, missing amendment targets, or nonce rejection**: read [order reconciliation](references/order-reconciliation.md).
- **Packaging/install fixes**: read [packaging and cleanup](references/packaging-and-cleanup.md).
- **Runtime overlap**: read [runtime boundaries](references/runtime-boundaries.md) before moving behavior across layers.

## Output Expectations

Lead with the exact command or code path when asked, then report assumptions, safety constraints, tests or probes run, and any branch/remote details relevant to deployment.
