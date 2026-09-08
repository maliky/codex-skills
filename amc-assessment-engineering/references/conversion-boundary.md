# AMC Source and Conversion Boundary

The user's September 8 direction makes native AMC LaTeX the authored source for questions and the input to future Haskell conversion. This changes source ownership; it does not mean a converter already exists or that every AMC construct fits GIFT.

- Inspect `Banque-GIFT/README.org`, its specification, `GiftAmc.Model`, inventory code, fixtures, and tests before implementing conversion. The inspected baseline contains a typed intermediate model and structural inventory, and explicitly reports no implemented AMC/GIFT converters. Recheck this state on each task.
- A typed internal representation can remain useful to parsers and writers without replacing AMC as the user's editable source. Reconcile older architecture documentation with the latest explicit direction within the requested implementation scope.
- Separate source discovery, include/macro resolution, parsing, semantic validation, and format emission. Regex inventory results do not prove correct LaTeX interpretation or a working conversion pipeline.
- Preserve identifiers, provenance, answers, scoring, figures, variants, and randomization where supported. Report each unsupported, manual, or lossy construct explicitly rather than silently flattening it.
- Validate supported conversions with synthetic fixtures and semantic comparisons, including scoring and answer behavior. Do not promise lossless round trips from text similarity alone.
- Keep archive ingestion read-only and exclude rosters, scans, marks, databases, and unrelated administrative files before reading. Reports should expose only the metadata required for the task.
- Conversion development does not authorize regeneration of existing AMC projects or replacement of manually edited questions. Hand back the supported contract, loss report, and tests actually run.
