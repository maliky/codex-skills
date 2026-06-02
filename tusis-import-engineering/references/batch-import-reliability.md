# Batch Import Reliability

Use this for large imports where one bad row can block confidence.

- use small bounded batches first
- keep reject logs stable and reproducible
- only promote batch size after duplicate/invalid rates are stable
- prefer deterministic recovery over partial auto-heal
