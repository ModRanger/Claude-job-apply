# Job Search — Local Handoff

**Generated:** 2026-06-10 • For: Viet Bui (viet.bui3@gmail.com)
**Branch:** `claude/multi-tool-job-apply-5m8292` (both repos)
**PRs open:** ApplyPilot #1, Claude-job-apply #1

This file is your single source of truth to continue locally. Everything referenced
lives in the `Claude-job-apply` repo unless noted.

---

## 0. TL;DR — what to do first

1. Clone both repos locally on this branch (commands in §4).
2. Apply to the **3 ready jobs** (§1) — forms need a browser, so this is you + a browser, or ApplyPilot.
3. Send the **3 LinkedIn DMs** (§2) and **2 emails** (§3).
4. Set up **ApplyPilot** (§5) for volume auto-apply.
5. Optional: run **Claude Code + browser MCP locally** (§6) so Claude can drive forms with you.

---

## 1. APPLY NOW — 3 ready jobs (all verified live 2026-06-10)

Materials are in `output/`. Resume PDFs are in `output/pdf/`. Form-field answers for
every standard question are in `output/application-kit.md`.

### ① Immutable — Senior BD Manager, Americas  (fit 4.3/5) ⭐ top pick
- Apply: https://jobs.lever.co/immutable/873e93e2-86e0-4695-94bc-9f800a930bce/apply
- Resume: `output/pdf/Viet_Bui_Resume_Immutable.pdf`
- Cover letter: `output/immutable-sr-bd-manager/cover-letter.md` (v2, tuned to real JD)
- **Comp band is $229,450–$267,800** — say "posted range works for me"; never quote lower.
- Closes 2026-06-30. Circle Back Initiative employer = they reply to every applicant.

### ② Base (Coinbase ecosystem) — Social Media Manager  (fit 4.2/5) ⏰ time-sensitive
- Apply: https://web3.career/i/yEzMwUTM  (live, posted 2026-06-09, Remote-USA)
- Resume: `output/pdf/Viet_Bui_Resume_Base.pdf`
- Cover letter: `output/base-social-media-manager/cover-letter.md`
- Rate ask $70–80K. Likely agency/EOR-employed embedded w/ Coinbase Base team — confirm in screen 1.

### ③ Function Health — Executive Assistant to CEO (Ezra)  (fit 3.8/5) — fastest loop
- Step 1 — form: https://www.functionhealth.com/careers → EA to CEO
- Resume: `output/pdf/Viet_Bui_Resume_FunctionHealth.pdf`
- Step 2 — email talent@functionhealth.com (text in §3) AFTER submitting the form.
- Comp $80–100K. JD waives the EA-title requirement; founder/AI-fluent profile is the angle.

---

## 2. SEND — 3 LinkedIn DMs (full text in `interview-prep/outreach-dms.md`)

⚠️ Verify each person still holds the role before sending (web-sourced 2026-06-10).

1. **Sam Frankel** — Head of Ecosystem @ Base — linkedin.com/in/sam-frankel-0a082771
2. **Mark Greenberg** — Kraken (announced self-serve listings) — linkedin.com/in/marklg
3. **Vlad Nazar** — Head of BD @ ChainGPT — linkedin.com/in/vladnazarxyz
   - ChainGPT also has 2 LIVE postings: BD & Partnerships (Launchpad) + SaaS Sales — apply too.

---

## 3. SEND — 2 email applications

Once Gmail is connected in a LOCAL Claude session, ask Claude to draft these.
Otherwise copy-paste from the files below and attach the matching PDF.

1. **Function Health** → talent@functionhealth.com
   - Body: `output/function-health-ea/email-to-talent.md`
   - Attach: `output/pdf/Viet_Bui_Resume_FunctionHealth.pdf`
   - Contains your real AI-workflow paragraph (this pipeline). Send AFTER the careers form.

