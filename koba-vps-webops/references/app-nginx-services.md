# App Nginx And Service Wiring

Use this reference for small app deployments on the Koba VPS, especially Flask/static sites, schedule services, and one-off `koba.sarl` subdomains.

## Nginx Files

- Prefer app-specific deploy notes and `deploy/nginx/` templates when they exist, but avoid keeping duplicate conflicting config files.
- Use an exact `server_name` for the hostname; do not rely on wildcard matches for production-facing subdomains.
- When binding upstreams, use the host IP or expected bridge/gateway address from local notes instead of guessing that `127.0.0.1` works from every context.
- Run `nginx -t` before reloads and verify the exact public hostname after changes.

## 502 After Reboot

Diagnose in this order:

1. confirm DNS and Nginx vhost selection
2. confirm the service, screen, systemd unit, or Docker Compose app is running
3. confirm the upstream port/socket is listening
4. inspect app logs before recreating services
5. reload Nginx only after config validation

## Operator Constraints

- If the user says not to change a screen session, do not attach, kill, or rename it; provide a command or wrapper instead.
- For tiny apps, a repo-local CLI wrapper that starts the service can be preferable to undocumented manual commands.
- Keep generated local deployment files out of git when the repo pattern says they are host-specific.
