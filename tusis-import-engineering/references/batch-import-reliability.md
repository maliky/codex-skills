# Batch Import Reliability

Use this reference when large imports need bounded batches, rollback thinking, and confidence checks.

- use small bounded batches first
- keep reject logs stable and reproducible
- only promote batch size after duplicate/invalid rates are stable
- prefer deterministic recovery over partial auto-heal
