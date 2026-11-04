---
name: genealogy-engineering
description: "Maintain the private Genealogie project in /home/jil/Genealogie: source reconciliation and uncertain relationships, consistent JSON/GEDCOM/Org data, the family-graph explorer, persistent web edits, and publication that preserves online corrections."
---

# Genealogy Engineering

Read `AGENTS.md`, current `DEV.org` decisions, `MANUAL.org` and the files relevant to the requested correction. Preserve the distinction between documentary evidence, family testimony and hypotheses. Keep family data private; write skill examples and technical reports without copying personal records.

## Workflow

1. Establish the source of the requested change: document, repository corpus, browser observation, or persistent web edit. Confirm the current graph fingerprint and dirty work before changing structured data.
2. Resolve exact person/family identifiers and provenance. Do not infer an identity or relationship from a similar name alone.
3. Use the maintained correction, validation and synchronisation helpers for the affected representations. A prose correction does not require regenerating the whole corpus.
4. For explorer work, preserve the data contract, selected people, camera/framing and edit-conflict behaviour. Verify changes with isolated graph/browser fixtures.

## Routes

- **Facts, sources, uncertainty, import corrections or linked formats**: read [corpus and provenance](references/corpus-and-provenance.md).
- **Persistent edits, repository synchronisation, explorer verification or private publication**: read [editing and publication](references/editing-and-publication.md).
- **Host DNS/TLS wiring**: use `koba-vps-webops` alongside the project's deployment runbook when needed.

## Report

State which representations and fingerprints changed, remaining uncertainty, validation performed and whether the result is local or published. Describe technical outcomes without exposing private source documents or full family records.
