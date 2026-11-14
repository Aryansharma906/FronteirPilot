import re
from pathlib import Path

ROOT = Path("/Users/aryansharma/Desktop/linkedin-skills-main")
TARGET_HTML = ROOT / "studio" / "templates" / "frontierpilot.html"
DOCS_HTML = ROOT / "docs" / "frontierpilot.html"

print("Reading", TARGET_HTML)
html = TARGET_HTML.read_text(encoding="utf-8")

# 1. ORIGINAL FIGMA EDITORIAL DESIGN SYSTEM CSS
EDITORIAL_CSS = """
    @font-face {
      font-family: 'Instrument Serif';
      src: url('/assets/fonts/instrument-serif/InstrumentSerif-Latin-Regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'Instrument Serif';
      src: url('/assets/fonts/instrument-serif/InstrumentSerif-Latin-Italic.woff2') format('woff2');
      font-weight: 400;
      font-style: italic;
      font-display: swap;
    }
    @font-face {
      font-family: 'Inter';
      src: url('/assets/fonts/inter/Inter-Latin-Variable.woff2') format('woff2');
      font-weight: 100 900;
      font-style: normal;
      font-display: swap;
    }

    :root, html.light {
      /* Warm Linen Paper & Editorial Palette */
      --bg: #f7f6f3;
      --bg-alt: #eae8e1;
      --surface: #ffffff;
      --surface-hover: #faf9f5;
      --surface-active: #f3f1ea;
      --surface-card: #ffffff;
      --surface-elevated: #ffffff;

      --border: rgba(0, 0, 0, 0.08);
      --border-light: rgba(0, 0, 0, 0.14);
      --border-glow: rgba(234, 88, 12, 0.25);

      --fg: #1c1917;
      --muted: #64748b;
      --faint: #94a3b8;
      --landing: #0f172a;

      /* Warm Terracotta Editorial Accent */
      --brand: hsl(26 73% 51%);
      --brand-text: #c2410c;
      --brand-soft: hsl(26 73% 51% / 0.10);
      --brand-foreground: #ffffff;

      --cyan-400: #0284c7;
      --cyan-500: #0369a1;
      --purple-400: #9333ea;
      --purple-500: #7e22ce;
      --emerald-400: #059669;
      --emerald-500: #047857;
      --amber-400: #d97706;
      --amber-500: #b45309;
      --rose-400: #e11d48;
      --rose-500: #be123c;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.06), 0 1px 2px rgba(0, 0, 0, 0.04);
      --shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.09);

      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-serif: 'Instrument Serif', Georgia, serif;
      --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    }

    html.dark {
      /* Sleek Obsidian & Slate Editorial */
      --bg: #0f172a;
      --bg-alt: #1e293b;
      --surface: #1e293b;
      --surface-hover: #334155;
      --surface-active: #3b4252;
      --surface-card: #1e293b;
      --surface-elevated: #242f47;

      --border: rgba(255, 255, 255, 0.08);
      --border-light: rgba(255, 255, 255, 0.15);
      --border-glow: rgba(251, 146, 60, 0.35);

      --fg: #f8fafc;
      --muted: #94a3b8;
      --faint: #64748b;
      --landing: #ffffff;

      --brand: hsl(26 73% 51%);
      --brand-text: #fb923c;
      --brand-soft: hsl(26 73% 51% / 0.18);
      --brand-foreground: #ffffff;

      --cyan-400: #38bdf8;
      --cyan-500: #0ea5e9;
      --purple-400: #c084fc;
      --purple-500: #a855f7;
      --emerald-400: #34d399;
      --emerald-500: #10b981;
      --amber-400: #fbbf24;
      --amber-500: #f59e0b;
      --rose-400: #fb7185;
      --rose-500: #f43f5e;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 6px 20px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 12px 36px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg);
      color: var(--fg);
      font-family: var(--font-sans);
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
      min-height: 100vh;
      transition: background-color 0.2s ease, color 0.2s ease;
    }

    .font-serif { font-family: var(--font-serif); }
    .font-serif-italic { font-family: var(--font-serif); font-style: italic; }
    .font-mono { font-family: var(--font-mono); }

    /* Layout Structure */
    .app-layout {
      display: flex;
      min-height: 100vh;
      position: relative;
    }

    /* Sidebar Navigation (Clean Editorial Rail) */
    .app-sidebar {
      width: 260px;
      flex-shrink: 0;
      background: var(--surface);
      border-right: 1px solid var(--border);
      position: sticky;
      top: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 24px 16px;
      overflow-y: auto;
      z-index: 50;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
    }

    .app-main {
      flex: 1;
      min-width: 0;
      padding: 24px 36px 60px 36px;
      max-width: 1440px;
      margin: 0 auto;
      box-sizing: border-box;
    }

    /* Brand Header in Sidebar */
    .brand-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 22px;
      text-decoration: none;
      color: inherit;
      padding: 0 4px;
    }
    .brand-mark-box {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      background: var(--brand);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-serif);
      font-size: 22px;
      font-style: italic;
      font-weight: 700;
      flex-shrink: 0;
      box-shadow: 0 2px 8px hsl(26 73% 51% / 0.35);
    }
    .brand-title-wrap {
      display: flex;
      flex-direction: column;
    }
    .brand-title {
      font-family: var(--font-serif);
      font-size: 21px;
      font-weight: 400;
      letter-spacing: -0.01em;
      color: var(--landing);
      line-height: 1.1;
    }
    .brand-subtitle {
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 0.02em;
      margin-top: 2px;
    }
    .brand-version-pill {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 600;
      color: var(--brand-text);
      background: var(--brand-soft);
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: auto;
    }

    /* Quick Find / Palette Trigger */
    .cmd-trigger {
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 12.5px;
      color: var(--muted);
      cursor: pointer;
      margin-bottom: 18px;
      transition: all 0.15s ease;
      width: 100%;
      text-align: left;
    }
    .cmd-trigger:hover {
      border-color: var(--brand);
      color: var(--fg);
      background: var(--surface-hover);
    }
    .cmd-key {
      margin-left: auto;
      font-family: var(--font-mono);
      font-size: 10px;
      background: var(--surface);
      border: 1px solid var(--border-light);
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--muted);
    }

    /* Navigation */
    .nav-category-label {
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--faint);
      margin: 14px 0 6px 8px;
    }
    .nav-list {
      display: flex;
      flex-direction: column;
      gap: 3px;
      list-style: none;
    }
    .nav-btn {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 500;
      color: var(--muted);
      background: transparent;
      border: 1px solid transparent;
      width: 100%;
      text-align: left;
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
    }
    .nav-btn:hover {
      background: var(--surface-hover);
      color: var(--fg);
    }
    .nav-btn.active {
      background: var(--brand-soft);
      color: var(--brand-text);
      font-weight: 600;
    }
    .nav-btn .icon {
      font-size: 15px;
      width: 18px;
      text-align: center;
    }
    .nav-btn .badge {
      margin-left: auto;
      font-size: 10px;
      font-weight: 600;
      padding: 2px 6px;
      border-radius: 10px;
    }

    /* Sidebar Footer Promo */
    .sidebar-footer-card {
      margin-top: auto;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      font-size: 12px;
    }
    .sidebar-footer-card h4 {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--landing);
      margin-bottom: 4px;
    }
    .sidebar-footer-card p {
      color: var(--muted);
      line-height: 1.4;
      margin-bottom: 8px;
      font-size: 11.5px;
    }

    /* ===================================================================
       REFINED HEADER UPPER RIBBON BAR
       =================================================================== */
    .header-ribbon-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
    }
    .ribbon-left {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }
    .ribbon-brand-badge {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ribbon-brand-title {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 600;
      color: var(--landing);
    }
    .ribbon-pill {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 16px;
      font-size: 11.5px;
      font-weight: 500;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--muted);
    }
    .ribbon-pill.live-health {
      color: var(--emerald-500);
      background: hsl(152 57% 53% / 0.10);
      border-color: hsl(152 57% 53% / 0.25);
    }
    .ribbon-pill.roles-count {
      color: var(--brand-text);
      background: var(--brand-soft);
      border-color: hsl(26 73% 51% / 0.25);
      font-weight: 600;
    }
    .pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: currentColor;
      box-shadow: 0 0 6px currentColor;
    }

    .ribbon-right {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .ribbon-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ribbon-profile-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 4px 12px 4px 4px;
      text-decoration: none;
      color: inherit;
      font-size: 12px;
      transition: all 0.15s ease;
    }
    .ribbon-profile-pill:hover {
      border-color: var(--brand);
      background: var(--surface-hover);
    }
    .ribbon-avatar {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--brand);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
    }

    /* Cards & Containers */
    .card, .glass-card {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 22px;
      box-shadow: var(--shadow-sm);
      transition: box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .card:hover, .glass-card:hover {
      box-shadow: var(--shadow-md);
      border-color: var(--border-light);
    }

    /* KPI Grid */
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .kpi-card {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .kpi-label {
      font-size: 12px;
      font-weight: 600;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .kpi-value {
      font-family: var(--font-serif);
      font-size: 34px;
      font-weight: 400;
      color: var(--landing);
      line-height: 1.1;
      margin: 10px 0 6px 0;
    }
    .kpi-subtext {
      font-size: 12px;
      color: var(--muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Grids & Tables */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
      gap: 16px;
      margin-top: 14px;
    }

    .table-container {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
      margin-top: 14px;
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }
    .data-table th {
      background: var(--bg);
      padding: 12px 16px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--muted);
      border-bottom: 1px solid var(--border);
      white-space: nowrap;
    }
    .data-table td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      color: var(--fg);
      vertical-align: middle;
    }
    .data-table tr:hover td {
      background: var(--surface-hover);
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
      border: 1px solid transparent;
      white-space: nowrap;
    }
    .btn-primary {
      background: var(--brand);
      color: #fff;
    }
    .btn-primary:hover {
      background: #c2410c;
    }
    .btn-outline {
      background: var(--surface);
      border-color: var(--border-light);
      color: var(--fg);
    }
    .btn-outline:hover {
      background: var(--surface-hover);
      border-color: var(--brand);
      color: var(--brand-text);
    }
    .btn-sm {
      padding: 5px 10px;
      font-size: 11.5px;
    }
    .btn-xs {
      padding: 3px 8px;
      font-size: 11px;
    }

    /* Chips & Badges */
    .chip {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 500;
      background: var(--bg);
      border: 1px solid var(--border);
      color: var(--muted);
    }
    .chip.brand {
      background: var(--brand-soft);
      border-color: hsl(26 73% 51% / 0.3);
      color: var(--brand-text);
    }
    .chip.green {
      background: hsl(152 57% 53% / 0.12);
      border-color: hsl(152 57% 53% / 0.25);
      color: var(--emerald-500);
    }
    .chip.purple {
      background: hsl(270 70% 60% / 0.12);
      border-color: hsl(270 70% 60% / 0.25);
      color: var(--purple-500);
    }
    .chip.cyan {
      background: hsl(199 89% 48% / 0.12);
      border-color: hsl(199 89% 48% / 0.25);
      color: var(--cyan-400);
    }

    .score-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 3px 8px;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      background: var(--brand-soft);
      color: var(--brand-text);
    }
    .score-badge.priority {
      background: #047857;
      color: #fff;
    }
    .score-badge.high {
      background: var(--brand);
      color: #fff;
    }

    /* Mobile Responsive */
    .mobile-header {
      display: none;
      padding: 12px 16px;
      background: var(--surface);
      border-bottom: 1px solid var(--border);
    }
    @media (max-width: 900px) {
      .mobile-header { display: flex; align-items: center; justify-content: space-between; }
      .app-sidebar {
        position: fixed;
        left: -300px;
        transition: left 0.3s ease;
      }
      .app-sidebar.mobile-open { left: 0; }
      .app-main { padding: 16px; }
      .header-ribbon-bar { display: none; }
    }
    @media (max-width: 480px) {
      .app-main { padding: 12px 6px; width: 100%; box-sizing: border-box; overflow-x: hidden; }
      .card-grid { grid-template-columns: 1fr; }
      .glass-card, .card { padding: 14px 10px; max-width: 100%; box-sizing: border-box; overflow-x: auto; }
      body, html { overflow-x: hidden; }
    }

    /* Toast Notification */
    .toast-note {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--landing);
      color: #ffffff;
      padding: 12px 18px;
      border-radius: 8px;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 9999;
      opacity: 0;
      pointer-events: none;
      transform: translateY(12px);
      transition: all 0.25s ease;
      box-shadow: var(--shadow-lg);
    }
    .toast-note.show {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }

    /* Modal / Command Palette */
    .cmd-modal {
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(4px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 9000;
    }
    .cmd-modal.open { display: flex; }
    .cmd-box {
      width: 580px;
      max-width: 90%;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      box-shadow: var(--shadow-lg);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .cmd-input {
      width: 100%;
      padding: 10px 14px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: var(--bg);
      color: var(--fg);
      font-size: 14px;
      outline: none;
    }
    .cmd-input:focus {
      border-color: var(--brand);
    }
"""

