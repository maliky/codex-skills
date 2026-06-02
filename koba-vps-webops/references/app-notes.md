# App Notes

## TULearn / Moodle

Wrapper path:

```bash
cd /home/jil/tulearn
```

Common files:
- `README.org`
- `docker-compose.yml`
- `deploy/nginx/tulearn.koba.sarl.conf`
- `docker/php-fpm/Dockerfile`

Useful commands:

```bash
docker-compose build php
docker-compose up -d php
docker-compose exec -T php php /var/www/html/admin/cli/purge_caches.php
docker-compose exec -T php php /var/www/html/admin/cli/cron.php
```

Known recurring issues:
- PHP extensions missing from the image.
- Moodledata ownership or writeability.
- Host PostgreSQL access from the PHP container.
- Host Ollama access from the PHP container.
- Nginx rewrite cycles or wrong document root.

## TUWP / WordPress

Wrapper path:

```bash
cd /home/jil/tuwp
```

Useful commands:

```bash
docker-compose ps
docker-compose logs -f wordpress
docker-compose run --rm wpcli --info
docker-compose run --rm wpcli theme list
```

Do not run `docker-compose down -v` unless the user explicitly wants to destroy WordPress database data and uploaded files.

Recurring tasks:
- Nginx publication for `tuwp.koba.sarl`.
- WP-CLI user/page/menu setup.
- Theme activation and lightweight TU institutional styling.
- Checking broken theme assets through the public hostname.

## TUSIS Preprod

Working tree:

```bash
cd /home/jil/Tusis/Tusis_app
```

Useful commands:

```bash
docker-compose -f docker-compose-preprod.yml ps
docker-compose -f docker-compose-preprod.yml logs -f web db
docker-compose -f docker-compose-preprod.yml exec -T web python manage.py check
```

Use `tusis-admin-ui-engineering` when the issue is inside Django admin, permissions, templates, or tests. Use this skill when the issue is deployment, Nginx, TLS, container reachability, or public host behavior.
