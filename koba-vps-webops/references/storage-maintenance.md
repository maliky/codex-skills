# Storage Maintenance

Use current filesystem measurements and process/deployment references. Read the relevant system/application notes, including previous sanitised cleanup reports, but do not reuse old candidate IDs or free-space totals as current facts.

## Inventory And Authority

Separate host free space, filesystem quota and per-account usage. `df -hT`, `findmnt`, `docker system df -v`, journal usage and scoped `du -x` provide different evidence. Unprivileged permission failures on a private directory do not prove it is empty. Inspect the selected candidate objects before the authorised cleanup; a broad space-saving goal does not identify expendable databases or volumes.

Record the current running containers/services, mounted volumes, protected models/releases and required evidence. Candidate estimates are not additive: Docker layers and hard-linked files can be shared. Report actual available-byte change after completion, along with service continuity checks.

## Object-Specific Checks

| Candidate | Evidence needed before removal or change |
| --- | --- |
| Docker images | Exact IDs/digests, references from active/stopped containers and selected rollback needs. Removing tags can leave digest-only images; inspect those separately. Avoid broad `docker system prune` or forced removal. |
| Docker volumes/databases | Explicit ownership, mounts, project references and retention decision. An unattached volume is not automatically disposable. |
| Temporary PostgreSQL clusters | Directory age, PID/process ownership, sockets/ports, mounts and current test references. A directory under `/tmp` can still contain an active cluster. |
| Codex releases | Active launcher targets, process executables and daemon fallback references. Older version numbers alone do not establish inactivity. Preserve session/runtime state unless it is specifically in scope. |
| Application logs | Retention and debugging/import/reconciliation value. TUSIS logs can contain unique evidence; preserve tracked sentinels such as `logs/.gitkeep`. |
| Rollback backups/images | Successful post-change validation and the user's applicable retention/removal decision. Keep a sanitised audit when private backup artifacts are retired. |
| APT cache | Completion of active package operations and their locks; clearing cache is separate from removing installed packages. |

For a Docker image cleanup, `docker image ls -f dangling=true` identifies images without tags, not images without users. Compare each candidate's full image ID with the `.Image` field of **all** running and stopped containers; retain every referenced ID and the chosen rollback tags. Remove reviewed IDs individually without `--force`. Treat unused build cache as a separate target: confirm its active count and authorisation before a builder-cache prune, and leave volumes and containers out of that command. Image unique-size sums and Docker's reclaim estimate can differ from the actual `df` change because layers are shared.

For Codex release cleanup, check `current` targets, daemon fallback, and process executable, working-directory, and open-file references on the **host**. A sandboxed `/proc` view may omit live host Codex processes. Do not delete a release used by a live process, even when its version is old; a deleted executable can remain open until that process ends. A broad disk-cleanup request does not identify exact session records for deletion: use `codex-session-cleanup` for an explicitly targeted session. Stale plugin staging can be removed only after checking age, configuration/symlink references, and live process use.

## Repeated Growth And Shared Files

For a long-lived cron log, truncate in place when chosen so inode/ownership and open writers remain intact; configure a suitable rotation policy rather than repeatedly unlinking it. Inspect existing logrotate rules first. Journald retention/drop-ins and vacuuming should target the intended budget without discarding unrelated evidence merely to match a past example.

Ollama blobs under user and service stores may contain identical bytes but have different ownership or active consumers. Check hashes, filesystem, permissions, open files and model-API availability before an explicitly chosen deduplication. Preserve required paths and models and verify availability afterward; do not infer a general hard-link policy from one successful intervention.

After cleanup, compare the same baseline services, volumes, active release/model references and disk metric. Explain shared-layer or inode effects if measured reclamation differs from the preview. Do not claim a service remained healthy from a container count alone.
