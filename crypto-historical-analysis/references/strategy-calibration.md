# Cross-Instrument Strategy Calibration

Use this route when adapting a Kolabi strategy template to a different instrument from historical amplitude placement. Read the current `manalysis` and Kolabi repo instructions, the canonical template and parser, and the current `bv`/inventory help before selecting commands. Keep statistical calibration separate from replay and live execution.

## Source And Mapping

1. Fix the requested UTC observation window and acquire source and target one-minute histories over the same interval. Verify minute-grid completeness, provider limits and contract opening dates. Resume the documented cache after a provider gap; do not invent missing candles or silently compare different windows.
2. Record which template fields may change. Preserve row count/order, pair topology, quantities, schedules, order types, hooks and deltas when the user asks for an otherwise identical strategy.
3. For each relative placement, estimate its empirical source percentile in the specified direction and map that percentile to the target instrument's same-window amplitude distribution. Preserve the measured rank rather than replacing it with a convenient fixed p10/p20 label.
4. Obtain a fresh target ticker and instrument metadata for absolute levels and tick conversion. Use Decimal arithmetic, the actual tick grid and directionally correct outward rounding; do not reuse the source instrument's price or tick.

## Audit And Acceptance

Keep an auditable mapping with source field/value, source percentile, target amplitude or log-bp, final target value, data bounds, coverage and metadata observation time. Independently check the numeric conversion and compare every non-placement field against the template, then parse the resulting Org strategy with the matching Kolabi version. Parser success establishes syntax and structure only; performance, demo readiness and live execution require separate evidence and authorisation.
