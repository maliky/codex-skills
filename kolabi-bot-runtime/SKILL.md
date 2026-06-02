---
name: kolabi-bot-runtime
description: "Use when work touches typed `kolabi` runtime internals: `State + Event -> State + Commands`, tail lifecycle transitions, or `Chronos`/`StrategyRuntime`/`Ogun` execution boundaries."
metadata:
  author: local-codex
  maturity: draft
---

# Kolabi Bot Runtime

Use this skill when the request is about the kolabi bot internals rather than CLI-facing UX.

This skill is for:
- maintaining the `State + Event -> State + Commands` runtime contract
- debugging `TailState` transitions, tail restoration, and tail-submission semantics
- preserving `Chronos`/`StrategyRuntime`/`Ogun` role boundaries
- ensuring interrupt cleanup behavior for living tails remains deterministic
- reviewing pair-cycle or intent transitions that affect command emission

This skill is not for:
- CLI argument design
- feed websocket parsing
- static docs not tied to runtime semantics
- generic exchange theory or non-runtime operator behavior

## Workflow

1. Confirm the request scope.
   - If behavior changes in command output are expected, work in runtime.
   - If command syntax or operator help changes are expected, use `kolabi-kraken-futures`.

2. Keep the runtime pure.
   - Keep `State`, `Event`, and transition logic deterministic.
   - Keep adapter/API execution in command handlers only.
   - Favor data model updates over side-effectful patches.

3. Apply boundary-safe edits.
   - Update event-to-state transitions first.
   - Emit commands from state transitions, not from random helper functions.
   - Preserve existing naming for `tail`, `PairIntent`, and existing state containers.

4. Tail handling rules.
   - Do not widen target values without an explicit new event.
   - Respect profitable direction constraints for stop logic.
   - Preserve "initial reference clear" behavior where required by existing tail semantics.

5. Run bounded verification.
   - Verify command output after each transition shape change.
   - Confirm `run`/`run-once` still triggers interrupt cleanup behavior.
   - Check that living-tail cleanup is deterministic and idempotent where relevant.

## Preferred Routes

### Runtime boundaries

- Start by reading:
  - [runtime boundaries](references/runtime-boundaries.md)

- Default route:
  1. identify the current transition entry point
  2. update transition rules and event handlers
  3. keep emitted commands unchanged unless a contract change is needed
  4. validate expected command traces on a bounded run

### Tail tracking internals

- Start by reading:
  - [tail tracking and lifecycle](references/tail-tracking.md)

- Default route:
  1. confirm state fields used by legacy tail logic
  2. preserve reference-clear and direction constraints
  3. validate trail state for partial or stale events

### Admin safety and cleanup

- Start by reading:
  - [admin cleanup and safety commands](references/admin-action-boundaries.md)

- Default route:
  1. verify interrupt cleanup paths are explicit
  2. preserve bot-mediated destructive actions in the runtime contract
  3. ensure cancel/all lifecycle semantics remain coherent with current operator constraints

## Operating Rules

- Keep project symbols that carry stable meaning.
- Document transition changes with expected command traces.
- Do not patch runtime in a way that changes CLI intent without explicit CLI pass.
- Preserve the state/event split even when adding new runtime cases.

## Deliverables

When using this skill, include:
- modified state/event entrypoints
- impacted command stream and expected command diffs
- confirmation of tail lifecycle behavior
- cleanup or shutdown behavior impacts

## References

- [runtime boundaries](references/runtime-boundaries.md)
- [tail tracking and lifecycle](references/tail-tracking.md)
- [state and event loop](references/state-event-loop.md)
- [admin cleanup and safety commands](references/admin-action-boundaries.md)
