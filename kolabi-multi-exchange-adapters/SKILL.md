---
name: kolabi-multi-exchange-adapters
description: "Use for kolabi cross-exchange adapter work: Binance, BitMEX, Kraken, demo/live setup, DB-backed exchange switching, adapter comparisons, Org strategy and CLI grammar, virtual order types, and price or quantity units."
---

# Kolabi Multi-Exchange Adapters

Use this skill for Kolabi adapter contracts and typed Org or CLI strategy inputs. Keep the runtime exchange-neutral, and put exchange-specific auth, symbols, payloads, precision, and API behavior inside adapters.

## Default Workflow

1. Confirm the active checkout, branch, target exchange, and whether the task is demo, sandbox, or live.
2. Read the local repo instructions and the Kraken path as the comparison baseline before changing a new adapter.
3. Map the requested behavior through the exchange-neutral contract: Org strategy or CLI input -> typed order intent -> runtime command -> adapter payload -> feed reconciliation. Virtual orders execute in the local state/event core and never reach the exchange adapter.
4. Keep derivatives/perpetual assumptions explicit unless the user asks for spot or another product family.
5. Preserve DB-grounded architecture for each platform from day one; do not add a side path that bypasses persistence or typed runtime boundaries.
6. Verify parser and materialisation changes with focused offline tests or replay; use a bounded demo or smoke order only within the authorised execution scope.

## Routes

- **Adapter design or review**: read [adapter workflow](references/adapter-workflow.md).
- **Org strategies, virtual types, units, or demo runs**: read [strategy grammar and demos](references/strategy-grammar-and-demos.md).

## Output Expectations

Report the target exchange, environment, branch, command or strategy path, adapter boundary touched, tests or smoke probes run, and any live-operation risk that remains.
