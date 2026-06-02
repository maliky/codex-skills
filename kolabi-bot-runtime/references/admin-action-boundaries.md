# Admin Actions and Safety Boundaries

Use this when adjusting run-once/run cleanup and admin destructive actions.

## Core Constraints

- `run` and `run-once` should keep cleanup paths deterministic on interrupt.
- Living-tail cancellation should be explicit, idempotent when possible, and non-blocking.
- destructive actions should keep bot mediation paths explicit.

## Procedure

- identify where interrupt and signal handling is defined
- confirm cleanup path invokes the same runtime command sequence as standard cancel operations
- validate command ordering so cancel paths do not bypass runtime state checks
