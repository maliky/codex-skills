# Visual Review And Retries

Use this reference when reviewing native panels or legacy sheets and when writing rejection notes that will drive the next attempt.

## Review From Facts

Inspect the generated bitmap itself. Do not accept from the prompt, tool success, filename, normalization, or a prior assistant description. Compare it with the exact claim prompt, `AGENTS.md`, the relevant `STORYBOARDS.org` step, and validated recipe facts.

Review in this order:

1. **Asset structure:** one square independent panel in native mode; no sheet, collage, inset, border, or montage.
2. **Forbidden marks and style:** no text, digits, letters, logo, watermark, color, tint, photorealism, or decorative clutter.
3. **Recipe identity:** correct ingredients, first alternative only, no optional or invented ingredient, and only required utensils.
4. **Quantities:** exact visible counts from 1 through 11; grouped counts for 8 through 11; plausible abundance for 12 or more; no duplicated representation.
5. **Measures:** each weight is one batch on an analog scale without visible digits; each required volume or spoon quantity has a distinct, coherent, unmarked measure.
6. **People and anatomy:** no person or hands in P1; at most two coherent hands from the recurring chef in intermediate panels; only the finale may show the complete chef; no assistants.
7. **Continuity and action:** one dominant step, plausible transformation, stable chef and utensils, and presentation-only finale.

Reject when any required observable fact fails. Do not reject merely because the composition is less elegant than expected.

## Rejection Notes

Use this compact order:

```text
Passed context; blocking mismatch; exact correction for the next attempt.
```

Example:

```text
P1 square without hands or text; 5 garlic cloves are visible instead of 6 and optional harissa was added; show exactly 6 separate cloves and omit all harissa.
```

Name visible evidence, not speculation about the model. Include every blocking defect so the next retry does not correct only the first one. Preserve passed facts likely to regress, but do not restate the full base prompt. Never use `non conforme`, `bad image`, or `retry` alone.

## Retry Choice

- **Targeted edit:** use for one or two local defects while layout and recipe identity are otherwise correct.
- **Fresh generation:** use for wrong recipe identity, many count or measurement errors, photorealistic or multi-panel output, or a missing composition.
- **Blocked:** preserve evidence when the attempt budget is exhausted; do not reopen automatically.
- **Prompt or source repair:** use when repeated failures expose ambiguous or contradictory generated instructions. Validate the pipeline before spending more attempts and never patch an immutable active claim.

An edit is still a new attempt. It uses the currently claimed prompt and previous evidence, undergoes full visual review, and is recorded through the normal review receipt.

## Wave Discipline

Generate only claimed items and keep one output mapped to one `attempt_id`. Review every output before recording the wave. Make the receipt durable before discarding image-generation context. Then run validation and status and report current accepted, rejected, blocked, claimed, and pending counts.

If one rejection category dominates several recipes, stop spending attempts and report the aggregate pattern before reopening blocked panels.
