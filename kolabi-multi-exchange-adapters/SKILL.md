---
name: kolabi-multi-exchange-adapters
description: "Use for kolabi cross-exchange adapter work: Binance, BitMEX, Kraken, demo/live setup, DB-backed exchange switching, adapter comparisons, MWE runs, and TSV or CLI grammar changes."
---

# Kolabi Multi-Exchange Adapters

Use this skill when kolabi work crosses exchange boundaries. Keep the runtime exchange-neutral, and put exchange-specific auth, symbols, payloads, precision, and API behavior inside adapters.

## Default Workflow

1. Confirm the active checkout, branch, target exchange, and whether the task is demo, sandbox, or live.
2. Read the local repo instructions and the Kraken path as the comparison baseline before changing a new adapter.
3. Map the requested behavior through the exchange-neutral contract: CLI or TSV input -> typed order intent -> runtime command -> adapter payload -> feed reconciliation.
4. Keep derivatives/perpetual assumptions explicit unless the user asks for spot or another product family.
5. Preserve DB-grounded architecture for each platform from day one; do not add a side path that bypasses persistence or typed runtime boundaries.
6. Verify with the smallest useful demo, smoke, or replay before suggesting live operation.

## Routes

- **Adapter design or review**: read [adapter workflow](references/adapter-workflow.md).
- **Demo runs, API setup, or TSV grammar**: read [demo and TSV workflow](references/demo-and-tsv.md).

## Output Expectations

Report the target exchange, environment, branch, command or TSV path, adapter boundary touched, tests or smoke probes run, and any live-operation risk that remains.
