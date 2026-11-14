# SOURCE FEATURE INVENTORY — Detailed Capability Breakdown

**Source Application:** `career-ops` Web Cockpit (`http://127.0.0.1:3000`)

---

### Feature 1: Multi-Portal Zero-Token & Playwright Scanner
- **Purpose:** Automatically scrapes, parses, and ingests job postings from company career pages without consuming expensive LLM tokens.
- **User Problem Solved:** Eliminates manual job board surfing across hundreds of company pages.
- **User Journey:** User navigates to `/explore`, clicks "Scan (FREE)", system queries APIs or launches headless Playwright scrapers, extracts title, location, salary, URL, and deposits them into the inbox.
- **Frontend Components:** `ExploreView`, `FacetChips`, `ScanProgressBar`, `DateRangeFilter`.
- **Backend Functionality:** `scan.mjs`, `scan-ats-full.mjs`, `lib/board-api-catalog.mjs`.
- **API Endpoints:** `POST /api/explore`, `GET /api/explore`.
- **Implementation Status:** Fully implemented.

---

### Feature 2: Structured Job Evaluation (A-H Report & 1-5 Scoring)
- **Purpose:** Analyzes any job listing against the candidate's profile across 8 deterministic dimensions:
  1. Block A: Work Authorization & Location Check
  2. Block B: Role Clarity & Scope
  3. Block C: Technical Stack & Superpower Alignment
  4. Block D: Team Structure & Seniority
  5. Block E: Compensation Realism
  6. Block F: Red Flags & Risk Indicators
  7. Block G: Tailoring Strategy
  8. Block H: Final Score (1.0 to 5.0) & Recommendation
- **User Problem Solved:** Eliminates guesswork on whether a job is worth applying for.
- **User Journey:** User pastes a job URL or selects one from the inbox, clicks "Evaluate", system generates report and calculates 1.0–5.0 score.
- **Frontend Components:** `ReportView`, `ScoreBadge`, `FitRadar`, `BlockCard`.
- **Backend Functionality:** `gemini-eval.mjs`, `openrouter-runner.mjs`, `modes/oferta.md`.
- **API Endpoints:** `POST /api/pipeline`, `GET /api/pipeline/[id]`.
- **Implementation Status:** Fully implemented.

---

### Feature 3: Interactive CV Studio & ATS Keyword Optimizer
- **Purpose:** Displays the candidate's CV side-by-side with the JD, identifies missing ATS keywords, and rewrites bullets with anti-hallucination guardrails.
- **User Problem Solved:** Tailoring resumes manually is tedious and risks either keyword omission or accidental resume fabrication.
- **User Journey:** User opens `/pipeline/[id]/cv-studio`, reviews keyword gaps, clicks "Rewrite Bullet", views real-time diff, verifies against source facts, and exports PDF.
- **Frontend Components:** `CvStudioView`, `KeywordCoverageBar`, `BulletDiffViewer`, `ExportPdfButton`.
- **Backend Functionality:** `verify-cv-facts.mjs`, `keyword-coverage.mjs`, `generate-pdf.mjs`.
- **API Endpoints:** `GET /api/cv-studio/[n]`, `POST /api/cv-studio/[n]/rewrite`, `POST /api/cv-pdf`.
- **Implementation Status:** Fully implemented.

---

### Feature 4: Follow-up Cadence & Outreach Tracker
- **Purpose:** Automatically categorizes submitted applications by elapsed days and flags which applications require follow-ups.
- **User Problem Solved:** Job seekers lose momentum after submitting applications and miss optimal follow-up windows.
- **User Journey:** User visits `/followups`, sees roles grouped into *Urgent* (7-10 days no response), *Overdue* (>14 days), *Waiting* (<5 days), clicks "Generate Outreach Draft", and copies tailored follow-up copy.
- **Frontend Components:** `FollowupsView`, `CadenceBadge`, `OutreachDraftModal`.
- **Backend Functionality:** `followups-server.ts`, `data/status-log.tsv`.
- **API Endpoints:** `GET /api/followups`, `POST /api/followups/log`, `POST /api/followups/cadence`.
- **Implementation Status:** Fully implemented.

---

### Feature 5: Multi-Role Comparative Decision Matrix
- **Purpose:** Renders a side-by-side comparison table of 2–4 evaluated offers across Compensation, Match Score, Tech Fit, Remote Policy, and Risk.
- **User Problem Solved:** Choosing between multiple active offers or application priorities without spreadsheet clutter.
- **User Journey:** User selects 2+ jobs on `/pipeline` and clicks "Compare", landing on `/pipeline/compare`.
- **Frontend Components:** `CompareView`, `ComparisonMatrixTable`, `TradeoffCard`.
- **Backend Functionality:** `lib/pipeline-sort.mjs`, `pipeline-table.mjs`.
- **Implementation Status:** Fully implemented.

---

### Feature 6: Scheduled Background Scans & Alerts
- **Purpose:** Periodically executes portal scans on a recurring schedule and flags newly discovered matching roles.
- **User Problem Solved:** Continuous passive job discovery without manual intervention.
- **User Journey:** User configures a scan schedule (daily at 9:00 AM) on `/scheduled-scans`, background process triggers and records new entries.
- **Frontend Components:** `ScheduledScansView`, `NewScanModal`, `CronLogViewer`.
- **Backend Functionality:** `scheduled-jobs-store.mjs`, `scripts/scheduler.mjs`.
- **API Endpoints:** `GET /api/scheduled-jobs`, `POST /api/scheduled-jobs`.
- **Implementation Status:** Fully implemented.
