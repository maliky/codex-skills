# Graph BO Math Releases

Use for deployment and host wiring. Application sources, imports and editor/library behaviour belong to [graph-bo-math-engineering](../../graph-bo-math-engineering/SKILL.md). Inspect current `AGENTS.md`, `README.org`, `deploy/publish.sh` and `deploy/activate-release.sh`; Git synchronization alone does not publish the website.

## Release And Persistent State

- Verify the checkout and remote revision before release. Known wiring is branch `main`, remote `jil@54.36.60.51:git/graph-bo-math.git`, checkout `/home/jil/graph-bo-math`, and hostname `graph-bo-math.koba.sarl`.
- Under `/srv/apps/graph-bo-math/`, `releases/<commit>/` holds the built site and `api-releases/<commit>/` holds the Python server, pinned requirements and deployment configuration. Both bundles have verified manifests; `current` and `api-current` select compatible versions.
- `library/graphs.sqlite3`, `library/assets/` and `library/backups/` persist outside releases. Use the SQLite backup API through `server.manage` for a consistent database backup, and retain the immutable asset directory with it. A code rollback must preserve saves created since deployment.
- Nginx serves the site and proxies `/api/` to the Unix socket of `graph-bo-math-api.service`. Inspect the dedicated service, vhost and Certbot renewal configuration when diagnosing host issues.

## Publication And Verification

Complete the repository's build, check, unit and relevant browser gates for an authorised release. The publisher requires clean checkouts and matching local/advertised `main`, fast-forwards the VPS checkout, and refuses existing release directories. On the VPS itself, the supported entrypoint is `GRAPH_DEPLOY_LOCAL=1 bash deploy/publish.sh`. Inspect partial results before retrying a failed publication.

Activation verifies both bundles, prepares the API environment, backs up SQLite and registers the catalogue/assets before switching service code. It checks socket and public API readiness before exposing the new frontend. Verify both active targets, the public manifest, `/api/health`, library access and the changed interaction. Public browser checks use `GRAPH_URL=https://graph-bo-math.koba.sarl/ npm run test:browser`, with `CHROMIUM_PATH` when needed.

The activation failure handler restores previous site/API links, service configuration and Nginx after a failed switch while retaining library data. It does not handle a browser check run after the script has exited; inspect the actual active targets and application state before further recovery.

## Coordinated Rollback

For an authorised rollback, verify both retained bundles with `deploy/verify_release.py` and confirm that the selected API understands the current library data. Record current targets, restore the compatible site/API pair and required service/vhost configuration, then check the service, Nginx, public manifest, API and library. Do not restore an older database as part of an ordinary code rollback or delete releases/backups incidentally.
