---
name: kolabi-kraken-futures
description: Build, debug, and operate the local `kolabi` Kraken Futures trading workflow. Use when a task involves CLI behavior, order-contract alignment, smoke/probe commands, cancel/close/list operations, editable-install or packaging fixes, and local command-surface maintenance.
metadata:
  author: local-codex
  maturity: draft
---

# Kolabi Kraken Futures

Use this skill when the task is primarily about the Python `kolabi` codebase for Kraken Futures trading, order execution, or operator-facing command workflows.

This skill is for:
- extending or debugging Kraken Futures order support
- maintaining CLI entrypoints for probing, placing, cancelling, closing, or listing orders
- validating smoke flows against demo or test environments
- fixing local packaging or editable-install setup
- reorganizing the codebase while preserving project naming constraints
- documenting exact operator commands in repo-local docs such as `MAN.org`, `DEV`, or CLI help
- delegating detailed runtime or feed internals to focused companion skills

This skill is not for:
- Haskell-only `FinancialNoise` simulator work that does not touch the Python Kraken Futures path
- generic exchange-agnostic trading theory
- remote deployment or VPS hardening unless it directly blocks the local Kraken Futures workflow

## Workflow

1. Establish the operating path.
   - Identify whether the task is about CLI behavior, adapter behavior, order-contract coverage, packaging, or codebase cleanup.
   - Confirm the intended environment: demo, live, or local smoke path.
   - Prefer the existing operator command surface over adding a new one unless the current surface is clearly missing a necessary action.

2. Preserve the project's naming rules.
   - Keep symbolic names that carry project meaning, such as `tail`, `multi_kola`, and `run_multi_kola`.
   - Prefer `bargain` over generic `trade` naming where the project already made that choice.
   - Remove legacy shim or compatibility layers when they are no longer needed, but do not replace them with vaguer names.

3. Verify command flows with bounded probes.
   - Use short smoke or probe commands first.
   - Prefer deterministic command checks over long unattended runs.
   - When debugging failures, capture the exact CLI invocation and the exact adapter or API error before changing behavior.

4. Treat order support as a contract surface.
   - Enumerate supported order types explicitly.
   - Keep market, limit, stop-loss, take-profit, trigger-entry, and trailing-stop behavior distinct.
   - If trailing behavior is strategy-managed rather than exchange-native, document that boundary clearly.
   - Do not silently pass unsupported trailing fields into adapters that do not accept them.

5. Route deep internals to focused skills.
   - Use `kolabi-bot-runtime` for `State + Event -> State + Commands`, tail transitions, and `Chronos`/`Ogun` boundaries.
   - Use `kolabi-market-feeds` when debugging public/private websocket behavior, feed-driven order visibility, or private-balance updates.
   - Keep this skill focused on operator-surface behavior and command compatibility.

6. Keep packaging and local operation obvious.
   - `pip install -e .` should work when the repo claims editable-install support.
   - Prefer standard `setuptools.build_meta` or an equally explicit build backend.
   - Document operator commands where the user will actually look for them.

7. Patch conservatively and re-check the operator path.
   - Keep command names short and task-shaped.
   - After a contract or CLI change, re-check help text, smoke flows, or documented commands.
   - Prefer one canonical option over parallel aliases when both express the same behavior.

## Preferred Routes

### CLI and operator commands

- Start by reading:
  - [cli and operations](references/cli-and-operations.md)

- Default route:
  1. identify the existing entrypoint
  2. verify the exact command grammar already in use
  3. extend or fix the minimum command surface needed
  4. update local command documentation

### Order contract and adapter behavior

- Start by reading:
  - [order contract](references/order-contract.md)

- Default route:
  1. list the intended order types and parameters
  2. compare them against the adapter signature
  3. remove unsupported fields instead of leaking them through blindly
  4. re-run the bounded smoke path

### Packaging and codebase cleanup

- Start by reading:
  - [packaging and cleanup](references/packaging-and-cleanup.md)

- Default route:
  1. confirm the build backend and editable-install path
  2. remove unnecessary compatibility layers
  3. keep naming and module layout coherent
  4. re-check importability and documented entrypoints

## House Rules For This Host

- Prefer short runnable commands over abstract descriptions.
- Keep the local command surface obvious through `--help`, `MAN.org`, or adjacent repo docs.
- Probe before guessing when a feed, adapter, or CLI path appears broken.
- Preserve symbolic project naming and remove stale legacy code instead of layering more aliases on top.
- Treat operator workflows as source of truth; do not invent a cleaner but incompatible command language.

## Deliverables

When using this skill, the output should usually include:
- the command path or entrypoint touched
- the supported or changed order-contract surface
- the exact operator commands to run next
- any packaging or environment prerequisite that still blocks execution

## References

- [cli and operations](references/cli-and-operations.md)
- [order contract](references/order-contract.md)
- [packaging and cleanup](references/packaging-and-cleanup.md)
- [runtime split guidance](references/runtime-boundaries.md)
