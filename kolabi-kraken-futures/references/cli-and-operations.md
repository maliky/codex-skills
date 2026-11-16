# CLI And Operations

Use this reference when the task is mainly about the operator-facing command path.

For `scripts/kolabi-fresh-run`, `--no-purge` or adding another symbol to an active account, read [launch modes and shared accounts](../../kolabi-bot-runtime/references/live-runtime-lessons.md#launch-modes-and-shared-accounts) before suggesting a command.

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

## Exact Order Recovery And Financial Inspection

Inspect `scripts/kolabi-recover-orders` and current help before use. The current route accepts repeated exact `--order-id` with `--log`, `--run`, `--environment` and account scope; `--dry-run` queries without saving evidence. Persistence/repair flags can evolve and require explicit authorization: do not infer a safe default from an older command example. Confirm identity, original accepted quantity, fresh venue evidence and terminal status before writing; a fill's `remaining_order_qty` is not the original order quantity. Older verification cannot override a newer absence observation without renewed evidence. Never resend an accepted order after `ACCEPTED_TOTAL_PERSIST_FAILED`; reconcile its exact identity instead.

Balance/position questions use read-only account evidence and [account reconciliation](../../kolabi-run-analysis/references/account-reconciliation.md). Inspect operator effects before invocation: a run snapshot/pause helper can stop the bot and cancel orders. Do not use that mutating handoff to obtain a financial snapshot. On PostgreSQL recovery errors, inspect disk availability, container logs and readiness; preserve database files and WAL.
