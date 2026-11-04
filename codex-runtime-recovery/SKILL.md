---
name: codex-runtime-recovery
description: "Diagnose and restore Codex CLI startup locally or over SSH, including daemon readiness failures, locked or damaged SQLite runtime databases, and shared-filesystem storage problems. Use session-cleanup for an individual session writer lock or exact session deletion."
---

# Codex Runtime Recovery

Restore the requested usable runtime: a fresh session or a specific resumed session. Infer that choice from the conversation; ask only if the distinction affects the repair and remains unclear. Do not turn a fresh-start request into a history-recovery investigation.

Read [startup recovery](references/startup-recovery.md) for the diagnostic sequence, recovery choices, and acceptance checks.

## Boundaries

- Establish the failing layer before changing state: SSH, launcher, daemon, database, or session initialization. A version banner or rendered welcome screen does not establish readiness.
- Inspect the installed command help and effective configuration before using version-dependent commands, flags, or database filenames. Consult current official OpenAI documentation when local evidence is insufficient.
- A runtime restart or permission to discard a stuck session does not authorize deleting unrelated histories, databases, or writer locks. Prefer an isolated runtime when fresh startup is the goal and ownership of existing state is unresolved.
- Existing repair authorization carries forward. Scope process termination to verified owners; shared daemons can serve unrelated work. Keep authentication values out of diagnostic output.
- Distinguish observed failures from explanations: corruption and I/O errors are evidence, while NFS involvement or a recent update alone does not prove the cause.

## Routing

- For an individual session writer lock or exact session removal, use [Codex Session Cleanup](../codex-session-cleanup/SKILL.md) when available; do not use its deletion script to repair general startup.
- Retrieve historical conversation content only when the requested repair needs it. Session titles, process ownership, and metadata are usually sufficient for identification.

## Completion

Verify the user's normal launch command in the intended directory, then report the working command, runtime location, relevant persistence limits, and any remaining limitation. If a temporary command or daemon bypass is all that was verified, say so. For a resumed session, verify the exact target; for fresh startup, verify a new session. A minimal no-tools reply can establish end-to-end operation when within the authorized recovery scope.
