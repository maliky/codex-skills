# Startup recovery

## Locate the failure

For SSH work, separate connection, authentication, shell readiness, and Codex startup. A local sandbox denial is not evidence that the remote host is down. Allow for a slow authenticated login and reuse an established diagnostic connection rather than repeatedly paying the login delay. Bound probes and keep the user informed while waiting.

Resolve the actual launcher with `command -v`, symlink inspection, and file-type detection. Read a launcher only after establishing that it is text; do not run `head` on a native executable. Record CLI and managed-daemon versions separately. Different versions are a clue, not proof of an incompatibility. Inspect the installed CLI help for supported diagnostics, daemon management, and bypass options.

Reproduce interactive startup in a terminal without submitting project work. If Screen is involved, list sessions and map window processes to working directories; prefer a read-only window query or a private temporary hardcopy over detaching the user's terminal. Limit output to the relevant error, and preserve any unsent draft before an authorized restart.

Inspect only relevant daemon errors and runtime metadata. Avoid dumping authentication files, whole environments, full configuration, or entire transcripts. Confirm the effective `CODEX_HOME`, database location, environment overrides, launcher arguments, and project configuration for the intended working directory. Changing the global configuration may not control the actual launch if another layer overrides it.

## Classify database and ownership evidence

| Observation | Next check |
| --- | --- |
| Database is locked | Identify the exact path and open handles, process namespace, filesystem, and possible owners on other nodes. |
| Database disk image is malformed | Retain the exact Codex error; inspect a safe snapshot with a compatible SQLite tool if integrity analysis is needed. |
| Fresh database fails with disk I/O errors | Check storage type, permissions, available space, quotas where applicable, and local-disk behavior before repeating resets. |
| Daemon is not ready | Inspect its startup error and verified process identity; a PID file alone does not establish a live daemon. |
| Session backfill or migration is running | Identify whether work is progressing or another initializer owns it; do not edit migration markers or delete history merely to skip the wait. |

Use mount information to distinguish local storage from NFS or other shared filesystems. Local `/proc`, `lsof`, or `fuser` checks cannot exclude a writer on another node. Empty or old lock files do not establish that locks are stale. Do not unlink or rename a potentially held lock; the owner can retain the original inode while another process locks its replacement.

Check the SQLite tool's version and capabilities before interpreting its output. A missing Python `_sqlite3` module is a tooling failure, and an old SQLite parser rejecting a newer schema is not proof of database corruption. Use a read-only connection or supported consistent snapshot for inspection; do not copy an actively written database alone while ignoring its journal or WAL. Probe schema before considering a database repair.

Record what is known separately from hypotheses. A failed update may have encountered an existing database problem. Successful operation on local disk supports a storage-related diagnosis, but does not identify the exact event that corrupted the old database.

## Choose the smallest effective recovery

### Restart or bypass the daemon

Prefer the installed product's supported stop/restart commands when the daemon is the failing component. Verify process identity and affected sessions before termination; recheck ownership before escalating an unresponsive process. Do not use broad process-name kills. An existing restart authorization is sufficient within its established scope.

When available, test `--no-daemon` to distinguish daemon readiness from runtime initialization. If both paths return the same database error, address storage or database state. Keep bypassing the daemon a targeted workaround, and disclose it if retained in the final launcher.

### Put SQLite state on suitable local storage

If the evidence implicates shared-storage locking or I/O, inspect support for `sqlite_home` in the installed release and choose an owned, private directory on a verified local filesystem. Check existing path ownership, symlinks, permissions, and available capacity before use. Prefer durable local storage; if temporary storage is necessary, establish its cleanup and reboot behavior and report the persistence limitation. A path named `/SCRATCH` or `/var/tmp` does not itself establish locality or durability.

Test the override for one launch before making it persistent. Verify that the database files actually appear at the intended path, including when launched from the user's project directory. Treat a successful database creation as intermediate evidence; complete session initialization must still succeed.

### Isolate a fresh runtime when history is unnecessary

Use a separate, owned `CODEX_HOME` when the user wants a fresh usable session and existing state is damaged, contested, or blocks migration. Keep the original runtime available; isolation does not require moving all histories, indexes, writer locks, and SQLite stores aside. If the user needs a particular old session, explain that isolation establishes fresh startup but does not fulfill resume recovery.

Carry forward only the needed configuration and authentication through the supported mechanism. Protect credential permissions, never print credential values, and account for the lifetime and accessibility of any source used through symlinks. Recheck security and model settings rather than bypassing them as part of recovery. Choose explicitly which skills and rules need to remain available.

Ensure the isolated runtime also uses its intended SQLite directory; a project configuration or existing launcher can redirect it back to the troubled store. Do not hardcode a historical account, release, hostname, or temporary directory from a previous incident.

### Make the working launch usable

Persist the tested configuration only when needed for the requested normal launch. If a wrapper is necessary, preserve the original launcher or symlink target, forward arguments and signals correctly, and verify the executable exists. Check how the wrapper interacts with the installed updater rather than assuming it will survive an update. Provide a rollback path and make its runtime-directory initialization and persistence behavior explicit.

Do not let diagnostic experiments silently become permanent settings. Restore superseded changes after verifying the chosen solution. Retain narrowly scoped recovery backups without expanding a runtime repair into history cleanup.

## Acceptance

- Start the user's normal command in the intended directory and confirm session initialization finishes; a welcome screen still loading is insufficient.
- For a fresh-start request, open a new session. For resume recovery, open the exact requested session without resubmitting queued work.
- When end-to-end interaction is within scope, request one short reply with no tools or file changes; otherwise report that model interaction was not tested.
- Check the effective runtime/database paths. A compatible `PRAGMA quick_check` may supplement startup verification, but cannot replace it.
- Close only diagnostic processes created for the investigation, or leave a clearly named detached session when that is useful to the user. Report any daemon bypass, local-only state, temporary-storage lifetime, and rollback location relevant to continuing use.

## Product reference

The [official configuration reference](https://developers.openai.com/codex/config-reference/) documents `sqlite_home`. Verify current documentation and installed help when applying this guidance; daemon command surfaces and storage schemas can change independently of this skill.
