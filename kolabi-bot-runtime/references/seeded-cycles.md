# Seeded Activation Cycles

Use the current `MANUAL.org` hook contract and `kolabi/bot/dependencies.py`, `cycle_policy.py`, `chronos.py`, `strategy_runtime.py` and reducers. `tests/bot/test_seeded_cycles.py` is the focused executable contract. This mechanism differs from event repetition and coexisting clones; use the graph validator rather than assuming every dependency cycle is invalid or accepting an arbitrary cycle.

## Unblocked Tail-Fill Evidence

`-tuf` (`-tail-unblocked-filled`) requires an increase in this tail attempt's cumulative execution after the recorded runtime `first_unblocked_at`. The unblock decision is distinct from an acknowledged amendment or profitable exit. An earlier fill cannot qualify later through a repeated cumulative snapshot; a new positive execution after unblock can qualify. Unblock alone and zero-fill cancellations supply no evidence.

The same rule applies to real and virtual attempts, with fresh evidence on each attempt. Existing `-tf` keeps its positive-tail-fill semantics. `-tuf` is a hook condition, not a supported new `repeat` signal; direct self-hooks remain rejected.

## Bootstrap And One-Shot Admission

An example supported shape has `R` activated by `any(C-tuf,seed-tuf)` and `C` by `R-tuf`. The external activation path must satisfy every bootstrap threshold. Reject unseeded cycles, direct self-hooks, cancellation-action cycles and event-based cloning inside a cycle. Cycle members reset after ordinary terminal completion with their configured pause/cooldown.

Each source instance/attempt and condition can signal each destination once. A destination that is busy, cooling, held, outside its window or unable to admit a fresh head discards the signal; it does not queue it for later. A new source attempt can make a new offer. Consumed signals survive compatible strategy revisions but are not durably restored after restart.

`CycleSignalAccepted` means accepted for admission. It does not prove exchange submission, head fill or a completed cycle. Capacity, fresh market evidence, exact admission identity and other safety gates are rechecked at final dispatch; a race must not turn a stale offer into a delayed order. A pending guarded offer is not a general queue of discarded signals.

## Implementation And Verification

Keep graph validation and evidence facts deterministic, orchestration in Chronos and irreversible effects in execution layers. Test bootstrap thresholds, duplicate/partial fills, busy destinations, cooldown/hold/window rejection, capacity/market races, compatible revisions and live/replay agreement. Protect unique attempt/admission identities through command queues.

For apparent head timeouts, inspect both the emitted fill fact and deadline order. Head completion can occur after a partial fill already placed a tail; it still needs its own transition. Process the queued event batch before checking head-fill deadlines, while incomplete heads retain applicable clocks. Activation-hooked pairs can have no configured head deadline, including with unlimited attempts; cancellation-only hooks do not grant that exemption. See [timeouts and repetition](timeouts-and-repetition.md) for inherited-clock rules and [run reporting](../../kolabi-run-analysis/references/run-reporting.md) for historical fill recovery and financial attribution.
