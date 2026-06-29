---
name: crypto-historical-analysis
description: "Use when working on crypto historical price backfill and statistics workflows, including DataFetchers/historical_prices, Kraken BitMEX CoinGecko or Binance historical downloads, standalone historical_prices repo maintenance, MarketAnalysis/beast_variation.py, log-bps amplitude analysis, one-minute OHLCV windows, and report-stage separation from live kolaBiBot runtime data."
---

# Crypto Historical Analysis

Keep historical backfill and statistical analysis separate from live trading/runtime state. Use the downloader for datasets, then use analysis scripts for reports.

## When to Use

- Select or maintain the historical price downloader repo.
- Fetch historical OHLCV, VWAP, or trade-derived bars from Kraken, BitMEX, CoinGecko, Binance, or similar providers.
- Work with `/mnt/backup/Prog/Python/Crypto/DataFetchers/historical_prices`.
- Run or fix `/mnt/backup/Prog/Python/Crypto/MarketAnalysis/beast_variation.py`.
- Analyze non-directional amplitude in log basis points.
- Publish or sync the standalone `historical_prices` repo.

## Avoid When

- The task is live Kolabi runtime state, order execution, or feed reconciliation; use the relevant `kolabi-*` skill.
- The user asks for a live current-state tree service; do not route that into historical backfill.
- The task is generic Git publication with no crypto/data workflow implications.

## Workflow

1. Confirm the active repo boundary: historical downloads belong in `DataFetchers/historical_prices`, not `kolaBiBot/tree`.
2. Keep acquisition and analysis as separate stages.
3. For statistics, default to amplitude-only `log_bps` unless the user asks for directional returns.
4. Validate one-minute windows against `ln(high / low) * 10000` when working with one-minute bars.
5. Report the downloader path, analysis path, command used, output/report location, and any provider precision limits.

## Routes

- **Historical downloader and analysis workflow**: read [historical workflow](references/historical-workflow.md).

## References

- [historical workflow](references/historical-workflow.md)
