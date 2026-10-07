# Close-Only Intrinsic-Time Calibration

Use for the agreed descriptive `manalysis` research protocol, not trading decisions. The inspected 2026-10-06 `DEV.org` entry remains a TODO plan: do not claim a calibration CLI or measured deltas already exist. Recheck the current source/help and task status before implementation; `threshold-grid` and `popular-prices` count different phenomena. Do not traverse an explicitly excluded `These/` folder.

The ADA task targets 2, 3, 5, 7 and 13 confirmed directional changes per 20 elapsed hours, up/down combined. One confirmation is not a round trip, overshoot, trade entry or amplitude exceedance. Other instruments or targets require the user's requested scope. Inversion of a fitted count law is this local research proposal, not a complete method supplied by a cited paper.

## Freeze the Input

- Resolve the data-host checkout, `.python-version` and code revision. Read `python beast_variation.py kraken-futures-inventory --help`; obtain the actual cache with `kraken_futures_inventory.default_cache_path()` rather than a hardcoded XDG path. Inspect SQLite read-only before scheduling acquisition.
- Use the archived `PF_ADAUSD` perpetual identity and `trade/1m` candle closes only. Do not substitute spot `ADAUSD`, ticks, mark/index prices or bid/ask mid. A close becomes available at the candle's opening timestamp plus one minute; no intraminute reversals are inferred.
- Reuse existing data. Any necessary acquisition is a separate, scoped stage using the verified inventory interface, limited to `--symbols PF_ADAUSD --acquire-only` with explicit cache/output. Offline inventory use requires an existing `inventory_snapshot.json` and matching cache fingerprint, not a fresh empty output directory.
- Record the exclusive UTC cutoff, effective bounds, contract/source/timeframe, metadata, fingerprint and code revision. Audit finite positive prices, duplicates/corrections, order, gaps and coverage. An existing zero-volume candle is an observation; a missing minute is not. Never forward-fill missing prices.

## Causal Sampler

- Fractional `d=0.01` means 1%. In rising mode update `H=max(H,p)`; confirm a fall at `p <= H*(1-d)`. In falling mode update `L=min(L,p)`; confirm a rise at `p >= L*(1+d)`. Switch mode and reset the extremum to the observed price after confirmation. Record direction, confirmation timestamp, extremum and its timestamp; never backdate the decision to a retrospectively known peak.
- Specify causal initialization per contiguous segment, such as rising mode at its first close with the first confirmation excluded as warmup. Report delta-dependent warmup time. Reset on actual gaps, not at every 20h bucket; count at most one confirmation per observed close, even after a large jump.
- A symmetric log-bps sampler is a separate convention: `b=10000*abs(ln(p/extremum))` corresponds to different up/down fractional percentages. Do not equate it exactly with fractional `d` or reuse high/low amplitude thresholds. Optional synthetic OHLC/OLHC sensitivity is separate from observed close-only results and is not a guaranteed bound on true events.

## Calibrate, Invert and Replay

- Declare chronological calibration/holdout bounds, elapsed-20h windows and coverage rules before fitting. Select on calibration a logarithmic grid of at least eight distinct deltas bracketing the requested rates, compatible with data/tick resolution. Retain every attempted threshold; do not tune on holdout.
- For each delta count eligible confirmations `n(d)` over eligible observed hours `T(d)`, excluding gaps/warmup: `N20(d)=20*n(d)/T(d)`. Compare deltas on common temporal coverage and keep per-window counts, up/down counts and segment coverage. Keep zero-count observations; flag insufficient support and omit unusable points from a log fit without invented pseudo-counts.
- Fit `N20(d)=A*(d/d0)^alpha`, with `d0=0.01`, `A>0`, `alpha<0`. Inspect residuals, curvature, supported range and temporal stability rather than imposing `alpha=-2` or describing the relation as a `1/f` spectrum.
- Invert for each target: `d_k=d0*(k/A)^(1/alpha)`. Replay the sampler at each exact resulting threshold. Flag unbracketed targets/extrapolation; if the fit is inadequate, say so and label any empirical interpolation separately.
- Freeze deltas before holdout replay. Past prices may initialize state at the split, but holdout events must be confirmed after it. Report achieved rates, target error, coverage and dispersion. For uncertainty, resample time blocks of counts/exposures and refit coefficients; do not splice price blocks into artificial jumps. Record block size and seed.

## Verification and Handoff

Test constant/monotone series, exact-threshold equality, known alternating changes, a large jump, duplicates, gap resets, 20h boundaries, chunk resumption, batch/stream parity and unit/timestamp conventions. The calibration is not complete until it runs on the actual data host and all five exact deltas are replayed.

Deliver a manifest, data audit, grid/coverage, coefficients/diagnostics and five-target CSV under a scoped report directory such as `reports/intrinsic-time-pf-adausd/<run>/`. Include fractional/percent convention, calibration and holdout rates, uncertainty and status. Start the Org report with the actual executed command and a full UTC date. Keep bulky events/data out of Git. Voting/quorum, support/resistance, `-u/+u` exposure, market entry and changes to live Kolabi remain separate work.
