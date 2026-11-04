# Cross-Instrument Strategy Calibration

Use this route when adapting a Kolabi strategy template to a different instrument from historical amplitude placement. Read the current `manalysis` and Kolabi repo instructions, the canonical template and parser, and the current `bv`/inventory help before selecting commands. Keep statistical calibration separate from replay and live execution.

## Select The Calibration Contract

- Establish whether the task transfers each source placement's measured percentile or uses explicit user-edited `target p` values. In rank-transfer mode, retain the empirical source rank. In target mode, reread the edited report and use its targets, preserving the family, window and side mapping. Labels such as p10/p20 in a pair name can describe another field and are not authoritative targets.
- Follow the requested data coverage. Use a common UTC interval for comparable same-window transfer; when the user asks for all cached history per asset, retain and disclose each asset's actual bounds and sample support. Check completeness, provider limits and contract opening dates, reuse verified caches, and honour a no-download request. Do not fill gaps with invented candles.
- Record the fields allowed to change. Preserve row count/order, topology, quantities, schedules, order types, hooks and offsets when requested. Reconcile unsaved editor content and on-disk changes before replacing a strategy; a stale buffer can restore obsolete targets or lose manual edits.

## Units And Rounding

Record the target ticker, tick metadata and observation time used for absolute prices and tick conversion; refresh them when the task requests current placements. Use Decimal arithmetic and the requested rounding policy. Whole B units, nearest five ticks or outward rounding are choices from particular tasks, not universal defaults. Preserve T offsets when the requested conversion excludes `hDelta`/`tDelta`.

Keep statistical amplitude `10000 * ln(high/low)`, displayed B/T values, and effective runtime price displacement distinct. Check the actual order materialiser: a sell-head B parameter can produce a different downward log distance from its literal B value. Audit both statistical and effective ranks where needed. An amplitude percentile or unlock-distance rank does not establish fill probability, conditional hook performance, or stop width.

## Audit And Acceptance

Keep an auditable mapping with source field/value, measured source percentile or explicit target p, target amplitude, rounded value, rounding policy, data bounds, support and metadata observation time. Retain the unrounded calculation even when the displayed report uses fewer decimals. Independently check conversion against the runtime materialiser and compare every protected field against the template, then parse the resulting Org with the matching Kolabi version. Parser success establishes syntax and structure only; performance and execution readiness require their own evidence.
