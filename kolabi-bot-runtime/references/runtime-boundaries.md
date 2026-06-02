# Runtime Boundaries

Use this reference when deciding which kolabi runtime layer should own a behavior.

This reference keeps runtime changes scoped to deterministic transitions.

- Keep `State + Event -> State + Commands` at the core.
- Treat `State` as the only mutable domain model.
- Keep `Chronos` for scheduling and event orchestration.
- Keep `Ogun` for command execution and irreversible side effects.
- Keep conversion to raw adapter payloads in execution layers only.

## Checks Before Editing

- If the change mutates persistence, state flow, or event replay, confirm transition rules.
- If the change calls into exchange clients, keep it in execution boundaries.
- If the change updates cleanup behavior, validate it through command path and cancel behavior.
