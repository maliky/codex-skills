# Resume and Workspace Paths

Use for a conversation missing from the resume picker after a folder move or rename. Perform file-based diagnostics first; database forensics is outside this skill.

## Diagnose

- Check the installed `codex --version` and `codex resume --help` for current behavior. In the inspected CLI, `--all` disables current-directory filtering and `-C` supplies the working root; verify these options before giving commands.
- Resolve the supplied old/new paths and symlinks. Read the narrowed rollout's first `session_meta` record for its id and stored `cwd`. Folder renames need not update this historical path.
- Compare rollout presence, JSONL parse integrity, actual user messages, and available index aliases separately. A metadata-only rollout is empty; an absent alias is not proof that a substantive conversation was deleted.
- Use stable UUIDs when names collide or index aliases are missing. Distinguish root rollouts from subagents and do not count renamed aliases as separate sessions.
- Bound parsing to the relevant sessions and report counts/errors without dumping message bodies, image payloads, or titles that may contain entire internal transcripts. Valid JSON alone does not prove end-to-end resumability or database integrity.

## Recovery Guidance

When current CLI help confirms the options, give commands using the verified new directory and exact root-session UUID:

```bash
codex resume --all -C /absolute/new/project
codex resume -C /absolute/new/project SESSION_UUID
```

These are discovery/working-root overrides, not a claim that all historical paths are migrated. Interactive resume may create state, so a read-only diagnosis should report it as untested unless actually exercised within the user's request.

Do not rewrite history, rollout metadata, database rows, or create compatibility symlinks merely because directory filtering explains a missing entry. If the supported command still fails, obtain the exact error and investigate that specific boundary. Request a separate scoped repair only when a repair is actually needed.
