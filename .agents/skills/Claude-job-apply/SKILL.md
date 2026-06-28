```markdown
# Claude-job-apply Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill covers the development and operational patterns used in the `Claude-job-apply` repository, a Python-based toolkit for evaluating job leads, tracking applications, and generating tailored application materials. The repository is workflow-driven, with a focus on batch processing, pipeline management, and document generation for job applications. No external frameworks are used, and the codebase emphasizes clarity and modularity.

## Coding Conventions

- **File Naming:**  
  Files are named using kebab-case, e.g., `lead-evaluator.py`, `pipeline-manager.py`.

- **Import Style:**  
  Relative imports are used throughout the codebase.
  ```python
  from .utils import parse_lead
  from .evaluation import evaluate_batch
  ```

- **Export Style:**  
  Named exports are preferred. Functions and classes are explicitly exported.
  ```python
  # In lead-evaluator.py
  def evaluate_lead(lead):
      ...

  __all__ = ['evaluate_lead']
  ```

- **Directory Structure:**  
  - `batch/tracker-additions/merged/`: Contains merged TSV files for batch evaluations.
  - `data/`: Stores pipeline and application tracking markdown files.
  - `output/`: Contains generated application packages per role.
  - `reports/`: Holds detailed evaluation reports.

## Workflows

### Pipeline Batch Evaluation and Tracking
**Trigger:** When a new batch of job leads needs to be evaluated and tracked.  
**Command:** `/batch-evaluate-leads`

1. Add new TSV files for each evaluated lead to `batch/tracker-additions/merged/`.
2. Update `data/applications.md` and `data/pipeline.md` with evaluation results and current status.
3. Generate detailed evaluation reports in `reports/`, one per lead.

**Example:**
```bash
# Add new batch TSVs
cp new-leads.tsv batch/tracker-additions/merged/

# Run evaluation script
python -m evaluation.batch_evaluate batch/tracker-additions/merged/new-leads.tsv

# Update pipeline and applications
python -m pipeline.update data/pipeline.md data/applications.md

# Generate reports
python -m reports.generate batch/tracker-additions/merged/new-leads.tsv
```

### Tailored Application Package Generation
**Trigger:** When a candidate is ready to apply to a specific role that passed the evaluation bar.  
**Command:** `/generate-application-package`

1. Draft and save a tailored cover letter in `output/<role>/cover-letter.md`.
2. Draft and save a tailored CV in `output/<role>/cv-<candidate>-<role>.md`.
3. Optionally, add email templates or application kits for the role.

**Example:**
```bash
# Generate cover letter
python -m application.generate_cover_letter --role "Data Scientist" --output output/data-scientist/cover-letter.md

# Generate tailored CV
python -m application.generate_cv --candidate "Jane Doe" --role "Data Scientist" --output output/data-scientist/cv-jane-doe-data-scientist.md

# (Optional) Add application kit
cp templates/application-kit.md output/data-scientist/application-kit.md
```

### Pipeline Lead Queue and Triage
**Trigger:** When new leads are discovered or when queued leads need to be reviewed.  
**Command:** `/queue-lead`

1. Add new leads to `data/pipeline.md`.
2. Review and update `data/pipeline.md` to remove or comment on leads after triage.

**Example:**
```markdown
# In data/pipeline.md

| Lead | Status      | Notes               |
|------|-------------|---------------------|
| Acme | Queued      | Awaiting evaluation |
| Beta | Triaged Out | Not a good fit      |
```

## Testing Patterns

- **Test File Naming:**  
  Test files follow the pattern `*.test.*`, e.g., `lead-evaluator.test.py`.
- **Framework:**  
  No specific testing framework detected. Tests may be written using Python's built-in `unittest` or similar.
- **Example:**
  ```python
  # In lead-evaluator.test.py
  from .lead-evaluator import evaluate_lead

  def test_evaluate_lead_basic():
      lead = {...}
      result = evaluate_lead(lead)
      assert result['score'] > 0
  ```

## Commands

| Command                      | Purpose                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| /batch-evaluate-leads        | Evaluate a batch of job leads and update trackers and reports           |
| /generate-application-package| Generate tailored CV and cover letter for a specific role               |
| /queue-lead                  | Add new leads to the pipeline and manage triage                         |
```