# Replace <style> block
html = re.sub(r'<style>[\s\S]*?</style>', f'<style>{EDITORIAL_CSS}</style>', html, count=1)

# 2. CLEAN EDITORIAL SIDEBAR
REFINED_SIDEBAR = """<aside class="app-sidebar" id="appSidebar">
    <a href="./frontierpilot.html" class="brand-header">
      <div class="brand-mark-box">FP</div>
      <div class="brand-title-wrap">
        <span class="brand-title">FrontierPilot</span>
        <span class="brand-subtitle">Autonomous Career Studio</span>
      </div>
      <span class="brand-version-pill">v2.0</span>
    </a>

    <button class="cmd-trigger" onclick="openCmdPalette()">
      <span>🔍</span>
      <span>Quick Actions & Jump...</span>
      <span class="cmd-key">⌘F</span>
    </button>

    <div class="nav-category-label">Career Radar</div>
    <ul class="nav-list">
      <li>
        <button class="nav-btn active" data-tab="today" onclick="switchTab('today')">
          <span class="icon">☀️</span>
          <span>Today Cockpit</span>
          <span class="badge" id="todayNavBadge" style="background:var(--brand-soft); color:var(--brand-text);">Live</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="pipeline" onclick="switchTab('pipeline')">
          <span class="icon">💼</span>
          <span>Pipeline Triage</span>
          <span class="badge" style="background:var(--bg); border:1px solid var(--border); color:var(--muted);">107</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="explore" onclick="switchTab('explore')">
          <span class="icon">🌐</span>
          <span>Explore Portals</span>
          <span class="badge" style="background:hsl(152 57% 53% / 0.12); color:var(--emerald-500);">104 New</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="compare" onclick="switchTab('compare')">
          <span class="icon">⚖️</span>
          <span>Compare Matrix</span>
        </button>
      </li>
    </ul>

    <div class="nav-category-label">Creator & AI Engines</div>
    <ul class="nav-list">
      <li>
        <button class="nav-btn" data-tab="linkedin" onclick="switchTab('linkedin')">
          <span class="icon">🚀</span>
          <span>LinkedIn Studio</span>
          <span class="badge" style="background:hsl(270 70% 60% / 0.12); color:var(--purple-500);">85 Drafts</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="cvstudio" onclick="switchTab('cvstudio')">
          <span class="icon">📄</span>
          <span>CV Studio (X-Y-Z)</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="intelligence" onclick="switchTab('intelligence')">
          <span class="icon">🧠</span>
          <span>Autonomous Radar</span>
        </button>
      </li>
    </ul>

    <div class="nav-category-label">Integrations & Sync</div>
    <ul class="nav-list">
      <li>
        <button class="nav-btn" data-tab="portals" onclick="switchTab('portals')">
          <span class="icon">📡</span>
          <span>Portals & ATS Health</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="wix" onclick="switchTab('wix')">
          <span class="icon">🎨</span>
          <span>Wix CMS Portfolio</span>
        </button>
      </li>
      <li>
        <button class="nav-btn" data-tab="followups" onclick="switchTab('followups')">
          <span class="icon">⏱️</span>
          <span>Follow-up Cadence</span>
        </button>
      </li>
    </ul>

    <div class="sidebar-footer-card">
      <h4>Notion & Cloud Active</h4>
      <p>Two-way synchronization active with Aryan Sharma's Notion Space & Google Drive.</p>
      <button class="btn btn-outline btn-xs" onclick="triggerCrossPlatformSync('all')">⚡ Sync Now</button>
    </div>
  </aside>"""

