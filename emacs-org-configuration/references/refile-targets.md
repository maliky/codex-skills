# Source-Relative Refile Targets

## Discover The File From The Source Buffer

Use the source buffer's `buffer-file-name`, falling back to its base buffer for an indirect buffer. `default-directory` can point elsewhere and does not establish where the source file lives. The existing helper `mk/org-sibling-refile-files` returns a readable regular sibling `REFILE.org`; inspect its actual definition before replacing it.

Keep the dynamic file provider first in `org-refile-targets` and retain existing targets and selectors. Skip missing/unreadable siblings without creating files or headings as a side effect. A non-file buffer has no inferred sibling directory. Org supports a function symbol as the target entry's file provider; let it resolve the file in the source-buffer context rather than freezing one path at startup.

## An Empty File Is A Different Case

A file present in the target list can still contribute no destinations: `:level`/`:maxlevel` selectors normally collect headings, and an empty file has none. Inspect its contents and the effective `org-refile-use-outline-path` before diagnosing discovery as broken.

For filing at the top of an empty target, file outline mode exposes the file itself as a destination. The smallest reversible check in the source buffer is:

```elisp
(setq-local org-refile-use-outline-path 'file)
```

Then inspect `(org-refile-get-targets)` or reopen the picker. Persist that policy only as requested. Adding an invented Inbox heading is not necessary merely to make an empty file selectable. Refresh the target cache if old entries remain after a change.

## Verify Without Moving Entries

Check source-relative resolution with different working/source directories, more than one source directory, an indirect buffer, a missing sibling and an empty sibling. Confirm retained destinations and intended heading depth. Use a temporary Org fixture for picker checks; no real entry needs moving.

Read effective settings in the actual source buffer when a live Emacs server is reachable. A failed socket connection leaves live behaviour unverified: batch checks can validate extracted definitions, source/output parity and `check-parens`, but do not establish what an already running buffer loaded. Avoid loading the complete personal init as a test because it can activate unrelated services or state.
