# Host And Container PHP Maintenance

Use this reference for a requested PHP inventory, security patch or compatibility upgrade. Read the affected application/deployment notes and current sanitised intervention records under `/home/jil/sysadmin`. Historical versions, package counts and successful probes are evidence about that intervention, not today's runtime inventory.

## Establish The Whole Runtime Surface

- Inventory host CLI, CGI and FPM packages/pools plus PHP in running containers, including Apache modules, FPM and separate WP-CLI images. A host `php -v` result does not establish the version serving a containerised website.
- Map active Nginx routes, document roots, cron/worker invocations, container image IDs/digests, bind mounts and network/database dependencies. Identify current public, maintenance and standby modes before altering them.
- Confirm affected/fixed versions with current upstream, distribution and official image information. Distribution backports and mutable image tags require checking the actual package build and installed runtime. Treat a patch within a branch separately from a compatibility-tested branch upgrade.
- Inspect `tulearn` and `tuwp` deployment files for the current service names. Include every detected PHP service rather than assuming Moodle is the entire surface.

## Prepare The Scoped Change

Preserve verified database/application/deployment backups and rollback image references before the requested mutation. Use the configured application database account for a logical backup when root authentication is unavailable; do not invent a root password or expose environment contents.

If the selected incident response includes temporary isolation, record the exact Nginx and cron state before pausing public PHP work. Preserve an existing Moodle standby mode and restore the original schedule/routing rather than replacing it with a guessed default. A patch task does not itself decide to reopen a deliberately unpublished application.

Preserve local Moodle Ollama/Adaptable changes and required PHP extensions when rebuilding. Check code bind mounts after replacing directories: an existing container can retain the old mount and may need scoped recreation. Verify actual installed CLI paths independently of the web document root; the presence of a `public/` webroot does not imply every CLI script moved under it.

Inspect an APT lock's owning process. Wait for a real active updater; terminate only a confirmed stale process within scope. Do not remove lock files as a substitute for understanding the owner. Pin/rebuild the intended images, check their installed SAPIs, and recreate only affected services.

## Prove The Changed Services

For WordPress, check the serving PHP SAPI, homepage/login/assets, database access and WP-CLI separately. For Moodle, check FPM, extensions, login, schema/system checks, cron and required Ollama/network access. A system-check warning after deliberately paused cron can need a bounded cron run and schedule restoration rather than another code change; use supported options such as `--keep-alive=0` when appropriate to the installed version.

Validate Nginx before reloading, then check the expected public/auth/standby responses, relevant IPv4/IPv6 paths, container restart counts and logs. Use bounded follow-up monitoring proportional to the intervention. Keep backups until the recovery/retention decision is satisfied; do not turn a historical cleanup authorisation into a permanent deletion policy.
