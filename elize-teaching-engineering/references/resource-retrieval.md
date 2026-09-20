# Authenticated teaching resources

Inspect the repository's existing downloader and source manifest first; recent work used `chingmath-sources.py`. Keep provider URLs and authentication logic in the maintained helper rather than duplicating an ad hoc downloader.

For ChingMath, observed private PDF routes use numeric type `1` for statements and `2` for corrections, with the shape `/espaceFeuille/feuille-{account}-{worksheet}-{type}.pdf`. Recheck the current page/helper before reuse; guessed `-e`/`-c` suffixes failed, and the TeX archive uses a separate endpoint.

Use the user's authorized session without printing cookies, tokens, or account-specific URLs. Keep session artifacts in an ignored private build directory; verify ignore rules before staging. The previously used location was `assets/.build/chingmath`.

An HTTP success may contain a login page. Validate the PDF signature, `pdfinfo`, worksheet identity, statement-versus-correction content, and representative rendering. Record source provenance in the existing manifest without credentials. Never substitute invented exercises or corrections for inaccessible source material.
