# SOURCE API INVENTORY — Complete Route Specification

**Base URL:** `http://127.0.0.1:3000/api`

---

| Method | Endpoint | Description | Request Payload | Response Schema | Integration Feasibility |
|---|---|---|---|---|---|
| `GET` | `/api/status` | System diagnostics & health check | None | `{ healthy: boolean, version: string, tools: [...] }` | High |
| `GET` | `/api/explore` | Fetches scraped jobs from inbox | `?age=24h&source=ashby` | `{ jobs: Array<JobItem>, total: number }` | High |
| `POST` | `/api/explore` | Triggers a live portal scan | `{ sources: ["ashby", "greenhouse"], mode: "fast" }` | `{ scan_id: string, new_jobs: number }` | High |
| `GET` | `/api/pipeline` | Returns all pipeline entries & stats | `?status=Applied&min_score=3.5` | `{ applications: [...], counts: {...} }` | High |
| `POST` | `/api/pipeline` | Evaluates a job posting from URL | `{ url: string, role?: string, company?: string }` | `{ report_id: string, score: number, report_markdown: string }` | High |
| `GET` | `/api/cv-studio/[n]` | Fetches CV analysis & keyword gaps for job #n | None | `{ candidate: {...}, job: {...}, missing_keywords: [...], bullets: [...] }` | High |
| `POST` | `/api/cv-studio/[n]/rewrite` | Rewrites a CV bullet for JD fit | `{ bullet_index: number, jd_context: string }` | `{ original: string, suggested: string, rationale: string, verified: boolean }` | High |
| `POST` | `/api/cv-pdf` | Compiles tailored HTML to PDF via Playwright | `{ html: string, format: "letter" \| "a4" }` | Binary PDF stream or `{ pdf_path: string }` | High |
| `GET` | `/api/followups` | Lists follow-up items with urgency tiers | None | `{ urgent: [...], overdue: [...], waiting: [...], cold: [...] }` | High |
| `POST` | `/api/followups/log` | Logs an outreach or employer reply | `{ application_id: string, note: string, action: string }` | `{ success: boolean, updated_at: string }` | High |
| `GET` | `/api/scheduled-jobs` | Returns cron jobs for background scanning | None | `{ jobs: Array<CronJob> }` | Medium |
| `POST` | `/api/scheduled-jobs` | Creates a new cron scan rule | `{ name: string, cron: string, sources: [...] }` | `{ job_id: string, status: "active" }` | Medium |
| `GET` | `/api/patterns` | Analyzes historical rejection/interview patterns | None | `{ pass_rate_by_score: {...}, best_sources: [...] }` | High |
| `POST` | `/api/linkedin-import` | Ingests job alert text or raw LinkedIn URLs | `{ raw_text: string }` | `{ parsed_urls: [...], added: number }` | High |
