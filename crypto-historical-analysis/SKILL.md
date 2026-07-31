---
name: crypto-historical-analysis
description: "Use when working on crypto historical price backfill and statistics workflows, including /home/jil/hprices, Kraken BitMEX CoinGecko or Binance historical downloads, /home/jil/manalysis beast_variation.py, Journal-derived Beast Amplitude Threshold reports, tmp.org ASCII threshold charts, log-bps amplitude analysis, one-minute OHLCV windows, and report-stage separation from live Kolabi runtime data."
---

# Crypto Historical Analysis

Keep historical backfill and statistical analysis separate from live trading/runtime state. Use the downloader for datasets, then use analysis scripts for reports.

## Avoid When

- The task is live Kolabi runtime state, order execution, or feed reconciliation; use the relevant `kolabi-*` skill.
- The user asks for a live current-state tree service; do not route that into historical backfill.
- The task is generic Git publication with no crypto/data workflow implications.

## Workflow

1. Confirm the active repo boundary: historical downloads belong in `/home/jil/hprices`, not `kolaBiBot/tree`; analysis belongs in `/home/jil/manalysis`.
2. Keep acquisition and analysis as separate stages.
3. For statistics, default to amplitude-only `log_bps` unless the user asks for directional returns.
4. Validate one-minute windows against `ln(high / low) * 10000` when working with one-minute bars.
5. Report the downloader path, analysis path, command used, output/report location, and any provider precision limits.

## Routes

- **Historical downloader and analysis workflow**: read [historical workflow](references/historical-workflow.md).
- **Journal threshold and ASCII chart work**: read [historical workflow](references/historical-workflow.md#journal-threshold-reports).
