# Safe Synchronization

Use this reference before moving a self-hosted remote branch or recovering from an ambiguous push.

## Establish State

```bash
git status --short
git branch -vv
git rev-parse HEAD
git fetch --prune origin
git rev-list --left-right --count HEAD...@{upstream}
git log --oneline --decorate --graph --max-count=20 HEAD @{upstream}
```

Fetch changes remote-tracking references but not the worktree. For a branch that is only behind, prefer a fast-forward-only update. If both sides have commits, inspect the commits and repository policy before choosing merge or rebase.

## Push And Verify

Use an explicit destination when branch naming is uncertain:

```bash
git push origin HEAD:refs/heads/BRANCH
git ls-remote origin refs/heads/BRANCH
git rev-parse HEAD
git rev-parse origin/BRANCH
```

Object enumeration and transfer do not prove that the remote reference moved. Verify the advertised remote object ID after success, timeout, disconnect, or rejection.

## Concurrent Ref Updates

An error such as `cannot lock ref ... is at NEW but expected OLD` usually means another process changed the branch during the receive operation.

1. Do not retry with `--force` and do not delete a server-side lock file.
2. Fetch again and compare local `HEAD`, `origin/BRANCH`, and the object IDs named by the error.
3. If the remote now equals local `HEAD`, another push already published the commit; verify and stop.
4. If the remote contains local `HEAD`, the requested commits are already present behind newer remote work.
5. If histories diverge, inspect both sides and resolve normally before another push.
6. Touch the bare repository directly only with explicit server authorization and after confirming no receive process is active.

Force-push only when the user explicitly authorizes rewriting that branch. Prefer a reviewed `--force-with-lease` tied to the expected remote object ID; never use an unqualified force as a ref-lock workaround.

## Large Transfers

Before publishing many generated assets, inspect `.gitignore`, `.gitattributes`, Git LFS policy, staged scope, and repository size. Keep one authoritative asset version when project policy says so. A failed ref update may leave uploaded objects on the server, but it still requires an OID check before assuming publication or retransferring everything.
