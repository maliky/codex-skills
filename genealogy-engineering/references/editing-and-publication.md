# Editing And Publication

Read `deploy/README.org`, `deploy/publier.sh`, `outils/editions_genealogiques.py` and `outils/synchroniser_editions.py` for the current storage and release contracts.

## Three Different States

- The repository corpus is the source revision prepared for publication.
- Persistent web edits live in private versioned storage, currently `/var/lib/genealogy/versions/`, with an atomic current link, fingerprints and actor/before/after journals. They survive code releases and restarts.
- Browser observations are local notes tied to a browser origin and corpus fingerprint. They require explicit export/import and are not automatically shared server edits.

Simple-person edits use a per-record revision to reject concurrent overwrites while preserving the user's form. Do not imply that unimplemented relationship-edit controls are already available; inspect current endpoints and editable-field validation. Adding or deleting an edge is a different operation from adding or deleting a person.

## Reconciliation And Publication

The publication helper reconciles incoming repository data, the previous publication base and online corrections. Independent edits merge; conflicts stop publication. The merge is repeated under the storage lock before activation. Follow that workflow rather than copying repository JSON over the persistent store. A code rollback never authorises downgrading persistent family data.

For an authorised return of online edits to Git, use the current `synchroniser_editions.py` export and import modes. Export to a new private file, inspect the import's dry-run, then apply within scope. The helper verifies the export fingerprint and local correction chain and updates linked formats, source/audit records and checksums. A repeated identical import is a no-op. Never print the export or attach it to a shared technical report.

Publication uses the maintained allowlist; original private documents, import archives, credentials and Git metadata are excluded. The service normally serves an authenticated Nginx proxy through a restricted Unix socket. Preserve peer-identity, HTTPS-origin and CSRF checks for writes. Test expected anonymous denial on pages/API/assets as well as authenticated graph loading; `/healthz` alone proves routing, not corpus availability.

## Verification

Use `python3 -m unittest discover -s tests` for the changed structured-data/editing boundary and the appropriate `outils/verifier_*_navigateur.py` command for UI work. `verifier_edition_navigateur.py` uses isolated storage/proxy fixtures for real writes; it must not mutate the published family store as a test. Screenshots and exports remain private.

After an authorised release, compare `/api/graphe`'s fingerprint with the active persistent corpus, not automatically today's repository file: an online edit may legitimately make them differ. Verify service state, the expected private HTTPS response and the actual changed explorer interaction. Preserve selection/framing on edits and leave concurrent-conflict input available for correction.
