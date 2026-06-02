# Curriculum Grammar

Use this reference when shaping TU curriculum Org into the expected section, table, and course-description grammar.

## Purpose

Use this as a harmonized target grammar for TU curricula while allowing local variation in visible wording.

## Core grammar

Curriculum =
- Identity
- FrontMatter
- CurricularPrograms
- [MinorOrEmphasisAreas]
- CourseDescriptions

Identity =
- CollegeName or UniversityName
- [CurriculumTitle]
- [Acronym]
- [RevisionYear or approval marker]

FrontMatter =
- [Introduction]
- [Vision]
- [Mission]
- [SharedRequirements]
- [SharedGeneralEducation]
- [Other stable front-matter sections]

CurricularPrograms =
- (ProgramGroup | Program)+

ProgramGroup =
- GroupName
- [GroupIntro]
- Program+

Program =
- ProgramName
- [ProgramOverview]
- [ProgramObjectives]
- [ProgramLearningOutcomes]
- [GraduationRequirements]
- YearPlan+

YearPlan =
- YearLabel
- SemesterTable6

MinorOrEmphasisAreas =
- (MinorArea | EmphasisArea)+

MinorArea =
- MinorName
- MinorTable4
- [MinorNote]

EmphasisArea =
- EmphasisName
- MinorTable4 or structurally equivalent table
- [EmphasisNote]

CourseDescriptions =
- [SharedCollegeCourseDescriptions]
- CourseDescriptionGroup+

CourseDescriptionGroup =
- GroupName
- [Vision]
- [Mission]
- CourseEntry+

CourseEntry =
- Code
- Title
- Credits
- [Prerequisites]
- Description

## What can vary

Visible labels can differ across colleges:
- `Minor`
- `Emphasis`
- `Concentration`
- `Major field of specialization`

Map these into the same structural slot only when their function is equivalent.

## Grouping rule

Prefer grouping course descriptions by department where the source supports it.

Use an `Other` group only when:
- courses belong directly to the college
- courses come from another college or department but are retained in the curriculum source
- the source does not provide a cleaner stable grouping

## Table families

- RequirementsTable2: requirement | Cr
- CourseListTable3: code | title | Cr
- SummaryTable3: label | sublabel | Cr
- MinorTable4: no. | code | title | Cr
- SemesterTable6: code | title | Cr || code | title | Cr

Choose the family based on semantic role, not just column count in the imported file.
