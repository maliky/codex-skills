# UTF-8 in terminal Emacs and user sessions

## Locate the failing layer

- Inspect `locale`, `locale charmap`, installed locales from `locale -a`, and `LANG`, `LC_CTYPE`, `LC_ALL`, and `LOCPATH`. Do not assume `C.UTF-8` exists. An installed locale such as `en_US.UTF-8` can provide UTF-8 without generating locales or changing system configuration.
- Trace the user's actual shell startup files and load order. `LC_ALL` overrides both category variables and `LANG`; an inherited unavailable value can defeat an otherwise correct `LANG`. Preserve unrelated regional preferences instead of setting every locale category indiscriminately.
- Inspect every relevant running Emacs instance through its existing server socket. Query `current-language-environment`, `locale-coding-system`, terminal and keyboard coding systems, `default-process-coding-system`, and relevant environment variables. Multiple instances can have different encodings despite sharing one init file.
- Check the terminal multiplexer separately. Correct UTF-8 bytes from Emacs can still be misinterpreted by a Screen window or the client terminal. Do not infer installed fonts or visible glyph quality from server-side encoding checks.

## Apply the account-level fix

Choose an installed UTF-8 locale compatible with the user's language preferences. If an inherited `LC_ALL` is the problem, unset it in the appropriate personal startup file; set `LANG` and, when needed, `LC_CTYPE`. A shell launched with an invalid locale may warn before reading that file. Editing startup files cannot change an already-running parent shell or agent's environment.

For Emacs, edit the maintained Org source and tangle it. This is a suitable coding-system block for terminal UTF-8 use:

```elisp
(set-language-environment "UTF-8")
(prefer-coding-system 'utf-8-unix)
(setq locale-coding-system 'utf-8-unix)
(set-terminal-coding-system 'utf-8-unix)
(set-keyboard-coding-system 'utf-8-unix)
```

Ensure Emacs's `process-environment` also contains the chosen valid locale when fixing already-running instances or launches that bypass shell startup. `prefer-coding-system` alone may leave `locale-coding-system` nil in an instance started under `LANG=C`. Check existing input-method preferences before changing the language environment.

Apply only the changed definitions to live instances. Terminal and keyboard coding settings can be applied per frame. Preserve unsaved buffers and avoid restarting Emacs or reloading the entire init for this change. Inspect existing subprocess coding before changing it: terminal emulators such as vterm may intentionally use binary input.

For GNU Screen, `defutf8 on` in the user's `.screenrc` affects future windows. `screen -S SESSION -p WINDOW -X utf8 on on` sets an existing window and its display to UTF-8 when that matches the client. Update session defaults and environment for future child processes as needed. These changes do not update environment variables inside existing shells. Give the user a short export command for those shells; do not inject commands into windows that may be running another application.

## Verify observable behavior

- Launch fresh login and interactive shells and check `locale charmap`. Print a sample such as `Français : é à ç œ — € α → ✓ 中文`; `wc -m` should count characters rather than UTF-8 bytes.
- Check generated Elisp with `check-parens`, then re-query the affected live Emacs coding settings and a child command's `locale charmap`.
- For a terminal integration check, use a controlling pseudoterminal: `pty.fork()`, or a new session plus `TIOCSCTTY`. Connecting ordinary subprocess pipes or an unclaimed PTY slave is insufficient for Emacs, which opens `/dev/tty`.
- Verify emitted UTF-8 bytes and actual interactive text insertion. Feed an accented character through Emacs's normal command loop and save the buffer with a bound command. A bare `read-event` can expose events before keyboard decoding and misreport valid UTF-8 input as mojibake; it is not an equivalent typing test.
- Report the scope of verification accurately. A PTY test establishes encoding and input handling, not the glyphs rendered by the user's remote terminal font. A dedicated sample buffer can support a visual check without replacing the user's current buffer.

## Dated host observation: 2026-10-07

On the account with home `/home/konemalikMI`, `~/.bashrc` forced `LANG=C`, `C.UTF-8` was unavailable, and `en_US.UTF-8` was installed. Two running Emacs instances had ASCII terminal settings. The source was `~/.emacs.d/init.org`; the shell, live Emacs instances, and Screen sessions all needed attention. Recheck these facts rather than treating them as permanent host properties.

During the same work, sandboxed command execution failed before launching the requested command because Bubblewrap could not create a user namespace. On this RHEL 7.4 host, `user.max_user_namespaces` was `0` and `unshare --user --map-root-user true` failed. This was independent of UTF-8. A user-local Bubblewrap binary cannot enable kernel namespaces; current upstream Bubblewrap requires them. Check current host support before attempting an installation, and use only the execution mechanisms permitted by the session. See the [upstream user namespace requirements](https://github.com/containers/bubblewrap#user-namespaces).
