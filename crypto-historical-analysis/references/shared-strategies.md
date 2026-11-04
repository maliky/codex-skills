# Shared Strategies Between Manalysis And Kolabi

Use this reference when maintaining shared strategy sources or repairing the paths used by replay, the simulation UI and Kolabi. Inspect both checkouts and `manalysis/strategies/README.org`, `scripts/link-kolabi-strategies.py`, and the current policy module before editing; dated descriptions can describe superseded strategy versions.

## Ownership And Loading

- Keep shared Org, JSON and Python files as regular tracked files in `manalysis/strategies/`. Kolabi's `orders/` contains ignored relative links for those individual files, for example `cfunc.py -> ../../manalysis/strategies/cfunc.py` in sibling checkouts.
- Retain Kolabi-specific strategies, demo files, `rfunc.py`, and `tfunc.py` in their existing locations unless the task explicitly changes their ownership. Do not replace the entire `orders/` directory with a link or introduce another synchronised copy.
- Edit the canonical source. Some editors save by replacing a symlink with a regular file, silently recreating divergence; check link targets after editing through a Kolabi path.
- The native policy loader follows `orders/cfunc.py`. Manalysis and its workers use `KOLABI_STRATEGY_CFUNC` pointing at the canonical `strategies/cfunc.py`; verify the actual worker environment as well as the interactive shell.
- Point the simulation UI's strategy directory at the canonical directory. Preserve its path-containment checks: an old UI rooted at `kolabi/orders/` can correctly exclude links pointing outside that directory. Repair the configured source root rather than weakening those checks.

## Migration Helper

From the manalysis checkout, using its project interpreter:

```bash
.venv/bin/python scripts/link-kolabi-strategies.py
```

The default is a dry-run. Inspect the named winners and both dirty trees before applying an authorised migration with `--apply`; use `--kolabi-dir /path/to/kolabi` for a non-sibling checkout. The helper selects shared `.org`, `.json` and `.py` files, excludes README/editor files, preserves selected bytes, installs relative links, and prints a temporary recovery directory with displaced copies and `receipt.json`.

The helper's newest-mtime rule serves the requested local deduplication. Filesystem mtime after a clone, checkout or restore is not evidence of which Git revision is authoritative. Inspect conflicting contents/history before accepting that selection; do not silently merge policies or normalise strategy bytes during link repair. Equal-mtime divergent contents, editor locks, unrelated links, non-regular canonical sources, or changes after planning block the migration and need resolution.

After applying, confirm that the canonical files are still regular files, each link resolves to the intended canonical path, and contents match the selected source. A second dry-run should report `0 links planned`. Keep the printed recovery receipt available; a successful link operation does not imply a commit, push or service restart.

## Other Hosts And Running Services

An ignored Kolabi link is not delivered by pulling Kolabi. On another host, verify both repository revisions and the canonical shared files, then recreate per-file links with the same helper as authorised. Confirm resolved paths and hashes, and check that the installed Kolabi parser/runtime supports the strategy's grammar. Shared files only become available through Git once the relevant manalysis changes are committed and published within the user's requested scope.

Check active UI/worker units, process arguments, working directory and `KOLABI_STRATEGY_CFUNC` when diagnosing catalogue or policy differences. Updated service templates alone do not update active units or processes. Perform installation/restart only when deployment is part of the requested work, then verify the running paths again.

## Replay And Execution Boundaries

For grammar and virtual order migrations, use [strategy grammar and demos](../../kolabi-multi-exchange-adapters/references/strategy-grammar-and-demos.md). Validate the parsed canonical files and policy registration with the matching Kolabi checkout. A virtual voter can feed a separate real follower; a file containing virtual voters is not necessarily safe to launch as a purely virtual strategy. Keep local virtual confirmations separate from real fills and PnL.

Deterministic parser/replay tests validate technical behaviour. Historical performance claims additionally need the recorded dataset window, instrument metadata, execution assumptions and actual replay results. Do not report profitability or a completed historical run from link convergence or fixture tests.
