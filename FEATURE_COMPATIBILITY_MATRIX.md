# FRONTIERPILOT 2.0 — FEATURE COMPATIBILITY MATRIX

This document evaluates every capability from the source application (`career-ops` web engine) against FrontierPilot 2.0 / LinkedIn Autonomous Creator Studio architecture.

---

## Compatibility Classification Key
- **A. DIRECT INTEGRATION:** Can be incorporated with minimal changes.
- **B. ADAPTABLE INTEGRATION:** Requires adaptation to fit FrontierPilot's Netlify/Python/SQLite architecture.
- **C. ARCHITECTURAL INTEGRATION:** Requires database, service, or serverless API bridge.
- **D. DESIGN INTEGRATION:** Provides UI components or interaction patterns fitting FrontierPilot's Cosmic Dark design system.
- **E. REDUNDANT:** Already exists in FrontierPilot.
- **F. INCOMPATIBLE:** Conflicts with FrontierPilot architecture or product direction.
- **G. NOT WORTH INTEGRATING:** Adds operational complexity without meaningful user value.

---

## 1. Feature Evaluation Matrix

| Source Feature | Category | FrontierPilot Equivalent | Classification | Recommendation & Action Plan |
|---|---|---|---|---|
| **A-H Structured Scoring & Evaluation Engine** | Intelligence | FrontierPilot Match Score (0–100%) | **B. ADAPTABLE INTEGRATION** | **ADAPT & ENHANCE:** Upgrade FrontierPilot's heuristic matcher with career-ops's 8-block criteria (Work Auth, Scope, Tech Stack, Compensation Realism, Team Signals, Risk Assessment). |
| **Interactive CV Studio & ATS Keyword Coverage** | Resume & Apply | `generate_tailored_resume.py` & markdown resumes | **B. ADAPTABLE INTEGRATION** | **INTEGRATE:** Add visual Keyword Coverage and Bullet Tailoring studio into FrontierPilot's web interface (`docs/frontierpilot.html`) with real-time diff preview. |
| **Multi-Role Comparative Decision Matrix** | Analytics | None (single-card radar view) | **A. DIRECT INTEGRATION** | **INTEGRATE:** Add a "Compare Roles" modal/tab in FrontierPilot to evaluate 2–4 opportunities side-by-side across match score, compensation, and remote policy. |
| **Follow-up Cadence & Outreach Tracker** | CRM / Lifecycle | Basic status tracking in SQLite | **B. ADAPTABLE INTEGRATION** | **INTEGRATE:** Add follow-up categorization (*Urgent, Overdue, Waiting, Cold*) and one-tap follow-up draft generation linked to Slack approval cards. |
| **Multi-Portal Ingestion & Web Scraper Bridge** | Ingestion | Manual JSON seed & Apify integration | **C. ARCHITECTURAL INTEGRATION** | **INTEGRATE:** Connect career-ops's portal scan output to FrontierPilot's `testing/frontierpilot.db` and Netlify edge gateway (`/api/frontierpilot/jobs`). |
| **Scheduled Background Cron Scans** | Automation | `daily_frontierpilot_sync.yml` & Netlify Cron | **E. REDUNDANT / MERGE** | **MERGE:** Keep FrontierPilot's GitHub Actions 24/7 runner while adopting career-ops's portal deduplication rules. |
| **Local Full-Screen Next.js App replacement** | Architecture | FrontierPilot Single-Page PWA & Netlify Serverless | **F. INCOMPATIBLE** | **REJECT:** Do NOT replace FrontierPilot's lightweight 24/7 cloud architecture with a heavy local Next.js instance. Retain PWA + Netlify edge. |
| **Heavy Local Dev Tools / Shaders** | UI / FX | Lightweight CSS Glows & Framer Dark theme | **G. NOT WORTH INTEGRATING** | **REJECT:** Shaders add multi-megabyte bundle overhead without improving user productivity. |

---

## 2. Deep Dive: Selected High-Leverage Integrations

### Integration 1: A-H Deterministic Evaluation & Match Score Synthesis
- **Why it belongs in FrontierPilot:** Currently FrontierPilot uses a numerical score (e.g. 96%). Adding the structured A-H breakdown gives the user deep transparency into *why* a role scored 96% and flags hidden risks (e.g., relocation mandates, missing visa sponsorship).
- **Files Changed:**
  - `lib/frontierpilot_integrator.py`: Add A-H block parser.
  - `netlify/functions/frontierpilot.mjs`: Return structured evaluation blocks with opportunity details.
  - `docs/frontierpilot.html`: Render A-H evaluation breakdown in the Opportunity Modal.
- **Dependencies:** Google Gemini API (already configured).
- **Risk:** Low. Fully backwards-compatible.

### Integration 2: Interactive CV Studio & ATS Keyword Coverage
- **Why it belongs in FrontierPilot:** FrontierPilot already generates tailored resumes in markdown. Providing an interactive keyword gap badge and bullet-level editor empowers the user to inspect and polish the resume before exporting.
- **Files Changed:**
  - `docs/frontierpilot.html`: Add CV Studio modal with keyword chips and bullet diff editor.
  - `netlify/functions/frontierpilot.mjs`: Add `/api/frontierpilot/tailor` endpoint.
- **Dependencies:** None.
- **Risk:** Low.

### Integration 3: Multi-Role Comparative Decision Matrix
- **Why it belongs in FrontierPilot:** When evaluating offers (e.g., GSoC vs. MLH vs. Handshake vs. Research Fellowships), a side-by-side comparison table highlights comp, workload, and career leverage instantly.
- **Files Changed:**
  - `docs/frontierpilot.html`: Add "Compare Matrix" view.
- **Dependencies:** None.
- **Risk:** Zero. Pure additive UI enhancement.

### Integration 4: Follow-up Cadence & Outreach Tracker
- **Why it belongs in FrontierPilot:** Connects the loop between applying and landing interviews. Categorizes submitted jobs into action buckets (*Urgent, Overdue, Waiting*).
- **Files Changed:**
  - `testing/frontierpilot.db`: Add `applied_date` and `last_contact_date` columns if not present.
  - `lib/frontierpilot_integrator.py`: Add follow-up cadence calculator.
  - `docs/frontierpilot.html`: Add Follow-up filter pill and quick outreach generator.
- **Dependencies:** None.
- **Risk:** Low.
