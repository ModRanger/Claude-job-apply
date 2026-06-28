---
name: tailored-application-package-generation
description: Workflow command scaffold for tailored-application-package-generation in Claude-job-apply.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /tailored-application-package-generation

Use this workflow when working on **tailored-application-package-generation** in `Claude-job-apply`.

## Goal

Creates tailored CVs and cover letters for shortlisted roles, outputting them in role-specific directories.

## Common Files

- `output/*/cover-letter.md`
- `output/*/cv-*.md`
- `output/*/email-application.md`
- `output/application-kit.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Draft and save a tailored cover letter in output/<role>/cover-letter.md
- Draft and save a tailored CV in output/<role>/cv-<candidate>-<role>.md
- Optionally, add email templates or application kits for the role

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.