html = re.sub(r'<aside class="app-sidebar" id="appSidebar">[\s\S]*?</aside>', REFINED_SIDEBAR, html, count=1)

# 3. REFINED UPPER RIBBON BAR
REFINED_RIBBON = """<div class="header-ribbon-bar">
        <div class="ribbon-left">
          <div class="ribbon-brand-badge">
            <span class="ribbon-brand-title">FrontierPilot 2.0</span>
            <span class="chip brand">Studio Edition</span>
          </div>
          <div class="ribbon-pill live-health">
            <span class="pulse-dot"></span>
            <span>Live System Health</span>
          </div>
          <div class="ribbon-pill roles-count">
            <span>107 Monitored Roles</span>
          </div>
          <div class="ribbon-pill">
            <span>📑 Notion & Drive Synced</span>
          </div>
        </div>

        <div class="ribbon-right">
          <button class="cmd-trigger" style="margin-bottom:0; width:auto; padding:6px 12px;" onclick="openCmdPalette()">
            <span>🔍 ⌘F</span>
          </button>
          
          <div class="ribbon-actions">
            <button class="btn btn-primary btn-sm" onclick="openNewLinkedinPostModal()">✨ New Post</button>
            <button class="btn btn-outline btn-sm" onclick="triggerCrossPlatformSync('all')">⚡ Sync All</button>
            <button class="btn btn-outline btn-sm" onclick="exportPipelineCsv()">📥 Export CSV</button>
          </div>

          <a href="https://github.com/Aryansharma906" target="_blank" class="ribbon-profile-pill">
            <div class="ribbon-avatar">AS</div>
            <div>
              <strong>Aryan Sharma</strong>
              <div style="font-size:10.5px; color:var(--muted);">AI & Security Researcher</div>
            </div>
          </a>
        </div>
      </div>"""

