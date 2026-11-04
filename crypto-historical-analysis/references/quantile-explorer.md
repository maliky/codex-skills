# Multiscale Quantile Explorer

Read current `DEV.org`, `SIMULATION.org`, `src/simulation_web/quantiles.py` and the affected static model/view modules before extending the explorer. This is a report reader and visualisation workflow; it does not require launching Kolabi orders or simulation workers.

## Preserve Measurements And Populations

The reader consumes existing report CSVs without recomputing their analysis. Preserve report family, instrument, source timeframe, observation window, population, sample support, source path/fingerprint and actual coverage. Requested date bounds do not prove effective data coverage. Keep rejected/ambiguous source attribution visible in diagnostics.

Beast populations are separate distributions; their quantiles cannot be pooled to reconstruct an overall percentile. Disabled/unmeasured windows are not missing UI features to fill with invented results. Preserve source fingerprints when caching: same-size file corrections must invalidate stale data.

Keep the project's accepted exploratory price-proxy policy and source provenance together. Surface an instrument/source distinction when it changes the conclusion or execution assumption, rather than repeating an immaterial caveat on every exploratory chart.

## Distinguish The Three Rates

| Quantity | Meaning and units |
| --- | --- |
| `Q_p(W)` | Amplitude quantile for percentile `p` and observation duration `W`, in log-bp. |
| `ΔQ/Δp` | Finite difference between adjacent measured percentiles at fixed `W`, in log-bp per percentile point; use the actual percentile spacing on 0–100. |
| `Q_p(W)/W` | Amplitude normalised by duration at fixed percentile, in log-bp per chosen time unit. |
| `ΔQ_p/ΔW` | Difference between measured windows at fixed percentile divided by their actual duration difference, in log-bp per time unit. |

A percentile slope is not a time derivative. A duration-normalised value is not the derivative between windows. With windows in minutes and a display unit of `u` minutes, time-normalised values and duration slopes scale by `u`; changing the display unit does not change the underlying comparison. Keep amplitude conversion `10000 * ln(high/low)` separate from ordinary percent returns.

## Missing Values, Interpolation And Display

Missing values interrupt curves and prevent adjacent slopes; do not bridge them with a distant quantile or substitute another percentile. Preserve measured zero; a logarithmic display needs a separate representation for non-positive values, not an invented epsilon. Interpolation must remain bounded by the supported measured domain and must not cross gaps.

Optional smoothing/window interpolation changes visual geometry, not the original measurements, finite-difference slopes or rankings. Retain full precision for calculations, differences, coordinates and selected values; round displayed labels/tooltips/tables to two decimals. Compare slopes using their actual interval widths rather than assuming equally spaced percentiles or windows.

## Code And Verification Routes

The reader is `quantiles.py`; shared quantitative rules live in `quantile-model.mjs` and `quantile-explorer-model.mjs`. Duration views use `quantile-window-relations.mjs`. Inspect the current free-3D versus linked/fixed-perspective views instead of imposing WebGL on every page. Preserve linked hover/pinned selection, keyboard navigation and mobile layouts when changing chart rendering.

Use affected `tests/test_quantiles.py`, the JavaScript model cases and the documented browser checks:

```bash
node --test tests/js/quantiles.test.mjs tests/js/quantile-explorer.test.mjs
RUN_QUANTILE_BROWSER=1 .venv/bin/python -m pytest -q tests/test_quantile_browser.py
```

Read CLI help for `serve-simulation --reports-dir` and the current environment default. For an authorised deployed verification, check both relevant pages and the actual served static modules; compare their hashes when diagnosing stale assets. `no-store` and `no-cache` can both prevent the stale-asset failure. Keep the existing private access policy. Report source/model/browser verification separately from deployment or historical-performance claims.
