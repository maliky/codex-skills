# Class Refactor Patterns

Use this reference when repeated layout or macro breakages require a class-side refactor.

- keep a minimal diff
- avoid global reformatting for one document family
- preserve legacy sectioning behavior unless migration is explicit
- prefer guard-style class conditionals over hard-coded document assumptions
