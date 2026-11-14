# SOURCE ARCHITECTURE MAP — Career-Ops Web Engine

```mermaid
flowchart TD
    subgraph Client [Browser Client: http://127.0.0.1:3000]
        UI[Next.js 16 App Router UI]
        CP[Command Palette ⌘K]
        EV[Explore / Live Feed]
        PL[Pipeline Kanban & Table]
        CS[Interactive CV Studio]
        FU[Follow-up Cadence]
        SC[Scheduled Scans]
    end

    subgraph WebServer [Next.js Server / API Routes: src/app/api/*]
        API_Explore[/api/explore]
        API_Pipeline[/api/pipeline]
        API_CV[/api/cv-studio]
        API_PDF[/api/cv-pdf]
        API_Followups[/api/followups]
        API_Cron[/api/scheduled-jobs]
        API_Status[/api/status]
    end

    subgraph CoreEngine [Local CLI & Worker Modules]
        Scanner[scan.mjs / scan-ats-full.mjs]
        Evaluator[gemini-eval.mjs / modes/oferta.md]
        CV_Engine[verify-cv-facts.mjs / keyword-coverage.mjs]
        PDF_Gen[generate-pdf.mjs / Playwright Chromium]
        Followup_Logic[followups-server.ts]
    end

    subgraph DataLayer [Local Persistence]
        ProfileYAML[config/profile.yml]
        PortalsYAML[portals.yml]
        CVMD[cv.md]
        ModesMD[modes/_profile.md / _brief.md]
        AppDB[(SQLite applications.db)]
        HistoryTSV[data/scan-history.tsv]
        StatusLogTSV[data/status-log.tsv]
    end

    UI --> API_Explore & API_Pipeline & API_CV & API_PDF & API_Followups & API_Cron
    API_Explore --> Scanner
    API_Pipeline --> Evaluator
    API_CV --> CV_Engine
    API_PDF --> PDF_Gen
    API_Followups --> Followup_Logic
    
    Scanner --> PortalsYAML & HistoryTSV & AppDB
    Evaluator --> ProfileYAML & CVMD & ModesMD & AppDB
    CV_Engine --> CVMD
    Followup_Logic --> StatusLogTSV & AppDB
```

---

## Architectural Characteristics

1. **Local-First & Zero Cloud Lock-In:** All operational data lives in local SQLite, TSV, YAML, and Markdown files.
2. **Deterministic Evaluation:** Prompt engineering with strict A-H schemas and anti-hallucination checks against `cv.md`.
3. **Headless Engine Hybridization:** Lightweight HTTP/REST API calls for public ATS boards (Greenhouse, Ashby, Lever), falling back to Playwright Chromium headless browsing only when JavaScript SPAs require DOM rendering.
4. **Token Economy Discipline:** Free/Zero-token parsing for scraping, reservation of LLM calls strictly for structured evaluations and tailoring rewrites.
