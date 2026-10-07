# graph-bo-math Static Releases

Use only for the deployment/host side of the standalone graph. Its maintained sources, explicit Elize imports and protected BO boundaries are covered by `elize-teaching-engineering` and its [graph workflow](../../elize-teaching-engineering/references/bo-progressions-graph.md). Do not import teaching sources just to publish an existing graph revision.

## Inspect Before Publishing

- Recheck `AGENTS.md`, `README.org`, `deploy/publish.sh`, Git status/remotes and the requested action. “Commit and push to the VPS” means Git synchronization only; website publication must be explicitly requested.
- Known wiring: remote `jil@54.36.60.51:git/graph-bo-math.git`, branch `main`, VPS checkout `/home/jil/graph-bo-math`, public hostname `graph-bo-math.koba.sarl`. Verify rather than changing a different checkout/remote to match these notes.
- For an authorized release, validate `npm run build`, `npm run check`, `npm test` and `npm run test:browser`. Resolve any protected-source changes and stage only intended source files. Use `self-hosted-git-operations` for requested commit/push; compare local HEAD with the advertised remote `main` OID. Push success is not a release result.

## Publish and Verify

Run the inspected `deploy/publish.sh` only after release authorization. The current script requires a clean local checkout whose HEAD matches remote `main`, fast-forwards the clean VPS checkout to that revision, and refuses to overwrite an existing release directory. Do not bypass these guards or blindly rerun after a partial failure; inspect the exact revision, release directory and active link first.

The script builds/checks and transfers **only `site/`** to `/srv/apps/graph-bo-math/releases/<commit>/`, verifies release-file hashes, and atomically changes `/srv/apps/graph-bo-math/current`. It compares the public `https://graph-bo-math.koba.sarl/manifest.json` hash with the local manifest; a mismatch restores the previous release link, or withdraws an initial release with no predecessor. Existing releases remain available; do not remove them as incidental cleanup.

After success, confirm the published revision/manifest and run public browser checks with `GRAPH_URL=https://graph-bo-math.koba.sarl/ npm run test:browser`; use `CHROMIUM_PATH` for an installed browser if needed. Report Git OID, publication verification and browser outcome separately. A failed browser check after publication is not covered by the script's manifest-triggered rollback; investigate and obtain direction for any further state change outside the release request.

## Host Boundary and Recovery

The dedicated Nginx vhost serves `current`; no Python/Node production service is required. Inspect `deploy/graph-bo-math.koba.sarl.conf`, the actual enabled vhost, webroot `/var/lib/letsencrypt`, and the app's Certbot reload hook/renewal units when diagnosing TLS. Initial vhost/certificate installation is a separate, explicit host operation.

For an authorized rollback, identify a retained release, verify it with `deploy/verify_release.py`, record the current target, switch only this application's `current` link atomically, then check the public manifest and browser. Never infer release validity from directory existence alone.
