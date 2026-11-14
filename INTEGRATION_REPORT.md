# FRONTIERPILOT 2.0 — SOURCE FEATURE EXTRACTION & INTEGRATION REPORT

**Target Branch:** `frontierpilot-2.0` (Separated from `main`)  
**Lead Architect:** Principal Software Architect & QA Lead  
**Audit & Integration Date:** November 14, 2026  

---

## 1. Source Application Overview
The source application is `career-ops` (v1.40.0), a full-stack Next.js 16 application running at `http://127.0.0.1:3000`. It was built to solve local job operations: headless scraping across ATS providers (Ashby, Greenhouse, Lever, Workable), deterministic prompt scoring (A-H structured evaluations), bullet-level resume tailoring, and follow-up tracking.

## 2. Complete Feature Inventory
- **Multi-Portal Ingestion & Headless Scraping:** Scrapes public ATS boards without LLM tokens.
- **A-H Structured Scoring & Evaluation Engine:** Evaluates roles across 8 deterministic blocks (Work Auth, Scope, Tech Stack, Compensation, Red Flags, Tailoring, Final Score).
- **Interactive CV Studio & ATS Keyword Coverage:** Identifies missing keywords and rewrites resume bullets.
- **Role Decision Matrix (Compare):** Renders a side-by-side comparison table of multiple offers.
- **Follow-up Cadence & Outreach Tracker:** Groups jobs into *Urgent, Overdue, Waiting, Cold* and suggests outreach drafts.
- **Scheduled Background Scans:** Cron-based job watcher.

## 3. Selected Features for Integration
1. **Role Decision Matrix (Compare Engine):** Side-by-side evaluation of 2–4 opportunities across Match Score, Compensation, Category, Location, and Superpowers.
2. **Follow-Up Cadence & Recruiter Outreach Tracker:** Automatic classification of submitted roles into *Urgent (7–10d)*, *Overdue (>14d)*, *Waiting (<5d)*, and *Cold (>30d)* with one-tap follow-up draft generation.
3. **Structured A-H Evaluation Transparency:** Direct rendering of Blocks A through H inside Opportunity Intelligence notes.
4. **Interactive ATS Keyword Coverage Progress:** Real-time visibility into matched vs gap skills against Aryan's verified profile.

## 4. Rejected Features & Architectural Rationale
- **Replacing FrontierPilot with Next.js SPA:** *Rejected.* FrontierPilot's core strength is its lightweight 24/7 serverless deployment on Netlify edge and mobile PWA. Running a heavy local Next.js node server would break continuous cloud operation without local machines.
- **Web UI Shader FX (`@paper-design/shaders-react`):** *Rejected.* Adds heavy WebGL dependencies without adding career leverage.
- **Complex Multi-Step Wizard Onboarding:** *Rejected.* FrontierPilot uses direct 1-tap Slack approval and Notion sync.

## 5. Integration Architecture
FrontierPilot maintains its unified Cosmic Framer Dark theme, Netlify edge serverless API gateway, SQLite WAL persistence, and Slack Block Kit mobile hub. The newly extracted capabilities from `career-ops` operate natively within FrontierPilot:
- Python Backend: `lib/frontierpilot_integrator.py` provides `evaluate_structured_blocks()`, `compute_followup_cadence()`, `compare_opportunities()`, and `analyze_keyword_coverage()`.
- Serverless Edge: `netlify/functions/frontierpilot.mjs` exposes `/api/frontierpilot/followups`, `/api/frontierpilot/compare`, and `/api/frontierpilot/cv_studio`.
- Glassmorphic Web PWA: `docs/frontierpilot.html` renders the new *Role Decision Matrix* tab and *Follow-Up Cadence* tab, plus A-H evaluation cards in Opportunity Details.

## 6. Backend Changes
- Enhanced `lib/frontierpilot_integrator.py` with 4 new production methods:
  - `evaluate_structured_blocks(opp)`
  - `compute_followup_cadence(opps)`
  - `compare_opportunities(opp_ids)`
  - `analyze_keyword_coverage(opp)`
- Added endpoints in `netlify/functions/frontierpilot.mjs` for edge delivery.

## 7. Frontend Changes
- Navigation Sidebar: Added `Role Decision Matrix` and `Follow-Up Cadence` tabs.
- Viewports: Added `#tabCompare` and `#tabFollowups` responsive containers.
- Opportunity Details Drawer: Embedded Structured A-H Matrix and ATS Keyword Coverage progress bar.
- Outreach Actions: Integrated 1-tap recruiter follow-up email template copy to clipboard.

## 8. Database & Data Integrity
- Maintained SQLite WAL schema in `testing/frontierpilot.db`.
- Backwards compatible: No destructive migrations or deleted tables.

## 9. Files Modified
- `lib/frontierpilot_integrator.py`
- `netlify/functions/frontierpilot.mjs`
- `docs/frontierpilot.html`
- `tests/test_frontierpilot_integrator.py`
- `SOURCE_APPLICATION_AUDIT.md` (New)
- `SOURCE_FEATURE_INVENTORY.md` (New)
- `SOURCE_ARCHITECTURE_MAP.md` (New)
- `SOURCE_API_INVENTORY.md` (New)
- `FEATURE_COMPATIBILITY_MATRIX.md` (New)

## 10. Tests Executed & Results
- **Unit & Integration Tests:** 145/145 tests passed (`Ran 145 tests in 19.761s, OK`).
- **Playwright Headless Browser Tests:** All 6 high-resolution viewports and mobile layouts validated without console errors.
- **Git Separation:** All changes reside on branch `frontierpilot-2.0`. Branch `main` remains untouched.

## 11. Captured Screenshots
Located in `testing/source_audit/frontierpilot_integration/`:
1. `01_dashboard.png`: Executive Career Overview & Funnel
2. `02_decision_matrix.png`: Multi-Role Side-by-Side Decision Matrix
3. `03_followup_cadence.png`: 4-Column Urgency Cadence Board
4. `04_roles_with_ah_matrix.png`: Opportunity Details with A-H Evaluation & ATS Progress Bar
5. `05_mobile_matrix.png`: iPhone Mobile Responsive Decision Matrix
6. `06_mobile_followups.png`: iPhone Mobile Responsive Follow-up View

## 12. Remaining Risks & Mitigations
- **Network Fluctuation on Netlify Edge:** Mitigated via offline-first LocalStorage / IndexedDB fallback in `frontierpilot.html`.
- **ATS Keyword Over-Optimization:** Verified anti-hallucination policy against Aryan's master profile.

## 13. Rollback Instructions
If desired, you can switch back to `main` at any time:
```bash
git checkout main
```
To delete the experimental branch without affecting anything:
```bash
git branch -D frontierpilot-2.0
```
