---
name: courses-budget-engineering
description: "Maintain the Courses grocery-budget application in /home/jil/Courses: private receipt imports and OCR proposals, catalogue associations, financial confirmation, typed Django/PostgreSQL services, shared tables, and safe data migrations or publication. Use for household purchases, not academic course catalogues."
---

# Courses Budget Engineering

Work from `AGENTS.md`, `DEV.org`, `Cahier_des_charges_budget_courses_v0_2.org`, `ARCHITECTURE.org`, `README.org`, `MANUAL.org`, and the relevant acceptance notes in `RECETTE.org`. Distinguish confirmed requirements from proposed extensions. Current modules and commands can evolve independently of the published application.

## Workflow

1. Confirm the checkout, dirty work and target environment. Identify whether the request changes documentary evidence, product identity, categorisation, financial facts, or presentation.
2. Keep business writes in typed transactional domain services. Views, forms and TypeScript compose the interaction; permissions, amounts, relation checks and batch invariants remain on the server.
3. Preserve original receipt files and transcriptions. Machine output and suggested associations remain proposals until the corresponding explicit confirmation.
4. Implement the smallest complete slice, including its migration/export contract when relevant, then verify financial and space-isolation invariants before browser details.

## Routes

- **Receipts, prices, quantities, catalogue identity, or business extensions**: read [domain and evidence](references/domain-and-evidence.md).
- **Typed interfaces, shared tables, verification, data preparation, or release work**: read [development and publication](references/development-and-publication.md).
- **DNS, TLS or host service wiring**: use `koba-vps-webops` alongside this skill when the requested task crosses that boundary.

## Report

Name the business facts changed, confirmation state, migration/export impact and checks actually run. Distinguish local implementation, production data changes and publication. Use synthetic examples in shared reports and tests.
