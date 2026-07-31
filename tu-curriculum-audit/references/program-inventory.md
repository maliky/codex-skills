# Program Inventory

Use this reference when the user asks for current TU programs, offerings by college, or a deduplicated college/program list from curriculum Org sources.

## Source Order

1. Work in the active curriculum checkout at `/home/jil/tucurricula`.
2. Use `Audit/programs.org` first when present; it is a fast index, not final authority.
3. Verify against current top-level Org headings before answering. Prior archive summaries can guide the search but should not override maintained sources.

## Current Source Pattern

For the June 2026 curriculum set, the high-signal files were:

- `cafs_curriculum_2024.org`
- `cas_curriculum_2025.org`
- `cba_curriculum_2025.org`
- `ced_curriculum_2025.org`
- `chs_curriculum_2024.org`
- `cet_curriculum_2024.org`
- `tu_curricula_2026.org` for Access-to-College program-center entries
- `Archives/college_programs.org` as a cross-check only

## Deduplication Rules

- Return grouped college-by-college results directly when the user asks for a list.
- Deduplicate near-identical labels and repeated headings.
- Treat minors as variants unless the user asks to list every minor separately.
- Keep certificates, diplomas, associate degrees, and HNDs as separate offerings.
- If an archive mentions a program that current headings do not confirm, do not silently merge it; call it out as an unresolved older entry.

## Search Guidance

- Prefer simple file-targeted Org heading searches over one large regex.
- Start from known college files and headings before broad repo-wide pattern hunting.
- If a regex becomes fragile, switch to smaller `rg '^\\*+ '` or structured Org parsing.
