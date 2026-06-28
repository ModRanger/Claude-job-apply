---
name: pipeline-batch-evaluation-and-tracking
description: Workflow command scaffold for pipeline-batch-evaluation-and-tracking in Claude-job-apply.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /pipeline-batch-evaluation-and-tracking

Use this workflow when working on **pipeline-batch-evaluation-and-tracking** in `Claude-job-apply`.

## Goal

Evaluates a batch of job leads, merges tracker TSVs, updates applications and pipeline, and generates evaluation reports.

## Common Files

- `batch/tracker-additions/merged/*.tsv`
- `data/applications.md`
- `data/pipeline.md`
- `reports/*.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Add new TSV files for each evaluated lead to batch/tracker-additions/merged/
- Update data/applications.md and data/pipeline.md with results and status
- Generate detailed evaluation reports in reports/ (one per lead)

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.