# Market Universe Analysis

Use this reference for public Kraken Futures inventory, CoinGecko-enriched rankings, and cross-instrument association commands maintained in `manalysis`.

## Boundary

`bv kraken-futures-inventory` and `bv cross-pipe-association` are historical/public market analysis. They do not read or update Kolabi runtime state and must not be routed to live order or feed workflows.

## Inventory

- Fetch the current tradeable, non-expired Kraken crypto futures universe and refresh the live instrument/ticker snapshot.
- Exclude xStocks, forex, commodities, and other traditional-finance contracts by default.
- Enrich underlyings through CoinGecko, using the exchange reference price to reject implausible duplicate-symbol matches before choosing market capitalization.
- Cache completed one-minute candle pages in the documented SQLite cache. Reruns overlap and upsert the latest completed candle so provider corrections are captured without duplicating rows.
- Stop final publication when Kraken history is incomplete, while preserving successfully downloaded pages for resume.
- Keep full-precision identifiers, history bounds, and percentiles in CSV; use compact Org reports for operator inspection.

## Ranked Org Reports

When preparing `JOURNAL.org`, `REPORT.org`, or another operator report, distinguish these four rankings:

1. global CoinGecko market capitalization
2. global market capitalization of unique underlyings available through eligible Kraken contracts
3. raw Kraken 24-hour volume per contract
4. global CoinGecko 24-hour volume of unique eligible Kraken underlyings

State the ranking universe and unit in each heading. Put the exact source command before generated tables.

- Exclude `FI_`, `PI_`, and stablecoins when the requested universe is crypto assets rather than indices or cash-like instruments.
- Keep eligible `PF_` perpetuals and `FF_` fixed-maturity contracts in contract-level Kraken volume rankings when requested.
- Deduplicate BTC, ETH, SOL, and other repeated underlyings in market-capitalization and global-volume rankings; repeated `FF_` maturities must not multiply one asset.
- Kraken contract volume is not the asset's global volume, open interest, market capitalization, or guaranteed executable liquidity. CoinGecko global asset volume is not Kraken-only activity.
- Explain large capitalization/low Kraken volume and low capitalization/high Kraken volume as screening observations only. Contract design, venue concentration, maturity, incentives, market-maker activity, and mapping quality are possible explanations, not conclusions.

## Cross-Pipe Association

- Run only after the inventory cache contains the explicitly requested perpetual contracts.
- Reuse cached candles and fingerprinted per-symbol/window/beast thresholds; recalculate after candle append or correction.
- Treat directional density, balance, lift, risk ratio, risk difference, odds ratio, phi, and backward coverage as descriptive full-history statistics.
- Keep low-support candidates in complete CSV output but exclude them from rankings according to the command's support threshold.
- Record unresolved asset mappings and provider/cache fallback behavior instead of silently dropping instruments.
