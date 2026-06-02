# Class Refactor Patterns

Use this route for repeated layout or macro breakages.

- keep a minimal diff
- avoid global reformatting for one document family
- preserve legacy sectioning behavior unless migration is explicit
- prefer guard-style class conditionals over hard-coded document assumptions
