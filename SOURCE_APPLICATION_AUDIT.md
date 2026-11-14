# SOURCE APPLICATION AUDIT — Career-Ops Web Engine (v1.40.0)

**Audit Date:** November 14, 2026  
**Auditor:** Principal Software Architect & QA Lead (FrontierPilot 2.0 Integration)  
**Source Target:** `http://127.0.0.1:3000` (`/Users/aryansharma/Desktop/career-ops/web`)  
**Destination Repository:** `linkedin-skills-main` (Branch: `frontierpilot-2.0`)

---

## 1. Executive Summary

The source application is the full-stack Next.js web application of `career-ops` (v1.40.0), a production-grade local job operations cockpit. It runs on Next.js 16.4.1 (React 19 / Turbopack), backed by Node.js ES modules, Playwright browser automation, SQLite/TSV/Markdown persistence, and LLM runner integrations.

The application serves as an autonomous pipeline for:
1. **Multi-portal automated job scanning** across Ashby, Greenhouse, Lever, Workable, and direct career sites.
2. **Structured Job Evaluation (A-H Report & 1-5 Scoring)** analyzing role clarity, tech alignment, visa/location constraints, compensation, and team signals.
3. **Interactive CV Studio & Bullet Tailoring** with anti-hallucination verification against `cv.md`.
4. **Application Follow-up Cadence & Outreach Tracker** classifying pending applications by urgency.
5. **Multi-Role Comparative Decision Matrix** evaluating trade-offs between offers.
6. **Scheduled Background Cron Watchers** discovering roles autonomously.

---

## 2. Navigation & Route Audit (Live Playwright Crawl)

| Route | Status | Title / Header | Key Interactive Components | Console / Network Status |
|---|---|---|---|---|
| `/` | `200 OK` | `career-ops — official web experience` | Quick triage input, stats counters, AI evaluation launcher, LinkedIn job import paste, command palette (`⌘K`), dark mode toggle | Clean, 0 network failures |
| `/pipeline` | `200 OK` | `career-ops — official web experience` | Inbox table (2,823 raw parsed jobs), filter chips, search input, status tabs (Inbox, All, Evaluated, Applied, Responded, Assessment), batch action bar | 1 React SSR hydration warning (handled gracefully) |
| `/pipeline/compare` | `200 OK` | `career-ops — official web experience` | Multi-role selector, side-by-side metric comparison (Fit Score, Comp, Remote, Sponsor, Superpower fit) | Clean, 0 errors |
| `/explore` | `200 OK` | `career-ops — official web experience` | Live portal scan trigger (Free/Zero-token vs AI search), age filter (24h, 3d, 7d, 14d, 30d), company tag filter, raw feed explorer | Clean, 0 errors |
| `/portals` | `200 OK` | `career-ops — official web experience` | Configured portal health checker, tracked companies list, ATS detection cards, toggle buttons | Clean, 0 errors |
| `/config` | `200 OK` | `career-ops — official web experience` | Candidate profile editor, target roles, comp floor, AI runner switcher, company logo fetcher toggle, save button | Clean, 0 errors |
| `/followups` | `200 OK` | `career-ops — official web experience` | Categorized cadence boards (All, Overdue, Urgent, Waiting, Cold), sortable company/role columns, log interaction button | Clean, 0 errors |
| `/scheduled-scans`| `200 OK` | `career-ops — official web experience` | Scheduled cron job manager, new scan modal, run history log viewer, pause/resume triggers | Clean, 0 errors |

---

## 3. Layout & Responsive Evaluation

- **Desktop (1440x900):** Spacious multi-column layouts, sticky sidebar navigation, collapsible facet filters, floating command palette (`⌘K`), high-density data tables with monospace metric chips.
- **Mobile (375x812 iPhone):** Responsive single-column collapse, scrollable horizontal status pills, bottom-drawer navigation, responsive touch-target buttons (>= 44px height).
- **Theme Support:** Native Dark & Light modes with CSS variables and custom typography (Instrument Serif + Inter Variable).

---

## 4. Technical Architecture of Source

- **Frontend:** Next.js 16 (App Router), React 19, Tailwind CSS, Lucide icons, `@paper-design/shaders-react`.
- **Backend / APIs:** Next.js Route Handlers (`src/app/api/*`) executing local Node.js child processes or importing core `.mjs` modules directly.
- **Persistence Layer:** SQLite (`applications.db`), TSV audit trails (`data/scan-history.tsv`, `data/status-log.tsv`), YAML configs (`config/profile.yml`, `portals.yml`), Markdown records (`cv.md`, `modes/_profile.md`, `data/pipeline.md`).
- **Automation Engine:** Playwright Chromium headless runner for page rendering, extraction, and PDF generation.
