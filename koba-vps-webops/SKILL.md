---
name: koba-vps-webops
description: "Use when operating, debugging, or updating Koba VPS web deployments and host wiring, including koba.sarl subdomains, OVH DNS records, Nginx vhosts, small app service wrappers, certbot or Let's Encrypt certificates, DNS or CNAME/A-record checks, Docker Compose web apps, host-to-container networking, PostgreSQL access from containers, account-owned deployment retirement, Moodle/TULearn, WordPress/TUWP, TUSIS preprod deployment status, disk or quota triage, and public 404/500/SSL failures."
---

# Koba VPS WebOps

Use this skill for host-level web operations on the Koba/TU VPS where the core issue is deployment, DNS, Nginx, Docker Compose, TLS, service wiring, or container-to-host connectivity.

Do not use it as the primary skill for application-domain fixes inside TUSIS, Kolabi, or TU curriculum sources. Use the relevant domain skill first, then use this skill when the failure crosses into deployment or host runtime.

## Default Workflow

1. Identify the app and hostname: TUSIS/preprod, TULearn/Moodle, TUWP/WordPress, or a general `koba.sarl` service.
2. Check local project notes before editing:
   - relevant notes under `/home/jil/sysadmin`
   - `/home/jil/sysadmin/users.org` for account-owned service cleanup
   - app-specific `README.org`
   - app-specific deploy or compose files
3. Diagnose in layers:
   - DNS resolves to the expected host
   - Nginx config is selected and valid
   - TLS certificate matches the hostname
   - Docker or service process is running
   - container networking reaches host services such as PostgreSQL or Ollama
   - app logs explain any remaining 404/500
4. Make the smallest config change that fixes the failing layer.
5. Verify with the exact public hostname or local bypass used to reproduce the issue.

## References

- Read [deployment-map](references/deployment-map.md) for host paths, app names, and common command routes.
- Read [diagnostic-ladder](references/diagnostic-ladder.md) for disk, quota, DNS, Nginx, TLS, Docker, and container networking checks.
- Read [app-notes](references/app-notes.md) for Moodle/TULearn, WordPress/TUWP, and TUSIS preprod specifics.
- Read [app-nginx-services](references/app-nginx-services.md) for small app Nginx files, exact host matching, service wrappers, and 502-after-reboot checks.
