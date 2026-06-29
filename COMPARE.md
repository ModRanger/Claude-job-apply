# Comparing the three job-apply tools

You have three repos. They are NOT three versions of the same thing — they do
different jobs. This file is how to clone, run, and compare them.

## Clone all three side by side

**macOS / Linux (bash):**
```bash
mkdir ~/job-apply-tools && cd ~/job-apply-tools
git clone https://github.com/ModRanger/ApplyPilot
git clone https://github.com/ModRanger/EasyApplyJobsBot
git clone https://github.com/ModRanger/Claude-job-apply
```

**Windows (PowerShell):** `&&` is not a valid separator in Windows PowerShell 5.1 —
run each line on its own. You don't need a wrapper folder; cloning into any working
folder drops the three repos side by side.
```powershell
git clone https://github.com/ModRanger/ApplyPilot
git clone https://github.com/ModRanger/EasyApplyJobsBot
git clone https://github.com/ModRanger/Claude-job-apply
```

All three default to `main`. Your customizations (ApplyPilot `profile.viet.json`,
Claude-job-apply evals + `HANDOFF.md`) are already merged into `main`, so a plain
clone gets everything — no feature branch to track.

## What each one is

| | ApplyPilot | EasyApplyJobsBot | Claude-job-apply (this repo) |
|---|---|---|---|
| Role | Autonomous apply engine | LinkedIn Easy Apply bot | Quality / evaluation layer |
| Flow | discover → score → tailor → **submit** | apply to LinkedIn Easy Apply listings | evaluate fit, write tailored CVs, track — **never submits** |
| Coverage | 5 boards + Workday + direct sites | LinkedIn only | whatever you paste / scan |
| Browser | drives Chrome itself | Selenium on LinkedIn | none (preps; you click) |
| Needs | Python 3.11+, Node, free Gemini key, Chrome | Python + your LinkedIn password | Claude Code |
| Risk | Low (dry-run first) | **High — LinkedIn bans automation** | None |
| Best for | volume across many boards | (skip — redundant + risky) | your 5 high-fit roles |

## How to compare them fairly

### ApplyPilot — the real contender

**macOS / Linux (bash):**
```bash
cd ~/job-apply-tools/ApplyPilot
pip install applypilot
pip install --no-deps python-jobspy && pip install pydantic tls-client requests markdownify regex
mkdir -p ~/.applypilot && echo 'GEMINI_API_KEY=PASTE_YOUR_KEY' >> ~/.applypilot/.env
cp profile.viet.json profile.json     # add a job-site password only if you want auto-submit on gated sites
applypilot doctor                      # <-- best 5-second test: shows what's installed/missing
applypilot run -w 4                    # discover → score → tailor → cover letters
applypilot apply --dry-run             # WATCH it fill forms without submitting — the real evaluation
applypilot apply -w 3                  # only after dry-run looks right
```

**Windows (PowerShell):** one command per line; use `Add-Content`, not `echo >>`.
```powershell
cd .\ApplyPilot
pip install applypilot
pip install --no-deps python-jobspy
pip install pydantic tls-client requests markdownify regex
New-Item -ItemType Directory -Force "$HOME\.applypilot"
Add-Content "$HOME\.applypilot\.env" "GEMINI_API_KEY=PASTE_YOUR_KEY"
Copy-Item profile.viet.json profile.json
applypilot doctor          # confirms Python 3.11+, Node, Chrome are present
applypilot run -w 4
applypilot apply --dry-run # WATCH it fill forms without submitting
applypilot apply -w 3      # only after dry-run looks right
```

**Prereqs `doctor` checks (install if it flags ❌):**
- Python 3.11+ → `python --version`; get it at python.org (tick "Add to PATH" on Windows)
- Node.js → `node --version`; get the LTS at nodejs.org
- Chrome → normal desktop install; auto-detected

### EasyApplyJobsBot — inspect, probably don't run
- Read `config.py` and `README.md` first.
- It covers only LinkedIn Easy Apply (ApplyPilot already does this) and wants your
  LinkedIn password in plaintext config. LinkedIn actively bans automation — a banned
  account mid-search is a real cost with no added coverage. Recommendation: clone to
  look at, not to run.

### Claude-job-apply — the quality layer (not a competitor)
- Open `HANDOFF.md`, run a local Claude Code session in this folder.
- Use it for the high-fit targets: evaluate, tailor, generate PDFs, track in
  `data/applications.md`. It deliberately stops before Submit so you keep final say.

## Likely verdict

ApplyPilot for volume + Claude-job-apply for your top 5 roles is the combo.
EasyApplyJobsBot loses on coverage and risk. Run `applypilot doctor` first — it tells
you immediately whether your machine can run the autonomous path.

## Reminder
- Paste your Gemini key only into the local `~/.applypilot/.env`, never into git.
- Rotate the key once the search is done.
