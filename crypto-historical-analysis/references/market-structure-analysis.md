# Market Structure Analysis

Use this reference for `bv` threshold grids, beast sequences, fine/coarse pipe relationships, and popular-price analysis in `manalysis`.

## Shared Conventions

- The revived codes are `R/r=bear`, `N/n=dragon`, `P/p=sheep`, `L/l=bull`, and `Z/z=zebre`. Uppercase adds the command's same-beast amplitude percentile gate; lowercase is label-only.
- `timeframe` is the stored source-bar duration and rolling decision spacing. `window` is the observation duration used to form a pipe.
- Reject windows and associations that cross missing source timestamps.
- Learn amplitude thresholds independently inside each symbol, window, and beast unless the command explicitly documents another scope.
- Full-history frequencies and associations are descriptive. Predictive claims require a chronological holdout whose thresholds and selections were learned only from calibration data.

## Command Routes

- `threshold-grid`: calculate empirical log-bps cutoffs across many windows and beasts. Human Org tables use compact integer minutes and amplitudes; CSVs retain precise values.
- `pipe-distance`: match each qualifying coarse pipe to the latest qualifying non-overlapping fine pipe in the same continuous segment. In episode association mode, distinguish signal time, coarse start, and confirmation time.
- `pipe-predict`: compare contained and forward alignments. `contained` overlaps the target and is continuation analysis; `forward` shares no bars and is the forecasting alignment.
- `block-predict --descriptive-only`: count exact configurations and positional motifs on full history. Default predictive mode selects on calibration data and evaluates on purged holdout data with optional bootstrap intervals.
- `popular-prices`: score exact or round price levels from consecutive disjoint pipe triplets and produce reversal/touch rates. Preserve support counts when ranking rates.
- `popular-prices-cube`: produce compact multi-symbol, multi-window data for D3 or Observable. Select aligned coarser grids with integer `price_index` divisibility; never average neighboring price levels.

## Interpretation Guardrails

- Always report support alongside conditional probabilities, lift, risk ratio, or odds ratio; rare motifs can have unstable extreme rates.
- `P(J|I)` is conditioning, not temporal order. Define the event timing separately.
- Lift compares against unconditional baseline; risk ratio compares against decisions without the signal. Do not treat either as return or profitability.
- A median-derived association window is descriptive and can mechanically shape backward coverage.
- Keep exact commands before Org report branches so results remain reproducible.
