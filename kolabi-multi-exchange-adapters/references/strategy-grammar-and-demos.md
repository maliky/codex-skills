# Strategy Grammar And Demos

Use this reference for Org strategy parsing, typed units, virtual execution, and cross-exchange demos. Read the current `MANUAL.org`, `kolabi/bot/tsv/parser.py`, `order_codes.py`, `price_units.py`, and `quantity.py` in the active Kolabi checkout; the `tsv` package name does not imply the old input grammar is supported.

## Demo Guardrails

- Treat demo, sandbox, and testnet credentials as sensitive. Do not print or commit API keys, secrets, tokens, or `.env` contents.
- Confirm the selected environment before any command that can place, cancel, or close orders.
- Reset public and private demo databases only when the user explicitly wants a clean demo state.
- Prefer bounded MWE commands over broad live runners when proving a new adapter path.
- Keep demo key names exchange-specific and explicit. Recent local convention used short exchange families such as Kraken futures/spot and BitMEX/Binance demo variables; map them in configuration code rather than scattering raw env names across adapters.
- Report missing demo credentials as setup gaps without exposing names plus values. It is acceptable to mention the variable names needed, but never echo secret contents.

## Org Strategy Grammar

- Use `exchg`, `qty`, `oType`, `tType`, `hDelta`, `tDelta`, `pGate`, `hPrice`, `tPrice`, `tUblk`, and `wUblk` with the parser's exact spelling. Scheduling and dependency fields include `tps_run`, `essais`, `tOut`, `pause`, `cool`, and `hook`; policy/repetition fields include `rFunc`, `cFunc`, `tFunc`, `repeat`, and `maxClones`.
- Legacy columns such as `atype`, `quantity`, `exchange`, `oDelta`, and lower-case `hprice` are rejected. Do not reintroduce them to repair an old example. Check whether the task concerns a historical checkout before migrating a legacy file.
- Resolve inherited Org properties before judging a blank cell. Preserve the required `pGate` and `hPrice` header columns even when their cells are blank; blank values can intentionally disable a gate or satisfy a market-order contract.
- Parse the whole strategy and resolve its exchange/product/symbol routes before starting feeders, purging local rows, or executing orders. `scripts/kolabi-fresh-run` performs route validation before those side effects; keep that ordering. Check [launch modes and shared accounts](../../kolabi-bot-runtime/references/live-runtime-lessons.md#launch-modes-and-shared-accounts) when existing bots or listeners are present.

## Virtual Execution

- `V` is an execution prefix. Use `VM`, `VL`, `VS`, `VSL`, `VMT`, or `VLT`, subject to the underlying type's suffix and price validation. Bare `V` is rejected and is not an alias for `VM`.
- Both legs of a pair must use the same execution mode. `VM` needs blank `hPrice` and a virtual tail. An old `V + real tail` pair needs an explicit redesign; changing only its head would silently change the intended exposure. Connect a virtual signal pair to a separate real pair through hooks.
- Virtual execution uses fresh local market observations, including executable bid/ask evidence after acceptance or trigger. A conditional trigger and fill cannot occur on the same observation. It produces no exchange order identity, request, account exposure, fee, or trading PnL.
- Virtual-only routes still require public data and instrument metadata. A real follower on the route retains private readiness and normal execution requirements. Preserve the boundary in parsing, route resolution, replay, and reporting tests.

## Price And Quantity Units

| Field family | Meaning and validation |
| --- | --- |
| Price `A`, `D`, `B` | Absolute price, nominal price distance, and logarithmic basis-point distance respectively; use the field's materialisation helper and side convention. `B` is not an ordinary percentage or tick count. |
| Price `T` | A finite whole number of instrument ticks in `hPrice`, `tPrice`, `hDelta`, `tDelta`, `pGate`, or `tUblk`; `T1.5` fails validation. Require a finite positive tick size from the exact route's metadata. |
| Quantity `A` | Absolute venue size, subject to that route's quantity step and minimum. Determine whether the instrument expresses size in contracts or base units. |
| Quantity `U` | USD notional materialised using mark price, contract size, quantity step, and minimum; preserve the requested notional separately from the resolved size. |
| Quantity `%` | Percentage of usable available balance, requiring a ready balance reader; the parser requires `0 < percent < 100`. Offline replay does not invent this balance. |

`T` changes price fields only. Signed ticks are allowed in limit offsets and gate bounds; head/tail distances and trailing-unblock distances are non-negative, with a positive distance required for fixed trailing. Venue rounding and post-only rules still apply. For example, with tick size `0.00001` and reference `0.24000`, a buy stop at `hPrice=T4` is `0.24004`; `hDelta=T4` gives a nominal buy limit of `0.24008` before venue validation. Never infer a tick from decimal precision or substitute a default when metadata is missing. Validate tick metadata even when only the tail uses `T`.

Keep quantity, price, and time parsing separate. In particular, `A8` quantity does not universally mean eight dollars, and `U100` is not an instruction to send 100 contracts. Test typed values after inherited defaults and policy callbacks, not just the raw table strings.

## MWE Procedure

1. Identify the Org strategy or fixture, resolve its defaults, and validate its routes offline.
2. Verify exchange-specific env selection and DB URL before running.
3. Within the authorised demo scope, run the smallest command that exercises order creation, feed observation, and cleanup.
4. Inspect operator logs for exchange, product, order id, client id, and normalized status.
5. Perform the agreed cleanup through runtime-mediated commands; cancelling an order and closing filled exposure are separate actions.

## Repository Hygiene

- Shared strategy sources are tracked in `manalysis/strategies/`; Kolabi uses per-file links for those files and retains its own local examples. For ownership or migration work, read [shared strategies](../../crypto-historical-analysis/references/shared-strategies.md). Keep account data and runtime artifacts out of strategy commits.
- Keep branch names and documentation aligned when merging multi-exchange work back to development branches. Record the fixture and exchange coverage in `README.org` or the nearest project runbook.

## Report Back

Lead with the exact command or fixture, the selected exchange environment, and whether the run proved parser, adapter, feed, or runtime behavior.
