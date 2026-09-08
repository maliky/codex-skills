# Configuration and Synchronization

Use this reference when repairing Mu4e/OrgMime composition commands, bindings, Maildir indexing, mbsync behavior, or local authentication.

## Authoritative Configuration

- Inspect current package versions, running Emacs state, worktree changes, and local instructions before reusing an old fix.
- In `/home/mlk/.emacs.d`, maintain mail configuration in `init.org`; treat `init.el` as tangled output. Preserve unrelated configuration and the existing opt-in OrgMime design.
- Keep composition bindings local to the mode that supplies the mail-header separator. A command that edits message composition should not be active in a read-only Mu4e article view.
- Repair the actual interactive command or wrapper rather than replacing the user's workflow. Verify command existence, `commandp`, and key lookup in the target mode.

## Configuration Validation

1. Check the focused `init.org` change and tangle it through the repository's established command.
2. Validate generated Elisp syntax and load behavior without claiming success from a text diff alone.
3. Inspect the binding in a real or representative `message-mode` buffer and confirm it is absent where inappropriate, especially `mu4e-view-mode` or article buffers.
4. Exercise the return/export behavior only as far as the user requested; do not send the test message.

The local workflows have used `s-o s-m` for standard OrgMime editing and `s-o s-c` for an opt-in custom wrapper. Treat these as current-state clues, not permanent constants: inspect the live configuration before changing them.

## Mu, mbsync, and Authentication

- Separate Maildir contents, Mu index state, mbsync transfer, GnuPG/keyring access, and provider authentication. A success or failure in one layer does not prove the others.
- Prefer read-only configuration, process, lock-owner, and connection checks first. Never print passwords, tokens, private keys, or decrypted secret material.
- Inspect a live index lock and its owner before considering cleanup. Do not delete locks, indexes, Maildir content, or account data without exact authorization and a recoverable plan.
- Do not launch a full synchronization merely to improve search results or navigation. Run account or folder synchronization only when the user explicitly requests it and the impact is understood.
- After a requested sync or index update, verify the specific account/folder result and distinguish server state, local Maildir state, and indexed visibility.
