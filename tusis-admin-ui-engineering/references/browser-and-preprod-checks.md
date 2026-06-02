# Browser And Preprod Checks

## Selenium

- Use the system chromedriver when Selenium is required. The TUSIS repo notes that `/usr/bin/chromedriver` should be preferred over webdriver-manager defaults.
- Use Selenium for behavior that depends on browser rendering, form widgets, dynamic filters, or navigation.
- Do not use Selenium as the first check for pure Python admin configuration problems.
- Keep browser tests focused on one route or workflow unless the task is an explicit click audit.

## Local And Preprod Routes

Common TUSIS working tree:

```bash
cd /home/jil/Tusis/Tusis_app
```

Typical preprod compose file:

```bash
docker-compose -f docker-compose-preprod.yml ps
docker-compose -f docker-compose-preprod.yml logs -f web
docker-compose -f docker-compose-preprod.yml exec -T web python manage.py check
```

Run narrow tests inside the same environment that reproduces the bug when possible:

```bash
docker-compose -f docker-compose-preprod.yml exec -T web python -m pytest -q path/to/test.py
```

## 500 Error Triage

For browser-visible 500 errors:

1. Reproduce the URL with the same auth/role context if possible.
2. Check web logs before changing code.
3. Identify whether the failure is template rendering, admin queryset evaluation, permission logic, or deployment configuration.
4. Add or update a targeted test when the failure is code-level and reproducible.

If the failure only appears through Nginx or public hostnames, use `koba-vps-webops` for the deployment side.
