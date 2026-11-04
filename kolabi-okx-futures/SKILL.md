---
name: kolabi-okx-futures
description: "Use for Kolabi's OKX Europe X-Perps (OKXF) adapter and operator workflow: explicit instruments, contract sizing, account readiness, private order evidence, complete portfolio and position snapshots, bounded reconciliation, and demo/live commands. Use kolabi-multi-exchange-adapters for shared contracts."
---

# Kolabi OKX Futures

Work from the current Kolabi checkout, its `AGENTS.md`, `MANUAL.org`, CLI help and implementation. The local manual describes the implemented route; verify current venue rules before relying on a historical account or product snapshot.

## Boundaries

- Use [multi-exchange adapters](../kolabi-multi-exchange-adapters/SKILL.md) for exchange-neutral grammar and adapter contracts, [market feeds](../kolabi-market-feeds/SKILL.md) for shared feed reconciliation, and [run analysis](../kolabi-run-analysis/SKILL.md) for historical PnL and exposure.
- Keep credentials, private portfolio values and dated instrument settings out of skills and commits. Inspect environment variable names and account scope without printing secret values.
- A request to inspect an account or repair code does not itself authorise a demo or live order, service restart, or change to leverage and collateral settings.

## Workflow

1. Check branch, dirty state, route, demo/live environment, account scope and exact native symbol. `OKXF` has no default instrument or automatic rollover.
2. Read [contracts and evidence](references/contracts-and-evidence.md) for X-Perp eligibility, units, order identity, position and portfolio interpretation.
3. Before running the operator helper, read [operator workflow](references/operator-workflow.md) and explain its current database and PostgreSQL effects. Preview the exact command when its effects are uncertain.
4. Trace adapter changes through typed intent, venue payload, durable identity, private feeder and canonical DB evidence; leave unknown execution outcomes unresolved.
5. Validate with focused offline adapter, integration and launcher tests. Treat account eligibility and native conditional behaviour as unverified until a separately authorised venue probe establishes them.

## Report

State the selected environment, account scope and symbol, evidence timestamps, actions and local mutations performed, checks run, and any unresolved venue or order state.
