# Strategy Revisions

Use this reference for periodic strategy loading and changes to an active family's definitions. Inspect the current branch and dirty state before relying on local behaviour; a checkout containing revision fixes does not prove the running bot has them. Start with `strategy_source.py`, `strategy_revision.py`, `strategy_runtime.py` and `chronos.py` in `kolabi/bot/`, plus `tests/bot/test_strategy_reload.py`.

## Source Selection And Acceptance

- `--strategy-reload` is a finite positive interval in hours: `1` is hourly and `.5` is half-hourly. It is fixed at startup; omitting it preserves one-off loading. A watcher can remain alive after every current attempt finishes.
- `--strategy` accepts an Org file or a folder. Folder selection uses immediate `.org` files, excludes names beginning with `.` or `#`, and picks the greatest `(mtime_ns, filename)`. It does not concatenate files or fall back to an older file after the selected candidate fails validation. A folder containing reports or unrelated Org documents is therefore a poor live source.
- Capture a stable candidate, validate parsing, dependencies, routes and policy compatibility, then accept it through the serialised runtime transition. A rejected candidate leaves active definitions and blocks intact. Formatting-only changes do not reset the strategy.
- Atomic saves matter: a valid but temporarily shortened table can be accepted as deliberate removal. An empty strategy is rejected. Keep source path, content digest, effective time and accepted revision in logs/snapshots.
- Reloading definitions does not reload Python policy modules. New instruments or real execution on a previously virtual-only route require the supported restart workflow; do not expand route/account resources silently during acceptance.

## Frozen Attempts And Late Results

An attempt is revisable only while unsent: latent/hooked, with no head send begun, order identities, virtual execution state, retirement, or pending/unresolved reconciliation. Active leases and outstanding commands normally protect it. A guarded head still waiting for REST capacity can be replaced before its send begins; invalidate its old queued command so it cannot execute after revision. A missing exchange acknowledgement does not make a sent head revisable.

Flying attempts retain their accepted parameters and order clocks. Unsent work and later activations use the accepted revision. Keep exact family, instance, generation, admission and order identities through queues, REST responses and private events. Drop obsolete results before bookkeeping; a late placement, cancellation or fill for an old attempt must not mutate a replacement attempt with the same source name. Recheck the attempt at the final dispatch gate.

## Shared Budget And Deferred Work

- The reset `essais` budget is shared across revisable unsent instances, reserved successors and pending ordinary repeats. Selection retains newest work by creation/request time, then generation and instance key. `essais=*` stays unlimited; flying attempts keep their terms.
- Retire surplus never-sent instances locally with `revision_budget`; discard excess reservations/repeats without replaying the original trigger. Log what was discarded so the reduced budget can be explained.
- Clear retained pause/cooldown delays without bypassing outstanding operations or reconciliation. Activation must recheck the remaining family budget and allocate a unique generation across both successor and ordinary-repeat paths.
- Preserve compatible collected votes with their original evidence ages. Acceptance must not refresh an old vote's lifetime or fabricate new hook evidence.
- A validated quantity or quantity-unit change can clear that family's `invalidSize` block, including instance blocks. An unchanged quantity, unrelated edit, or rejected candidate cannot. Reconciliation and authentication blocks remain in force, including for an uncertain sibling.

## Removal And Retirement

Removing a source row retires its instances and cancels remaining head/tail quantities through normal commands. Retain filled exposure and execution evidence; removal does not submit a closing trade. Keep cancellation available during reconciliation, and wait for pending submissions and cancellation outcomes before allowing that name to return. A late head fill during retirement must be accounted for without resurrecting removed strategy work. Administrative retirement does not create another successor.

## Verification

Use focused revision/lifecycle tests for accepted versus rejected candidates, frozen sent heads, late responses after replacement, multiple revisions while work is pending, reduced budgets spanning all three kinds of unsent work, unique generations, removed-family late fills, and quantity corrections beside reconciliation blocks. Verify both emitted commands and retained state. For report attribution, use [run reporting](../../kolabi-run-analysis/references/run-reporting.md); do not treat current file contents as an attempt's accepted snapshot.
