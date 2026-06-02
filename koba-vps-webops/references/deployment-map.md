# Deployment Map

## Host Notes

Start with:
- `/home/jil/Sysadmin/README.org`
- `/home/jil/tulearn/README.org`
- `/home/jil/tuwp/README.org`
- `/home/jil/Tusis/Tusis_app/README.org`

These files contain host-specific command reminders and deployment assumptions. Prefer them over generic package docs when the task is about this host.

## Common Working Trees

- TUSIS app: `/home/jil/Tusis/Tusis_app`
- Moodle/TULearn wrapper: `/home/jil/tulearn`
- Moodle upstream checkout: `/home/jil/tulearn/moodle`
- WordPress/TUWP: `/home/jil/tuwp`
- General sysadmin notes: `/home/jil/Sysadmin`

## Common Services

- Nginx runs on the host.
- TUSIS preprod uses `docker-compose-preprod.yml`.
- TULearn runs PHP-FPM through Docker Compose and uses host PostgreSQL.
- TUWP runs WordPress through Docker Compose and uses WP-CLI through the compose stack.
- Some container-to-host flows use fixed bridge/gateway IPs rather than `127.0.0.1`.

## Safety

- Do not run destructive volume commands such as `docker-compose down -v` unless the user explicitly requests data removal.
- Treat database dumps, `.env` files, and passwords as sensitive.
- Prefer `nginx -t` before reloads.
- Prefer `docker-compose ps` and logs before recreating services.