2. **Common Prefix — BD Lead** ($90–130K + stock, remote worldwide) → careers@commonprefix.com
   - Body: `output/common-prefix-bd-lead/email-application.md`
   - Attach: `output/pdf/Viet_Bui_Resume_Immutable.pdf` (BD-framed, fits as-is)
   - ⚠️ Add ONE sentence about their actual research before sending (it's a research firm).

---

## 4. Clone locally

Everything is merged to `main`, so plain clones get it all (no branch flag needed).

**macOS / Linux:**
```bash
git clone https://github.com/ModRanger/Claude-job-apply   # evals, CVs, tracker, this handoff
git clone https://github.com/ModRanger/ApplyPilot         # auto-apply engine
```

**Windows (PowerShell)** — run each line separately (`&&` fails in PowerShell 5.1):
```powershell
git clone https://github.com/ModRanger/Claude-job-apply
git clone https://github.com/ModRanger/ApplyPilot
```

Your pre-filled ApplyPilot profile is `ApplyPilot/profile.viet.json`.

---

## 5. ApplyPilot setup (volume auto-apply with a real browser)

**macOS / Linux (bash):**
```bash
cd ApplyPilot
pip install applypilot
pip install --no-deps python-jobspy && pip install pydantic tls-client requests markdownify regex
mkdir -p ~/.applypilot
echo 'GEMINI_API_KEY=PASTE_YOUR_GEMINI_KEY_HERE' >> ~/.applypilot/.env   # NOT stored in git
cp profile.viet.json profile.json   # then open it, add your job-site password if needed
applypilot init      # point at profile.json + your resume
applypilot doctor    # confirms Chrome, Node, key
applypilot run -w 4  # discover → score → tailor → cover letters
applypilot apply --dry-run   # WATCH it fill forms without submitting — do this first
applypilot apply -w 3        # then let it submit
```

**Windows (PowerShell)** — one command per line; `Add-Content`, not `echo >>`:
```powershell
cd .\ApplyPilot
pip install applypilot
pip install --no-deps python-jobspy
pip install pydantic tls-client requests markdownify regex
New-Item -ItemType Directory -Force "$HOME\.applypilot"
Add-Content "$HOME\.applypilot\.env" "GEMINI_API_KEY=PASTE_YOUR_GEMINI_KEY_HERE"
Copy-Item profile.viet.json profile.json
applypilot init
applypilot doctor    # confirms Python 3.11+, Node, Chrome, key
applypilot run -w 4
applypilot apply --dry-run
applypilot apply -w 3
```

If `doctor` flags a missing prereq: Python 3.11+ (`python --version`, python.org, tick
"Add to PATH"), Node.js LTS (`node --version`, nodejs.org), Chrome (normal install).

⚠️ Your Gemini key is NOT in this file or git (repo secret-scanning blocks it, correctly).
Paste it into `~/.applypilot/.env` locally as shown above. Rotate it after the search.

⚠️ Review `--dry-run` output before live `apply`. With the widened target list it will
hit admin/SDR roles too; confirm the tailored resumes don't overstate.

---

## 6. Optional: Claude Code + browser locally (drive forms together)

```bash
# in the Claude-job-apply repo, with Claude Code CLI installed:
claude mcp add playwright -- npx @playwright/mcp@latest
claude              # then: "open the Immutable apply link and fill it from output/application-kit.md"
```

This gives Claude a visible Chrome window on your machine — it fills each field, you watch,
you click Submit. Best for the 3 high-stakes apps in §1.

---

## 7. Full evaluation results (24 roles) — see `data/applications.md` + `reports/`

**Apply-worthy (≥3.6):** Immutable 4.3, Base 4.2, Nexo 3.8 (if comp clears $60K),
Common Prefix 3.8, Function Health 3.8, Sahara AI 3.6, Brale 3.6 (via COO DM only).

**Everything else** (16 roles) scored below bar or dead — reasons in `data/pipeline.md`.

**Pattern learned:** your profile wins on remote-first, founder-facing BD/social/community
roles at mid-size crypto cos. It loses on (a) NYC on-site gates, (b) "5+ yrs institutional/
DeFi" bars, (c) generic corporate EA roles. Direct DMs > dead job boards for the 1-week goal.

**Queued, not yet evaluated:** Tether Influencer Marketing Mgr ($104–144K), WOO Social &
Community Exec ($90–115K) — both in `data/pipeline.md` "Pending". Ask Claude to evaluate.

---

## 8. Interview prep (ready when calls come in)

- `interview-prep/story-bank.md` — 8 STAR+R stories (40-Deal Rolodex, $2M Raise,
  Treasury Through the Cycle, Two Salons Full Stack, Bear-Market BD, Chef-Speed, etc.)
- Negotiation scripts + comp targets: `modes/_profile.md`

---

## 9. Tracker maintenance

After you send applications, tell Claude (locally) "mark Immutable/Base/etc as Applied"
or update `data/applications.md` status column by hand. Health check: `node verify-pipeline.mjs`.