# Replace existing executive top bar or insert refined ribbon
if '<div class="executive-top-bar">' in html:
    html = re.sub(r'<div class="executive-top-bar">[\s\S]*?</div>\s*<!-- ROW 1:', REFINED_RIBBON + '\n\n        <!-- ROW 1:', html, count=1)
elif '<div class="header-ribbon-bar">' in html:
    html = re.sub(r'<div class="header-ribbon-bar">[\s\S]*?</div>\s*<!-- ROW 1:', REFINED_RIBBON + '\n\n        <!-- ROW 1:', html, count=1)

# 4. REFINED TODAY DASHBOARD COCKPIT (Clean, Readable, Editorial)
REFINED_TODAY_VIEW = """<section id="view-today" class="view-panel">
        """ + REFINED_RIBBON + """

        <!-- ROW 1: EXECUTIVE KPI SUMMARY -->
        <div class="kpi-row">
          <div class="kpi-card">
            <div class="kpi-label">
              <span>🎯 Global Growth Score</span>
              <span class="chip green">High Fit</span>
            </div>
            <div class="kpi-value" style="color:var(--emerald-500);">94%</div>
            <div class="kpi-subtext">
              <span>Verified qualification alignment across 107 opportunities</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-label">
              <span>💎 Target Compensation</span>
              <span class="chip brand">Top Tier</span>
            </div>
            <div class="kpi-value">$185,000<span style="font-size:16px; color:var(--muted);">/yr</span></div>
            <div class="kpi-subtext">
              <span style="color:var(--emerald-500); font-weight:600;">+14.8%</span>
              <span>vs frontier market baseline</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-label">
              <span>⚡ Conversion Velocity</span>
              <span class="chip cyan">Active</span>
            </div>
            <div class="kpi-value">24.2%</div>
            <div class="kpi-subtext">
              <span>107 active tracked · 27 in stage review · 4 interviewing</span>
            </div>
          </div>

          <div class="kpi-card">
            <div class="kpi-label">
              <span>📑 Cross-Platform Sync</span>
              <span class="chip green">● Synced</span>
            </div>
            <div class="kpi-value" style="font-size:24px; margin:16px 0 10px 0;">Notion & Workspace</div>
            <div class="kpi-subtext">
              <span>Dossier Radar (Aryan Sharma's Space)</span>
            </div>
          </div>
        </div>

        <!-- ROW 2: #1 PRIORITY TARGET HERO BANNER -->
        <div class="card" id="applyNextCard" style="background:var(--surface-card); border-left:4px solid var(--brand); margin-bottom:24px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; flex-wrap:wrap; gap:10px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span class="chip brand" style="font-weight:600;">Apply Next · #1 Priority Target</span>
              <span class="score-badge priority">100 Match</span>
            </div>
            <div style="display:flex; gap:8px;">
              <button class="btn btn-outline btn-sm" onclick="switchTab('cvstudio')">📄 Tailor Resume</button>
              <button class="btn btn-primary btn-sm" onclick="dispatchSlackApprovalAll()">📢 Send to Slack</button>
            </div>
          </div>
          
          <div style="display:flex; gap:16px; align-items:flex-start; margin-top:12px; flex-wrap:wrap;">
            <div style="width:44px; height:44px; border-radius:8px; background:var(--brand-soft); color:var(--brand-text); display:flex; align-items:center; justify-content:center; font-size:18px; font-weight:700;">HS</div>
            <div style="flex:1;">
              <h3 style="font-family:var(--font-serif); font-size:22px; font-weight:400; color:var(--landing);" id="applyNextTitle">AI Evaluation Specialist (LLM Reasoning & Safety)</h3>
              <div style="font-size:13.5px; color:var(--muted); margin-top:2px;" id="applyNextOrg">Handshake (San Francisco) · Remote Worldwide · $25 – $45/hr</div>
              <p style="font-size:13.5px; color:var(--fg); margin-top:10px; line-height:1.5;" id="applyNextReason">
                Direct validation of your published prompt vulnerability research. Active contract evaluating multi-turn reasoning and adversarial boundaries.
              </p>
            </div>
          </div>
        </div>

        <!-- ROW 3: TWO COLUMN SUMMARY (Awaiting Decision Cards + Live Sync Connections) -->
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap:20px; margin-bottom:28px;">
          
          <!-- Column 1: Awaiting Your Decision -->
          <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
              <div>
                <h3 style="font-size:16px; font-weight:600; color:var(--landing);">❓ Awaiting Immediate Decision</h3>
                <div style="font-size:12px; color:var(--muted);">Top roles ranked by verified match score</div>
              </div>
              <button class="btn btn-outline btn-xs" onclick="switchTab('pipeline')">View All (107) ↗</button>
            </div>

            <div class="card-grid" id="decisionCardsGrid" style="grid-template-columns:1fr; gap:12px; margin-top:0;"></div>
          </div>

          <!-- Column 2: Live Platform & MCP Connections -->
          <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
              <div>
                <h3 style="font-size:16px; font-weight:600; color:var(--landing);">🔌 Platform & MCP Connections</h3>
                <div style="font-size:12px; color:var(--muted);">Active cloud bridges & database sync</div>
              </div>
              <button class="btn btn-primary btn-xs" onclick="triggerCrossPlatformSync('all')">⚡ Sync All</button>
            </div>

            <table class="data-table" style="font-size:12.5px;">
              <tbody>
                <tr>
                  <td>
                    <strong>📑 Notion Database (MCP)</strong>
                    <div style="font-size:11px; color:var(--muted);">Aryan Sharma's Space · Dossier Radar</div>
                  </td>
                  <td><span class="chip green">● Live Synced</span></td>
                  <td style="text-align:right;">
                    <button class="btn btn-outline btn-xs" onclick="triggerCrossPlatformSync('notion')">Sync</button>
                  </td>
                </tr>
                <tr>
                  <td>
                    <strong>📊 Google Workspace</strong>
                    <div style="font-size:11px; color:var(--muted);">aryanaryan.9956@gmail.com · Drive & Sheets</div>
                  </td>
                  <td><span class="chip green">● Connected</span></td>
                  <td style="text-align:right;">
                    <button class="btn btn-outline btn-xs" onclick="triggerCrossPlatformSync('sheets')">Export</button>
                  </td>
                </tr>
                <tr>
                  <td>
                    <strong>🌐 Wix Studio & CMS</strong>
                    <div style="font-size:11px; color:var(--muted);">Headless Portfolio Collection</div>
                  </td>
                  <td><span class="chip green">● Connected</span></td>
                  <td style="text-align:right;">
                    <button class="btn btn-outline btn-xs" onclick="triggerCrossPlatformSync('wix')">Sync</button>
                  </td>
                </tr>
                <tr>
                  <td>
                    <strong>📢 Slack Approver</strong>
                    <div style="font-size:11px; color:var(--muted);">1-Tap Mobile Review & Webhook</div>
                  </td>
                  <td><span class="chip green">● Active</span></td>
                  <td style="text-align:right;">
                    <button class="btn btn-outline btn-xs" onclick="dispatchSlackApprovalAll()">Digest</button>
                  </td>
                </tr>
                <tr>
                  <td>
                    <strong>🎯 ATS Harvester</strong>
                    <div style="font-size:11px; color:var(--muted);">Ashby, Greenhouse, Lever, Workday</div>
                  </td>
                  <td><span class="chip cyan">104 Ingested</span></td>
                  <td style="text-align:right;">
                    <button class="btn btn-outline btn-xs" onclick="switchTab('explore')">Explore</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

        </div>
      </section>"""

