# Corpus And Provenance

## Source Precedence

Inspect provenance before treating any Org file as canonical. Preserve original spellings, variants, quotations, source identifiers and uncertainty. A search result, family recollection or visual connection in the graph is not documentary confirmation. Do not invent a date, parent, spouse or source, or merge people without identity evidence.

The repository's local rule prefers an identified documentary date over a tree date when they differ by a few days. Retain both values and the reason/reference in provenance. This rule does not automatically settle contradictions between documents or disputes about identity and filiation. Ask for the specific missing family fact only when available sources cannot resolve a consequential ambiguity.

An uncertain relationship can be represented when requested, with its uncertainty retained. Check the current chronology policy separately from documentary confidence: inclusion in a visual estimate does not turn the relationship into a confirmed fact. An unknown death date remains unknown; a historical `[Living]` placeholder is not proof that a person is currently alive.

## Linked Representations

The explorer reads `donnees_genealogiques.json`; relevant maintained outputs also include GEDCOM, Org, source notes, import mappings and `empreintes.sha256`. Use `outils/corpus_genealogique.py`, existing scoped correction helpers and the current manual to determine which representations a change affects. Preserve stable IDs, source links and correction history; avoid global regeneration for an isolated wording change.

Reconcile duplicate/conflicting records through the maintained correspondence and correction chain rather than deleting evidence because the UI no longer displays it. A private source can remain in provenance while the product UI shows a concise neutral description or a permitted public reference. Do not infer authorisation to publish a document from its presence in this private repository.

After a structured correction, run `python3 outils/verifier_genealogie.py`, update affected entries of `empreintes.sha256` through the established workflow, and run `sha256sum --check empreintes.sha256`. Use relevant tests for identity/relationship or export logic. Check counts and referential consistency without printing the underlying private records.

## Explorer Semantics

Keep selection, hover and search/filter behaviour distinct. The common view supports ancestors, descendants and both directions for explicit root people; spouse/social links do not automatically become ancestry paths. Preserve unknown/confidence states and the current date-estimation policy across 2D/3D views. Presentation changes to card shape or size must not silently change the graph's relationships or source facts.
