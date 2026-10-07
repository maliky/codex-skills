# Session lock recovery

Resolve the exact session and obtain the resume error before choosing a repair. Inspect the installed CLI help and current storage schema; version-specific filenames and commands are clues, not stable APIs.

## Establish ownership

- A writer-lock file may be empty and old while still representing a live kernel lock. Its age, size, and a rollout ending in `task_complete` do not prove that its owner has exited.
- Check the actual process namespace. Sandboxed `ps`, `lsof`, and `fuser` may see only sandbox processes; empty results there cannot establish absence of a host owner. Use an approved host-visible diagnostic when necessary and explicitly report unresolved visibility.
- Inspect the exact lock path with host-visible open-file and lock information, including deleted inodes where relevant. Tie any PID to the target thread before acting. Do not infer that an idle CLI or app server has released its writer lock.
- A missing background daemon does not exclude an ephemeral CLI/app-server owner. Database integrity and unarchived status likewise do not prove resumability.

## Repair and verification

Prefer the installed product's supported release/close mechanism. If the exact owner is an obsolete process and stopping it is within the requested repair, close it gracefully; shared servers may own unrelated sessions and need narrower handling.

For a suspended owner (`T` in the host process state), first map all its thread locks and helper processes, including Guardian review threads. Recheck PID identity, start time, and lock ownership immediately before signaling; never reuse a PID from a prior report. A stopped process may need TERM followed by CONT to handle termination. Signal only the verified owner, wait a bounded interval, and inspect its exit and remaining holders. Do not kill a shared server or escalate to KILL merely because it also owns the target lock.

Do not unlink or rename a potentially held lock: the existing owner can retain the old inode while a second writer locks a new file at the same path. Removing an empty lock is not proof of unlocking. If a previous attempt already unlinked it, investigate remaining open/deleted handles before permitting another writer.

Only perform a filesystem cleanup when ownership and the implementation's lock semantics establish that it is necessary and safe. Keep conversation records intact. Probe database schemas and back up affected records before any independently justified database repair; do not rewrite history merely to clear a runtime lock.

Verify by successfully opening/resuming the exact session through the supported interface without submitting work. Select its existing workspace and reach the loaded conversation/input screen; a working-directory chooser or loading screen alone is not a successful resume. Close the verification client normally, then recheck ownership; a shared daemon may retain loaded threads, so distinguish a compatible daemon-owned session from a stale incompatible writer. If this cannot be tested, report the precise repair and that resume remains unverified. Do not claim success from file absence alone.
