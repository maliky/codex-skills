# State and Event Loop

Use this reference when implementing new runtime transitions.

## Core Invariants

- Every external event should map to one explicit transition step.
- Transition results should be small and inspectable.
- Command emission should be explicit and stable for a given transition.

## Practical Steps

- trace event origin before deciding transition shape
- keep command creation as pure data
- avoid hidden side effects in transition helpers
- preserve existing state field names unless migration is explicitly requested
