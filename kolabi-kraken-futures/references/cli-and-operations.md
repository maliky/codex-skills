# CLI And Operations

Use this reference when the task is mainly about the operator-facing command path.

## Stable patterns captured from recent work

- Keep commands runnable from the repo without extra orchestration.
- Prefer bounded smoke commands to verify behavior quickly.
- Document exact commands in `MAN.org`, `DEV`, or CLI help when the user asks to remember them later.
- Add direct commands for repetitive actions such as:
  - smoke runs
  - cancel all open orders for a symbol
  - close all positions after cancelling orders
  - list open orders or trigger orders

## Practical guidance

- Reuse existing command groups before creating a new top-level command.
- If a command needs dangerous behavior, keep the default conservative and explicit.
- If a flag only duplicates another behavior and the user does not want it, remove the alias rather than carrying both.
- When a command fails, report the concrete invocation and the concrete adapter error.
