---
name: kolabi-kraken-futures
description: "Use when building, debugging, or operating the local kolabi Kraken Futures workflow, including CLI behavior, order contracts, smoke or probe commands, cancel/close/list operations, editable installs, packaging fixes, and command-surface maintenance."
---

# Kolabi Kraken Futures

Work from the repo's actual CLI grammar and order contract. Prefer concrete smoke commands and local code evidence over generic exchange advice.

## When to Use

- Build or debug Kraken Futures CLI commands and operator workflows.
- Fix order-contract alignment between CLI, runtime, and Kraken adapter calls.
- Investigate `open-orders`, `trigger-orders`, `cancel-all`, `close-all`, or `run-once`.
- Repair editable installs, package entrypoints, or command-surface cleanup.

## Avoid When

- The task is internal reducer/runtime design; use `kolabi-bot-runtime`.
- The task is feed reconciliation or logging from websocket payloads; use `kolabi-market-feeds`.
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
- **Packaging/install fixes**: read [packaging and cleanup](references/packaging-and-cleanup.md).
- **Runtime overlap**: read [runtime boundaries](references/runtime-boundaries.md) before moving behavior across layers.

## Output Expectations

Lead with the exact command or code path when asked, then report assumptions, safety constraints, tests or probes run, and any branch/remote details relevant to deployment.

## References

- [cli and operations](references/cli-and-operations.md)
- [order contract](references/order-contract.md)
- [packaging and cleanup](references/packaging-and-cleanup.md)
- [runtime boundaries](references/runtime-boundaries.md)
