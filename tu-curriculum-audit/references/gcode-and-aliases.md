# Gcode And Aliases

## When To Use

Use this reference when course ids, generated codes, labels, or internal anchors need to be rebuilt after title/code cleanup.

## Rules

- Visible course codes are source facts; do not change them just to make keys unique.
- Internal keys may be disambiguated when visible codes collide.
- Keep alias mappings explicit and reviewable.
- Detect collisions before editing source files.

## Mapping Shape

Use a plain table or TSV with:
- `old_key`
- `new_key`
- `visible_code`
- `title`
- `reason`
- `confidence`
- `source`

## Regeneration Sequence

1. Extract current keys and visible course facts.
2. Build a proposed mapping.
3. Check for duplicate `new_key` values.
4. Apply edits only after the mapping is accepted or clearly implied by the task.
5. Re-run extraction and compare counts before and after.
