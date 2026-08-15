# Diagnostic Ladder

## Disk Pressure

When the host is nearly full, refresh live sizes before answering. Start small and resumable:

```bash
df -hT
docker system df -v
journalctl --disk-usage
du -h -d 1 /home/jil /var/log 2>/dev/null
```

Rank concrete reclaim targets sized to the user's goal. Common buckets on this host include unused Docker images, `/home/jil/.ollama`, `/home/jil/.codex`, `/home/jil/.pyenv`, `/var/cache/apt/archives`, and large files under `/var/log`. Do not delete caches, images, logs, or volumes until the user chooses the target or explicitly authorizes cleanup.

For per-account space questions, distinguish host free space from quota:

```bash
findmnt -no SOURCE,FSTYPE,OPTIONS /
quota -s -u USER
sudo -n du -x -s -h /home/USER
```

Use read-only `sudo -n` first. If quota applies, answer with quota, current usage, and remaining quota rather than only global filesystem free space.

## DNS

Check the public name first when the user reports browser failures:

```bash
host example.koba.sarl
host example.koba.sarl 1.1.1.1
host example.koba.sarl 8.8.8.8
```

If DNS points elsewhere, fix DNS before changing Nginx or app code.

For OVH `koba.sarl` records, `subDomain` is relative to the zone. Use labels such as `app.ent.csrs`, not full FQDNs. After updates or creates, refresh the zone and query authoritative and public resolvers:

```bash
sudo ovhcloud domain-zone refresh koba.sarl
host LABEL.koba.sarl dns200.anycast.me
host LABEL.koba.sarl ns200.anycast.me
host LABEL.koba.sarl 1.1.1.1
host LABEL.koba.sarl 8.8.8.8
```

`ent.koba.sarl` may be a CNAME to `koba.sarl.` while deeper names are DNS-only A records. DNS success does not configure Nginx, TLS, WebSocket forwarding, or the app.

## Nginx

Inspect the app's generated deploy file and the host-enabled file. Validate before reload:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

When a public site returns 404 but the container is healthy, suspect server_name, enabled vhost, proxy_pass, or path/root mismatches.

## TLS

For certificate name errors, check both the certificate file and what the public socket serves:

```bash
sudo openssl x509 -in /etc/letsencrypt/live/HOST/fullchain.pem -text -noout
echo | openssl s_client -connect HOST:443 -servername HOST 2>/dev/null | openssl x509 -noout -subject -issuer -ext subjectAltName
```

If the served certificate is wrong but the file is right, suspect the active Nginx server block.

## Docker Compose

Run from the app wrapper directory:

```bash
docker-compose ps
docker-compose logs -f SERVICE
docker-compose up -d --force-recreate SERVICE
```

Use the compose file named by the app notes. For TUSIS preprod, include `-f docker-compose-preprod.yml`.

## Container-To-Host Networking

Inside containers, `127.0.0.1` means the container, not the host.

Check whether the compose file uses `host.docker.internal`, `extra_hosts`, or a fixed bridge gateway. For PostgreSQL, also check `pg_hba.conf` allows the container subnet.

Use app-native probes when possible:

```bash
docker-compose exec -T php php -r 'echo file_get_contents("http://HOST_OR_GATEWAY:11434/api/tags");'
docker-compose exec -T php php -r 'var_dump(pg_connect("host=HOST dbname=DB user=USER password=PASSWORD"));'
```

Avoid hardcoding a new subnet until you inspect the current compose network.
