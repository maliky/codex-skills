# Domain And Evidence

Read the current specification, `ARCHITECTURE.org`, affected models and domain `api.py` before choosing an extension point. A planned parent-company or shareholder feature does not establish its business rules or authorise inventing ownership history.

## Separate The Facts

- Original documents and their SHA-256 are immutable evidence. Keep OCR output, editorial correction and confirmed financial data distinguishable and traceable to that source. An OCR engine's success does not validate a receipt.
- Product identity, catalogue association, spending category and financial confirmation are separate decisions. A valid expense can exist without a catalogue reference. Classification proposals or bulk association confirmation must not silently validate a ticket's cost.
- Use Decimal for money and quantities; preserve units, currencies, calculation bases and rounding. Missing price is unknown, not zero. If the requested convention defaults an absent quantity to one, retain its default/provenance flag; do not overwrite explicit weights or volumes or portray that default as observed evidence.
- Keep invoiced cost, payments, change returned, loyalty and discounts separate. Do not deduct a summarised discount twice. Last paid price depends on purchase date and confirmed association; a late import or return cannot replace the latest valid purchase merely by being processed later.
- Preserve frozen forecasts and historical financial facts. Reconciliation cannot allocate the same amount twice. Changing catalogue metadata does not implicitly rewrite historical lines.

## Typed Boundaries And Permissions

The current monolith separates `core`, `spaces`, `catalog`, `purchases`, `documents`, `planning`, `application`, `ui` and `exports`. Follow domain `api.py` facades and the dependency direction in `ARCHITECTURE.org`; keep cross-domain workflows in the composition layer. Explicit Protocol ports support necessary inverse queries without importing views or the UI registry into business services. Reuse this structure rather than introducing parallel repositories or implicit signals.

Writes through domain commands/`MutationPolicy` and `spaces.records` recheck active membership, lock the space, validate versions, relations and editable fields, then mutate and audit atomically. Keep bulk operations bounded, atomic and idempotent. A repeated key with the same payload returns the same typed result; a concurrent change requires a new preview or conflict response, not silent last-write-wins.

Apply space scope to lookup/autocomplete choices, documents, downloads, exports, searches and bulk endpoints as well as mutations. Neither a readable URL nor a hidden UI control changes authorisation. Keep Decimal JSON representations and result codecs consistent between first execution and idempotent replay.

## Private Corpus

Real receipt data belongs in the authorised private environment. Do not serve originals through a public static alias or send them to an external recognition provider without applicable authorisation. Use fictitious data and simulated engines for ordinary OCR tests; do not rerun recognition over the private corpus as an incidental test. Keep credentials, backups and runtime media out of skill examples and commits.
