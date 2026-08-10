---
name: self-hosted-git-operations
description: "Use when operating or troubleshooting non-GitHub Git repositories hosted over SSH, especially jil@54.36.60.51:git/*.git, including remote URL changes, fetch/pull/push synchronization, passphrase or public-key boundaries, non-fast-forward divergence, concurrent pushes, cannot-lock-ref failures, large object transfers, bare-repository verification, or exact fallback commands the user must run interactively."
---

# Self-Hosted Git Operations

Inspect local and remote state before changing either side. Treat authentication, object transfer, and reference movement as separate facts; a transfer that ends with an error does not prove whether another process moved the remote branch.

## Avoid When

- The remote is GitHub and the task is a PR, review, or Actions workflow; use the relevant `github:*` skill.
- The core problem is a deployed web service on the Koba VPS; use `koba-vps-webops` after repository synchronization is understood.
- The task is only a local commit with no self-hosted remote or synchronization concern.

## Workflow

1. Confirm the repository root, worktree status, current branch, upstream, remote URLs, and local `HEAD` before mutation.
2. Preserve unrelated local changes. Stage and commit only the user-authorized scope.
3. Verify SSH and remote configuration separately from branch divergence; read [SSH and remotes](references/ssh-and-remotes.md).
4. Fetch before diagnosing ahead/behind state when remote access is available.
5. For pull, push, non-fast-forward, concurrent update, ref-lock, or large-transfer issues, read [safe synchronization](references/safe-synchronization.md).
6. Never infer success or failure solely from progress output. Compare local, tracking, and advertised remote object IDs after any ambiguous operation.
7. Push only when the user requested publication. Never enter, store, or expose a passphrase or private key; give the exact interactive command when the user must authenticate.
8. Report the final worktree state, branch relationship, relevant object IDs, command outcome, and any remaining user action.

## Routes

- **SSH keys, passphrases, renamed repositories, and remote URLs**: read [SSH and remotes](references/ssh-and-remotes.md).
- **Fetch/pull/push, divergence, concurrent ref updates, and large pushes**: read [safe synchronization](references/safe-synchronization.md).

## Output Expectations

State what was inspected and changed, whether the worktree is dirty, the local and remote branch names, ahead/behind or ancestry result, and whether authentication or a remote-side operation still requires the user.
