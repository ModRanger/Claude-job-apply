---
name: pipeline-lead-queue-and-triage
description: Workflow command scaffold for pipeline-lead-queue-and-triage in Claude-job-apply.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /pipeline-lead-queue-and-triage

Use this workflow when working on **pipeline-lead-queue-and-triage** in `Claude-job-apply`.

## Goal

Queues new leads into the pipeline and later triages/removes them based on fit or status.

## Common Files

- `data/pipeline.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add new leads to data/pipeline.md
- Review and update data/pipeline.md to remove or comment on leads after triage

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.