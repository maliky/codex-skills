# Packaging And Cleanup

Use this reference when the task is about installability, repo cleanup, or module reorganization.

## Durable constraints

- `pip install -e .` should work for normal local development.
- Prefer a standard editable-install path using an explicit build backend.
- Remove compatibility shims that no longer serve another live codebase.
- Keep naming that carries project intent:
  - preserve `tail`
  - preserve `multi_kola`
  - preserve `run_multi_kola`
  - prefer `bargain` where the project already chose it

## Cleanup posture

- Favor line-clean, homogeneous module layout.
- Remove legacy aliases rather than keeping multiple names for the same behavior.
- Keep the repo importable after any move.
- If documentation or config still refers to old paths, update it in the same pass.
