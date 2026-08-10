# Image OCR Ingestion

Use this reference for non-trivial photograph- or scan-to-structured-text conversion.

## Preserve Evidence

- Inventory every source path and SHA-256 before processing.
- Keep originals immutable and put preprocessing, OCR text, metadata, and logs in a generated work directory.
- Key reusable cache entries by source hash and complete processing profile, including OCR/tool versions and resolution choices.
- Generate a draft separately from the maintained document. Raw OCR is evidence, not truth.

## Benchmark Before Bulk Processing

Select representative pages for rotations, dark backgrounds, low resolution, dense prose, tables, separators, and mixed image/text content. Compare full resolution with proposed reductions using confidence and required reference terms. Reject a faster profile when important pages regress, even if aggregate confidence improves.

For independent pages, use bounded process-level parallelism. Reserve CPU and memory for the host, constrain OCR and image tools to one internal thread per worker, isolate failures per page, and publish shared manifests or drafts from one parent process atomically.

## Separate Classification From Editorial Decisions

Keep these concerns distinct in a structured manifest:

- intrinsic page type
- include/exclude decision and reason
- detected visual content and label
- target document entry or entries
- review status and notes

Machine classification may suggest values but must not silently alter reviewed fields on rerun. One source page may map to several document entries. Fence raw OCR as literal content when its numbering or punctuation could be interpreted as target-format structure.

## Validate

Check source count and hashes, manifest uniqueness and coverage, cache/profile consistency, every inclusion and exclusion decision, target heading/source links, ordering, and syntax of the maintained document. Report unresolved pages explicitly and do not present a machine draft as final editorial output.
