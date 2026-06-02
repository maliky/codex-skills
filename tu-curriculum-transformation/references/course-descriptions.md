# Course Descriptions

Use this reference when normalizing course-description sections into TU curriculum macro form.

## Target form

Normalize stable course-description entries into the TU curriculum macro form.

Preferred forms:
- `\TUCurriCrsDescEntry[...]...`
- `\TUCurriCrsDescEntryKey[...]...` when internal target disambiguation is needed

## Rules

1. Preserve visible course codes exactly as written.
2. Preserve visible titles and wording from the source.
3. Convert the credit argument to visible text such as `3 credits` or `1 credit` when that is the local convention.
4. Keep prerequisites visible but subordinate to the main code, title, and description.

## Duplicate and ambiguous cases

When the source reuses the same visible course code for different descriptions:
- preserve the visible code
- use the keyed macro form only to disambiguate the internal link target
- record the ambiguity for future maintenance

When identical descriptions recur across several programs:
- factor them into one shared college-level course-description section
- do not duplicate the same prose under each program when one shared section is clearer

## Group placement

Move course descriptions under the real `Course Descriptions` section when the import scattered them elsewhere.

Prefer grouping by department or stable section family. Do not invent a new grouping just because the current file is messy.

## Do not do this

- do not rewrite descriptions for style
- do not normalize visible inconsistencies unless the source itself clearly supports it
- do not change course codes just to simplify linking
