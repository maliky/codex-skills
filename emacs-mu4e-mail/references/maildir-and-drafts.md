# Maildir and Drafts

Use this reference when locating correspondence, reconstructing a thread, creating a local reply draft, or preparing a mail-delivered attachment.

## Canonical Local Data

- Resolve symlinks before editing. `/mnt/backup/.mbsync` is the canonical Maildir root and `/mnt/backup/.mbsync/Drafts` is the maintained Org drafting workspace unless current local configuration establishes another target.
- Search with the locally supported `mu find -o plain -f ...` grammar. Start with narrow sender, subject, date, mailbox, or message-id terms rather than dumping broad private result sets.
- When Mu rendering omits headers, multipart bodies, or attachments, locate and inspect the raw Maildir message. Do not assume a rendered view is complete.
- Duplicate hits may be indexed and Maildir copies of the same message. Confirm `Message-ID`, sender, recipients, subject, date, and mailbox path before treating them as separate correspondence.
- Check locally supported query syntax. An unsupported date or recipient expression is a query failure, not proof of absence; simplify to an exact address or subject, verify raw headers, and filter dates using those records. Use `-u`/`--skip-dups` when supported, while retaining conflicting versions for review.

## Drafting a Reply

1. Identify the message being answered and recover enough prior thread context to understand the requested action.
2. Preserve the correct `To`, `Cc`, `Subject`, `In-Reply-To`, and `References` values. Do not add recipients or change thread identity without evidence.
3. Draft in Org when that is the local maintained format. Preserve headings, lists, tables, links, directives, and `:noexport:` evidence or previous-version sections.
4. Correct conservatively in the user's language and register. Keep proofreading separate from an optional reformulation when the distinction matters.
5. Compare questions and answers point by point for clarification drafts; request only the unresolved decisions rather than repeating settled issues.
6. Verify headers and final body, then leave the draft unsent.

Do not state that an attachment is attached, that a message was sent, or that a recipient was contacted unless that exact action was requested and verified.

## Sensitive Correspondence

- Build chronology from dated messages and documents. Distinguish documented facts, the user's recollection, conflicting records, and unanswered questions; do not turn an uncorroborated account into an independently verified event.
- Use short, direct, polite sentences when matching the user's requested voice. Keep payment amount, payment date, property return, benefits status, and agreement terms as separate questions when the thread involves them.
- Verify legal claims against current primary sources when such analysis is requested. Preserve uncertainty and ask for the institution's exact policy or legal basis where evidence is incomplete; do not store case-specific legal conclusions as reusable facts.
- Inspect proposed evidence attachments for credentials and private third-party material. A handover document may contain secrets even when its title appears suitable for forwarding. Keep supporting analysis under non-exporting notes when appropriate and verify it does not enter the outgoing body.

## Attachments and Forms

- Keep received attachments unchanged and create a clearly named working or completed copy.
- Route structure-preserving office/PDF conversion and form completion through `document-conversion` when needed.
- Use only locally supported personal values, preserve legal notices and signatures, and leave unsupported fields visibly unresolved.
- Validate a completed attachment structurally and visually, but do not attach, upload, or send it automatically.

## Privacy

- Keep searches and reports narrow; do not print whole mailboxes, complete private bodies, secrets, tokens, or unnecessary personal details.
- Treat quoted mail and draft evidence as private even when it is stored in a Git working tree.
- Preserve unrelated drafts and existing edits. Do not commit mail or personal attachments unless explicitly requested and safe for that repository.
