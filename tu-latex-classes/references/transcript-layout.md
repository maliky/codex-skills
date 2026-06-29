# Transcript Layout

Use this reference for `tutranscript` package work in `/home/mlk/Templates/TU`, especially `tutranscript/tutranscript.sty`, `build-example.sh`, and generated transcript examples.

## Back Matter

- `\TUTranscriptBackMatterPage` controls the back-matter page style. The accepted plain version keeps only the centered page number.
- Plain back matter means no registrar/date signature and no transcript header.
- `\TUTranscriptColumnBreak` and `\TUTranscriptPortraitContinuationBreak` are the split hooks for duplex portrait ordering.
- Duplex contract from the retained work: page 2 is transcript back matter, page 3 is follow-up grades, page 4 is empty when needed for duplex printing.

## Geometry And Detail Text

- Landscape geometry is controlled by the top-level `\ifTUTranscriptLandscape` branch.
- Portrait two-column geometry is controlled by `\ifTUTranscriptDetailTwoColumns`.
- The validated margin target was `left=1cm,right=1cm` for landscape and `detailtwocolumns`; regular single-column portrait stayed at `margin=1.15cm`.
- `\TUTRDetailFont` and `\TUTRDetailStretch` are the main detail-text knobs. If landscape detail moves to about `9pt`, adjust leading and surrounding sizes for balance.
- The visible separator between two detail columns is `\columnseprule` inside `\TUPrintTranscriptTwoColumnBlockDetails`.

## Validation

- Run `tutranscript/build-example.sh` for the affected profiles.
- Use `pdfinfo` to confirm page count, page size, and orientation.
- Use `pdftotext -layout` to check duplex ordering and that back matter is plain.
- Treat font-size and margin changes as page-count tradeoffs; test them separately when the page count matters.

## Common Failures

- Do not stop at removing the signature if the user asks for plain back matter; update the page style so the header is gone too.
- Re-check exact LaTeX control names. A typo such as `\columseprule` instead of `\columnseprule` is fatal.
- Add a dedicated `detailtwocolumns` geometry branch instead of letting the profile inherit generic portrait margins.
