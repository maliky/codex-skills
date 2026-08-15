# Deployment Map

## Host Notes

Start with:
- relevant `.org` notes under `/home/jil/sysadmin`
- `/home/jil/sysadmin/users.org` when account ownership or user deletion is involved
- `/home/jil/tulearn/README.org`
- `/home/jil/tuwp/README.org`
- `/home/jil/Tusis/Tusis_app/README.org`

These files contain host-specific command reminders and deployment assumptions. Prefer them over generic package docs when the task is about this host.

## Common Working Trees

- TUSIS app: `/home/jil/Tusis/Tusis_app`
- Moodle/TULearn wrapper: `/home/jil/tulearn`
- Moodle upstream checkout: `/home/jil/tulearn/moodle`
- WordPress/TUWP: `/home/jil/tuwp`
- General sysadmin notes: `/home/jil/sysadmin`

## Common Services

- Nginx runs on the host.
- TUSIS preprod uses `docker-compose-preprod.yml`.
- TULearn runs PHP-FPM through Docker Compose and uses host PostgreSQL.
- TUWP runs WordPress through Docker Compose and uses WP-CLI through the compose stack.
- Some container-to-host flows use fixed bridge/gateway IPs rather than `127.0.0.1`.

## Account-Owned Deployments

Before removing a local account or account-owned app, audit:

- `systemctl` user/app services
- running processes
- `/srv/apps/<user-or-app>`
- Nginx enabled and available vhosts
- certificates and renewal config
- quotas, cron, logs, repositories, and exposed ports

Remove only resources owned by the targeted account or app. `userdel --remove` is not sufficient by itself and must not replace the dependency audit.

## Safety

- Do not run destructive volume commands such as `docker-compose down -v` unless the user explicitly requests data removal.
- Treat database dumps, `.env` files, and passwords as sensitive.
- Prefer `nginx -t` before reloads.
- Prefer `docker-compose ps` and logs before recreating services.