# Replace Today view
html = re.sub(r'<section id="view-today" class="view-panel">[\s\S]*?</section>', REFINED_TODAY_VIEW, html, count=1)

# 5. OVERHAUL LINKEDIN CREATOR STUDIO (Fixing all draft operations & modal generation!)
REFINED_LINKEDIN_VIEW = """<section id="view-linkedin" class="view-panel" style="display:none;">
        <div class="section-title-wrap" style="margin-top:0;">
          <span class="section-icon">🚀</span>
          <h1 style="font-family:var(--font-serif); font-size:32px; font-style:italic; color:var(--landing);">LinkedIn Autonomous Creator Studio</h1>
        </div>
        <p style="font-size:14px; color:var(--muted); margin-bottom:20px;">
          85 authentic founder post drafts, Google Gemini AI generation engine, and 1-tap Slack approval dispatch.
        </p>

        <!-- Action Strip & Generation Bar -->
        <div style="display:flex; justify-content:space-between; align-items:center; gap:12px; margin-bottom:20px; flex-wrap:wrap;">
          <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
            <button class="btn btn-primary" onclick="openNewLinkedinPostModal()">✨ Generate Gemini Founder Draft</button>
            <button class="btn btn-outline" onclick="dispatchSlackApprovalAll()">📢 Send Approval Digest to Slack</button>
          </div>
          
          <div style="display:flex; gap:8px; align-items:center;">
            <input type="text" id="linkedinSearchInput" class="search-input" placeholder="Search 85 drafts..." oninput="filterLinkedinDrafts()" style="padding:6px 12px; font-size:12.5px; width:220px;">
            <select id="linkedinFilterStatus" class="search-input" onchange="filterLinkedinDrafts()" style="padding:6px 10px; font-size:12.5px;">
              <option value="all">All Drafts</option>
              <option value="pending_approval">Pending Approval</option>
              <option value="approved">Approved</option>
              <option value="published">Published</option>
            </select>
          </div>
        </div>

        <!-- Drafts Grid -->
        <div class="card-grid" id="linkedinDraftsGrid"></div>

        <!-- Modal for Creating / Generating New Post -->
        <div class="cmd-modal" id="linkedinGenModal">
          <div class="cmd-box" style="width:640px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border); padding-bottom:12px;">
              <h3 style="font-family:var(--font-serif); font-size:22px; color:var(--landing);">Generate Founder Post with Gemini</h3>
              <button class="btn btn-outline btn-xs" onclick="closeNewLinkedinPostModal()">✕</button>
            </div>
            
            <div style="display:flex; flex-direction:column; gap:14px; margin-top:10px;">
              <div>
                <label style="font-size:12px; font-weight:600; color:var(--muted); display:block; margin-bottom:4px;">Topic / Strategic Angle</label>
                <input type="text" id="genPostTopic" class="cmd-input" placeholder="e.g. Why small AI teams beat 50-person agencies in 2026" value="Why small AI teams beat 50-person agencies in 2026">
              </div>

              <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                <div>
                  <label style="font-size:12px; font-weight:600; color:var(--muted); display:block; margin-bottom:4px;">Storytelling Style</label>
                  <select id="genPostStyle" class="cmd-input" style="padding:8px 10px;">
                    <option value="Founder Systems Perspective">Founder Systems Perspective</option>
                    <option value="Contrarian Technical Breakdown">Contrarian Technical Breakdown</option>
                    <option value="AI Safety & Evaluation Playbook">AI Safety & Evaluation Playbook</option>
                  </select>
                </div>
                <div>
                  <label style="font-size:12px; font-weight:600; color:var(--muted); display:block; margin-bottom:4px;">Hook Formula</label>
                  <select id="genPostHook" class="cmd-input" style="padding:8px 10px;">
                    <option value="Formula #1: Contrarian Take">Formula #1: Contrarian Take</option>
                    <option value="Formula #2: Specific Numbers / Benchmark">Formula #2: Specific Numbers / Benchmark</option>
                    <option value="Formula #3: Hard Truth / Unpopular Opinion">Formula #3: Hard Truth / Unpopular Opinion</option>
                  </select>
                </div>
              </div>

              <div>
                <label style="font-size:12px; font-weight:600; color:var(--muted); display:block; margin-bottom:4px;">Custom Prompt Instructions (Optional)</label>
                <textarea id="genPostInstructions" class="cmd-input" rows="3" placeholder="Include references to adversarial robustness, CS50x discipline, or Handshake benchmark findings."></textarea>
              </div>

              <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:8px;">
                <button class="btn btn-outline" onclick="closeNewLinkedinPostModal()">Cancel</button>
                <button class="btn btn-primary" onclick="submitGenerateLinkedinPost()">✨ Generate & Stage Draft</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Modal for Full Post Editing & Preview -->
        <div class="cmd-modal" id="linkedinEditModal">
          <div class="cmd-box" style="width:720px;">
            <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border); padding-bottom:12px;">
              <h3 style="font-family:var(--font-serif); font-size:22px; color:var(--landing);" id="editModalDraftTitle">Draft Preview & Editor</h3>
              <button class="btn btn-outline btn-xs" onclick="closeEditDraftModal()">✕</button>
            </div>
            
            <div style="display:flex; flex-direction:column; gap:14px; margin-top:10px;">
              <input type="hidden" id="editModalDraftId">
              <textarea id="editModalContent" class="cmd-input" rows="12" style="font-family:var(--font-sans); line-height:1.6; font-size:14px;"></textarea>
              
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span id="editModalStats" style="font-size:12px; color:var(--muted);">Char count: 0</span>
                <div style="display:flex; gap:8px;">
                  <button class="btn btn-outline btn-sm" onclick="saveEditedDraft()">💾 Save Changes</button>
                  <button class="btn btn-primary btn-sm" onclick="approveAndDispatchDraft()">📢 Approve & Send Slack</button>
                </div>
              </div>
            </div>
          </div>
        </div>

      </section>"""

html = re.sub(r'<section id="view-linkedin" class="view-panel" style="display:none;">[\s\S]*?</section>', REFINED_LINKEDIN_VIEW, html, count=1)

# Write out the updated file
TARGET_HTML.write_text(html, encoding="utf-8")
DOCS_HTML.write_text(html, encoding="utf-8")
print(f"✓ Saved updated HTML to {TARGET_HTML} ({len(html)} bytes)")
