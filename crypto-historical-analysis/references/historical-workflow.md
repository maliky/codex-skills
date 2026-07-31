# Historical Workflow

Use this reference for crypto historical download and amplitude-analysis work.

## Repo Boundary

- `DataFetchers/historical_prices` is the active base for unified historical download work.
- `kolaBiBot/tree` is live/current data infrastructure and should stay separate from deep historical backfill.
- The standalone historical repo lives at `/home/jil/hprices`.
- The VPS remote convention is `vps` with a bare repo under `~/git/<repo>.git`; for this repo the retained target is `jil@54.36.60.51:git/historical_prices.git`.

## Provider Role

Use `historical_prices` for historical data acquisition across providers such as:

- Kraken
- BitMEX
- CoinGecko
- Binance

Prefer the provider path that gives the deepest precise history available, with at least one-minute bars when possible.

## Analysis Stage

- Use `/home/jil/manalysis/beast_variation.py` for SQLite-backed amplitude analysis.
- Keep downloader output and analysis/report generation as separate stages.
- The user’s preferred metric is non-directional amplitude in log basis points.
- Do not split positive and negative movement unless the user reopens that scope.
- For one-minute bars and `--window 1min`, the expected one-bar amplitude target is `ln(high / low) * 10000`.

## Journal Threshold Reports

- In `/home/jil/manalysis`, `JOURNAL.org` is authoritative for Beast Amplitude Thresholds.
- Parse only from `* Beast Amplitude Thresholds` through `* Full-History Distribution Reports`; trim Org-table whitespace before counting rows.
- Expected full set: 2,040 rows = 12 asset/window reports x 5 beasts x 34 frequencies.
- `tmp.org` is the separate ASCII-chart artifact, not the source table.
- For adjacent threshold charts, compute raw integer differences as `T(next lower tail frequency) - T(x)`, for example `T(.24)-T(.25)` plotted above the `.25` mark.
- Keep chart bands separate for readability: `0.25-0.10`, `0.10-0.01`, and `0.010-0.001`.
- If `tmp.org` is missing from `/home/jil/manalysis`, check `/home/jil/.local/share/Trash/files/tmp.org` before assuming it was never created.

## Commands And Checks

- `beast_variation.py` is the current entry point for `ingest`, `summary`, `freq`, `tail`, `threshold`, and `report`.
- If compile/import checks hit a cache path failure in `MarketAnalysis`, set `PYTHONPYCACHEPREFIX=/tmp/...`.
- If an ad-hoc direct import fails while logic looks correct, retry with the module inserted into `sys.modules` before changing analysis code.

## Failure Patterns

- Do not collapse historical fetchers into `kolaBiBot/tree`; that boundary was explicitly rejected.
- If `git -C DataFetchers/historical_prices` says it is not a Git repository, inspect the folder directly because it may sit outside the current checkout root.
- If `--window 1min` yields no samples on one-minute bars, check whether rolling logic still requires two samples; one-bar amplitude windows need `min_periods=1`.
