# SSH And Remotes

Use this reference when a self-hosted remote cannot be reached, was renamed, or requires interactive SSH authentication.

## Inspect First

```bash
git remote -v
git remote get-url --all origin
git branch -vv
git ls-remote --symref origin HEAD
```

Remote paths such as `jil@54.36.60.51:git/repo.git`, `jil@54.36.60.51:~/git/repo.git`, and differently cased repository names are not interchangeable. Read the configured URL and the user-provided authoritative path before changing it. A repository rename normally needs `git remote set-url origin NEW_URL`, not a reclone.

## Authentication Boundary

- `Permission denied (publickey)` is an authentication failure, not evidence that the repository path is wrong.
- Inspect `~/.ssh/config`, `ssh-add -l`, key file presence, and permissions before proposing a new key.
- Do not generate, replace, copy, or upload keys without explicit authorization.
- Never request or echo a private-key passphrase. If the key needs an interactive prompt, provide the exact `git fetch`, `git pull`, or `git push` command for the user to run in their terminal.
- Do not weaken host-key checking. A changed host key requires independent verification.

After changing a remote URL, run a read-only advertisement such as `git ls-remote` before attempting a push. If authentication succeeds but the path is wrong, preserve the server error exactly so the repository owner can distinguish a missing repository from an access-control failure.
