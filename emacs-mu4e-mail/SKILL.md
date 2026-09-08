---
name: emacs-mu4e-mail
description: "Use when searching the local Mu4e Maildir, analyzing the user's writing style from historical mail, preparing unsent Org drafts, editing an active OrgMimeMailBody buffer, or repairing Mu4e/OrgMime composition behavior in Emacs."
---

# Emacs Mu4e Mail

Work on the user's existing local Maildir and opt-in OrgMime composition workflow. Preserve message context and the user's voice, make live-buffer edits recoverable, and keep drafting, conversion, attachment, synchronization, and sending as distinct authorization boundaries.

## Avoid When

- The task is generic document or form conversion with no mail context; use `document-conversion`.
- The task concerns a webmail or cloud-mail connector rather than the local Mu4e/Maildir setup.
- The request is domain engineering for CSRS, TU, or another project rather than finding or drafting its correspondence; use the relevant domain skill for the substantive analysis.
- The user asks only for general Emacs configuration unrelated to mail composition.

## Workflow

1. Resolve the real Maildir or draft path and read the nearest `AGENTS.md`. Treat `/mnt/backup/.mbsync` as the canonical local mail root unless current configuration proves otherwise.
2. Distinguish search, drafting, active-buffer editing, attachment preparation, configuration repair, account synchronization, and sending before acting; permission for one does not authorize the others.
3. Search indexed mail narrowly, verify message identity and thread context, and inspect the raw message when rendered or indexed output is incomplete.
4. Preserve recipients, subject, reply headers, quoted context, Org structure, tone, and factual uncertainty. Do not invent personal, administrative, financial, medical, or identity information.
5. For a live `OrgMimeMailBody` change, inspect the actual buffer and mode, make an undoable scoped edit, preserve the OrgMime control structure, and reread the exact result.
6. For a configuration repair, edit the canonical literate source, tangle or reload through the existing workflow, and validate behavior in both composition and read-only article contexts.
7. Leave messages unsent and attachments unattached unless the user explicitly requested the corresponding external action. Never expose credentials, private message bodies, or unnecessary personal data in reports.

## Routes

- **Maildir search, reply context, local Org drafts, and attachments**: read [Maildir and drafts](references/maildir-and-drafts.md).
- **Historical writing style, sample coverage, and voice adaptation**: read [writing-style analysis](references/writing-style-analysis.md).
- **Direct editing of an active OrgMime composition buffer**: read [OrgMime buffer editing](references/orgmime-buffer-editing.md).
- **Emacs bindings, Mu4e/mbsync diagnostics, authentication, and synchronization boundaries**: read [configuration and synchronization](references/configuration-and-sync.md).

## Output Expectations

Lead with the draft, buffer, configuration result, or exact evidence found. Report the real path or buffer, what was verified, unresolved factual or attachment questions, and whether synchronization, attachment, sending, or another external action was deliberately left undone.
