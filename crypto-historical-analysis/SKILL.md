---
name: crypto-historical-analysis
description: "Use when working on crypto historical price backfill and market-statistics workflows, including hprices providers, /home/konemalikMI/manalysis or /home/jil/manalysis, the bv/beast_variation CLI, amplitude and beast thresholds, pipe/block prediction, pipe-distance or cross-pipe association, popular-price reversal analysis, Kraken Futures inventory and CoinGecko-ranked Org reports, contract-versus-underlying volume interpretation, one-minute OHLCV windows, and separation from live Kolabi runtime state."
---

# Crypto Historical Analysis

Keep historical backfill and statistical analysis separate from live trading/runtime state. Use the downloader for datasets, then use analysis scripts for reports.

## Avoid When

- The task is live Kolabi runtime state, order execution, or feed reconciliation; use the relevant `kolabi-*` skill.
- The user asks for a live current-state tree service; do not route that into historical backfill.
- The task is generic Git publication with no crypto/data workflow implications.

## Workflow

1. Confirm the active checkout: historical downloads belong in `hprices` (`/home/konemalikMI/hprices` or `/home/jil/hprices`), not `kolaBiBot/tree`; analysis belongs in the matching `manalysis` checkout.
2. Keep acquisition and analysis as separate stages.
3. Read the current `README.org` and command help before constructing a `bv` command; the command surface evolves faster than this skill.
4. Decide whether the question is descriptive association or unseen-data prediction before choosing full-history, holdout, purge, or bootstrap behavior.
5. For statistics, default to amplitude-only `log_bps` unless the user asks for directional returns.
6. Validate one-minute windows against `ln(high / low) * 10000` when working with one-minute bars.
7. Put the exact command before generated Org results and report the data source, output location, date bounds, support, provider limits, exclusions, and ranking unit.

## Routes

- **Historical downloader and analysis workflow**: read [historical workflow](references/historical-workflow.md).
- **Journal threshold and ASCII chart work**: read [historical workflow](references/historical-workflow.md#journal-threshold-reports).
- **Pipe prediction, distance, thresholds, and popular prices**: read [market structure analysis](references/market-structure-analysis.md).
- **Kraken Futures inventory, CoinGecko rankings, and cross-instrument associations**: read [market universe analysis](references/market-universe-analysis.md).
