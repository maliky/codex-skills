# Timeouts And Repetition

Use `kolabi/bot/timeouts.py`, `repetition.py`, the reducers and Chronos together with `tests/bot/test_timeouts.py` and `test_event_repetition.py`. Resolve Org defaults before reasoning about the effective clocks.

## Four Order Clocks

| `tOut` key | Starts at | Applicable underlying types |
| --- | --- | --- |
| `hp` | First accepted head placement | `L`, `S`, `SL`, `MT`, `LT` |
| `ht` | First confirmed head trigger | `S`, `SL`, `MT`, `LT` |
| `tp` | First accepted tail placement | `L`, `S`, `SL`, `MT`, `LT` |
| `tt` | First confirmed tail trigger | `S`, `SL`, `MT`, `LT` |

Durations are minutes, for example `10-hp 3-ht 30-tp`. Tagged overrides merge by matching key through inherited defaults; `0-key` disables that component. Bare `33` resets the set to `33-hp` and disables the other components. Head settings never supply tail settings. An explicit incompatible component fails validation; inapplicable inherited defaults are omitted. `M`/`VM` has no order timeout clock. A tagged expression does not implicitly add automatic hp.

For a pair without an activation hook, absent `tOut` uses the existing automatic hp calculation where applicable, and `essais=*` requires an explicit applicable positive timeout. Activation-hooked pairs can omit all clocks, including with `essais=*`, and receive no automatic hp. Applicable inherited defaults still apply. Cancellation-only `CH:`/`CT:` hooks do not grant the exemption. A generic `cFunc` may preserve an absent timeout for an activation-hooked pair; a specific policy such as `rns_quorum` may still require one for its own calculations.

Once triggered, an enabled trigger clock replaces that order's placement clock. With `10-hp 3-ht`, placement at 12:00 and trigger at 12:08 means expiry at 12:11. With only `10-hp`, expiry remains 12:10; with only `3-ht`, there is no deadline before triggering. Each instance owns its clocks. Gate/capacity waiting starts no placement clock, and amendments, duplicate messages or partial fills do not restart one.

A positive fill of a known conditional order can establish an inferred trigger if the explicit event is missing. A public price crossing alone cannot start a real order's trigger clock; virtual orders use their explicit local evidence. Keep deprecated `tLife` handling at the compatibility boundary: it aliases `tt`, cannot accompany an explicit `tt`, and new snapshots use `tOut`.

## Expiry And Exposure

Expiry cancels remaining quantity. Head expiry preserves or creates tail work for the quantity already filled; a wholly unfilled real head creates no tail. Tail expiry cancels its remainder and prevents rearming or new successors from that retired instance, while an already reserved successor can remain eligible. Neither expiry nor clone eviction closes filled exposure, and either can leave exposure without a protective tail. Preserve uncertain-submission and cancel-confirmation safeguards.

Timers need the running bot and incur event-loop/cancellation latency. Offline replay schedules deadlines even when quotes stop. Current instances, timers and trailing state are not durably restored after a bot restart; do not promise resume semantics from a fresh launch.

## Repetition And Capacity

- `repeat` selects the event permitting one successor. Distinguish positive fills (`hf`, `tf`), confirmed conditional triggers (`ht`, `tt`), terminal failures (`he`, `te`), and legacy pair outcomes (`pc`, `pe`). A trigger can leave a stop-limit child active and unfilled; a transport exception with unknown outcome is not a failure signal.
- Blank/default `anyn(1,[pc,pe])` retains ordinary terminal repetition. Event repetition can create a successor while its parent remains active. Signals latch per instance and can reserve at most one successor; duplicates cannot replenish the budget. Flat `any`, `all`, and `anyn` expressions use the current parser's supported signals.
- Keep family name, runtime instance and generation distinct. `essais` bounds generations including the initial instance. Event-repeat `pause` controls spacing between admissions; `cool` applies on successful tail-close repetition. Fresh successors recheck gates and readiness.
- `maxClones` limits living instances per family (`0` means unlimited). Before a successor would exceed the limit, retire the oldest living instance's remaining orders and await confirmed termination before admission. This does not raise the independent `--max-active-pairs` capacity.
- Active-pair reservations survive pending acknowledgements and uncertain outcomes; partial fills retain capacity through needed tail work. Protective tails and cancellation remain possible at full head capacity. Do not prune reconciling instances or reserved successors as if they were idle history.

## Votes Are Policy Evidence

Read the selected hook and `cFunc` policy rather than equating repetition with a vote. For the current `rns_quorum` policy, the first positive tail fill supplies a vote from an exact attempt; clones of one family still count as one member. Vote validity begins at that fill using the configured tt duration (legacy hp fallback), independently of the order's tt deadline starting at trigger. Triggers, amendments and zero-fill cancellations supply no fill vote. Revisions preserve compatible vote ages; queued unsent heads revalidate expiring evidence before dispatch.

For `-tuf` and seeded dependency cycles, read [seeded cycles](seeded-cycles.md). Their one-shot admission offers and discard rules are separate from repeat-signal reservations.
