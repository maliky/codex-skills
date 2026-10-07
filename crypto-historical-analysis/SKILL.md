---
name: crypto-historical-analysis
description: "Use for crypto historical backfill and manalysis/bv statistics: amplitude thresholds, pipe/block prediction and associations, popular prices, Kraken Futures inventory, CoinGecko-ranked reports, volume interpretation, and one-minute close-only intrinsic-time/directional-change calibration. Keep this separate from live Kolabi runtime."
---

# Crypto Historical Analysis

Keep historical backfill and statistical analysis separate from live trading/runtime state. Use the downloader for datasets, then use analysis scripts for reports.

## Avoid When

- The task is live Kolabi runtime state, order execution, or feed reconciliation; use the relevant `kolabi-*` skill.
- The user asks for a live current-state tree service; do not route that into historical backfill.
- The task is generic Git publication with no crypto/data workflow implications.

## Workflow

1. Resolve the active `hprices`/`manalysis` checkout and its Python environment on this host; known roots vary between `/home/jil`, `/home/konemalikMI` and `/mnt/backup/Prog/Python/Crypto`. Do not redirect historical work into live `kolaBiBot/tree`. Reuse a workflow's existing inventory cache where applicable.
2. Keep acquisition and analysis as separate stages.
3. Read the current `README.org` and command help before constructing a `bv` command; the command surface evolves faster than this skill.
4. Decide whether the question is descriptive association or unseen-data prediction before choosing full-history, holdout, purge, or bootstrap behavior.
5. For amplitude statistics, default to non-directional `log_bps`. Directional returns and intrinsic-time confirmations are distinct measures; follow the requested workflow rather than substituting amplitude thresholds.
6. Validate one-bar amplitude against `ln(high / low) * 10000`. For close-only directional changes, use the causal confirmation rules in the intrinsic-time reference, not the candle's high/low amplitude.
7. Put the exact command before generated Org results and report the data source, output location, date bounds, support, provider limits, exclusions, and ranking unit.

## Routes

- **Historical downloader and analysis workflow**: read [historical workflow](references/historical-workflow.md).
- **Journal threshold and ASCII chart work**: read [historical workflow](references/historical-workflow.md#journal-threshold-reports).
- **Pipe prediction, distance, thresholds, and popular prices**: read [market structure analysis](references/market-structure-analysis.md).
- **Kraken Futures inventory, CoinGecko rankings, and cross-instrument associations**: read [market universe analysis](references/market-universe-analysis.md).
- **Intrinsic time, directional-change counts, and one-minute ADA delta calibration**: read [intrinsic-time calibration](references/intrinsic-time-calibration.md); distinguish the research plan from implemented commands and measured results.
