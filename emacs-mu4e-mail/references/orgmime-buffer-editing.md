# OrgMime Buffer Editing

Use this reference only when the user wants the current Emacs composition buffer inspected or changed directly.

## Identify the Real Surface

- Use the running Emacs instance and confirm that the target buffer exists, is the intended composition, and is in the expected mode. The conventional buffer is `OrgMimeMailBody`, but do not assume a stale or similarly named buffer is the target.
- Inspect enough context to locate the requested passage and the OrgMime control markers without echoing the entire private message into tool output.
- A Mu4e article view is not a composition buffer. Do not call composition commands in a read-only article buffer or infer that its visible text is the editable draft.

## Safe Edit

1. Narrow the replacement to the requested body region; preserve headers, the mail-header separator, OrgMime instructions, `:noexport:` history, links, and unrelated text.
2. Run the change inside the target buffer and an `atomic-change-group` so an error does not leave a partial edit and the user can undo it.
3. Preserve the user's meaning, voice, relationship, and level of formality. Do not silently turn proofreading into a substantive rewrite.
4. Calculate positions and verification values inside the target buffer rather than reusing positions from another buffer.
5. Reread the exact changed region and relevant structural markers after the edit. Confirm that export-visible and hidden sections still behave as intended.

Use timeout-bounded `emacsclient --eval` calls when the server might be unavailable. A socket or permission failure is not evidence that the buffer does not exist; diagnose the connection boundary without starting a second Emacs instance that could conflict with the live session.

## External Boundary

Editing the live buffer does not authorize HTML conversion, attachment, saving to a remote mailbox, synchronization, or sending. Perform only the composition steps the user requested and state what remains under their control.
