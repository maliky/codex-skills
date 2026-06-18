# Demo And TSV Workflow

Use this reference for cross-exchange demos, minimal working examples, TSV grammar, and operator-facing commands.

## Demo Guardrails

- Treat demo, sandbox, and testnet credentials as sensitive. Do not print or commit API keys, secrets, tokens, or `.env` contents.
- Confirm the selected environment before any command that can place, cancel, or close orders.
- Reset public and private demo databases only when the user explicitly wants a clean demo state.
- Prefer bounded MWE commands over broad live runners when proving a new adapter path.
- Keep demo key names exchange-specific and explicit. Recent local convention used short exchange families such as Kraken futures/spot and BitMEX/Binance demo variables; map them in configuration code rather than scattering raw env names across adapters.
- Report missing demo credentials as setup gaps without exposing names plus values. It is acceptable to mention the variable names needed, but never echo secret contents.

## TSV Grammar Notes

Recent multi-exchange work favored compact, explicit columns:

- use `qty`, not `quantity`
- use `exchg`, not `exchange`
- ignore empty columns instead of treating them as meaningful strategy input
- require explicit `atype` when the order/action type affects behavior
- allow comment/header context where the parser already supports it, but keep the first actionable row strict enough to catch swapped fields such as `qty` and type values
- keep symbol notation exchange-aware, for example a `bmm_ada`-style fixture must make the target exchange and product family unambiguous

Keep TSV parser changes backward-aware: report any intentionally dropped alias and add parser tests for both accepted and rejected rows.

## MWE Procedure

1. Identify the strategy TSV or fixture, such as a cross-exchange `bmm_ada`-style example.
2. Verify exchange-specific env selection and DB URL before running.
3. Run the smallest command that exercises order creation, feed observation, and cleanup.
4. Inspect operator logs for exchange, product, order id, client id, and normalized status.
5. Cancel or close demo orders through the same runtime-mediated path used by normal operations.

## Repository Hygiene

- Do not track ad hoc live order files by default. Prefer tracking only demo strategies, examples, and documented fixtures such as `EXAMPLE.org`.
- Keep branch names and documentation aligned when merging multi-exchange work back to development branches. Record the fixture and exchange coverage in `README.org` or the nearest project runbook.

## Report Back

Lead with the exact command or fixture, the selected exchange environment, and whether the run proved parser, adapter, feed, or runtime behavior.
