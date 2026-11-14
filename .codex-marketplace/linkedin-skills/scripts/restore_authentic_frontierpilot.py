import re
from pathlib import Path

ROOT = Path("/Users/aryansharma/Desktop/linkedin-skills-main")
TARGET_HTML = ROOT / "studio" / "templates" / "frontierpilot.html"
DOCS_HTML = ROOT / "docs" / "frontierpilot.html"

print("Reading", TARGET_HTML)
content = TARGET_HTML.read_text(encoding="utf-8")

# 1. Update CSS tokens and rules to authentic Editorial style
# Replace style section with clean, robust, authentic Editorial CSS
CSS_REPLACEMENT = """<style>
    /* Local font declarations */
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
      --bg: #f7f6f3;
      --surface: #ffffff;
      --surface-hover: #efeeea;
      --surface-active: #f3f1ea;
      --surface-card: #ffffff;
      --surface-elevated: #ffffff;

      --border: hsl(40 9% 86%);
      --border-light: rgba(0, 0, 0, 0.12);
      --border-glow: rgba(234, 88, 12, 0.25);

      --fg: hsl(30 10% 11%);
      --muted: hsl(35 9% 34%);
      --faint: hsl(35 7% 42%);
      --landing: #59592a;

      /* Warm Terracotta Editorial Accent */
      --brand: hsl(26 73% 51%);
      --brand-text: hsl(26 80% 36%);
      --brand-soft: hsl(26 73% 51% / 0.12);
      --brand-foreground: hsl(24 30% 12%);

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

      --dot: 40 8% 42% / 0.09;
      --pre-bg: #f2f1ed;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);

      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-serif: 'Instrument Serif', Georgia, serif;
      --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    }

    html.dark {
      --bg: #0a0a0a;
      --surface: #161616;
      --surface-hover: #232323;
      --surface-active: #2a2a2a;
      --surface-card: #161616;
      --surface-elevated: #202020;

      --border: #262626;
      --border-light: rgba(255, 255, 255, 0.12);
      --border-glow: rgba(234, 88, 12, 0.35);

      --fg: #fafafa;
      --muted: #a1a1aa;
      --faint: #8b8b95;
      --landing: #e4e2d0;

      --brand: hsl(26 73% 51%);
      --brand-text: hsl(26 73% 51%);
      --brand-soft: hsl(26 73% 51% / 0.15);
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

      --dot: 240 5% 65% / 0.10;
      --pre-bg: #111111;
      --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.5), 0 2px 4px -2px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.6), 0 4px 6px -4px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg);
      color: var(--fg);
      font-family: var(--font-sans);
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
      min-height: 100vh;
      background-image: radial-gradient(circle, hsl(var(--dot)) 1px, transparent 1px);
      background-size: 24px 24px;
      overflow-x: hidden;
    }

    .font-serif { font-family: var(--font-serif); }
    .font-serif-italic { font-family: var(--font-serif); font-style: italic; }
    .font-mono { font-family: var(--font-mono); }

    /* Layout */
    .app-layout {
      display: flex;
      min-height: 100vh;
    }

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
      padding: 20px 16px;
      overflow-y: auto;
      z-index: 100;
    }

    .app-main {
      flex: 1;
      padding: 24px 32px;
      max-width: 1440px;
      margin: 0 auto;
      width: calc(100% - 260px);
      min-width: 0;
    }

    /* Brand Header in Sidebar */
    .brand-header {
      display: flex;
      align-items: center;
      gap: 12px;
      padding-bottom: 16px;
      margin-bottom: 16px;
      border-bottom: 1px solid var(--border);
      text-decoration: none;
      color: inherit;
    }
    .brand-mark {
      width: 34px;
      height: 34px;
      background: var(--brand);
      color: #fff;
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: 18px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 6px rgba(234, 88, 12, 0.3);
    }
    .brand-title {
      font-family: var(--font-serif);
      font-size: 21px;
      font-weight: 600;
      color: var(--landing);
      line-height: 1.1;
      letter-spacing: -0.01em;
    }
    .brand-version {
      margin-left: auto;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--surface-hover);
      color: var(--faint);
      border: 1px solid var(--border);
    }

    /* Command Trigger Button */
    .cmd-trigger {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      padding: 8px 12px;
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      font-size: 12.5px;
      color: var(--muted);
      cursor: pointer;
      margin-bottom: 20px;
      transition: all 0.15s ease;
    }
    .cmd-trigger:hover {
      background: var(--surface);
      border-color: var(--brand);
      color: var(--fg);
    }
    .cmd-key {
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 5px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 4px;
      color: var(--faint);
    }

    /* Navigation Lists */
    .nav-category {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--faint);
      margin: 16px 8px 6px 8px;
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
      gap: 12px;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 450;
      color: var(--muted);
      background: transparent;
      border: none;
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
      font-size: 16px;
      width: 18px;
      text-align: center;
      display: inline-block;
    }
    .nav-btn .badge {
      margin-left: auto;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 7px;
      border-radius: 10px;
      background: var(--surface-hover);
      color: var(--faint);
      border: 1px solid var(--border);
    }
    .nav-btn.active .badge {
      background: var(--brand);
      color: #fff;
      border-color: transparent;
    }

    /* Sidebar Footer */
    .sidebar-footer {
      margin-top: auto;
      padding-top: 16px;
      border-top: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .sidebar-footer-card {
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      font-size: 12px;
    }
    .sidebar-footer-card h4 {
      font-size: 12px;
      font-weight: 600;
      color: var(--fg);
      margin-bottom: 4px;
    }
    .sidebar-footer-card p {
      font-size: 11px;
      color: var(--muted);
      line-height: 1.4;
      margin-bottom: 8px;
    }

    /* Executive Upper Ribbon Bar */
    .executive-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 18px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
      flex-wrap: wrap;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .top-bar-right {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-left: auto;
    }
    .ribbon-brand-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      padding-right: 12px;
      border-right: 1px solid var(--border);
    }
    .ribbon-brand-title {
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 600;
      color: var(--landing);
      letter-spacing: -0.01em;
    }
    .live-status-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 500;
      border: 1px solid var(--border);
      background: var(--surface-hover);
      color: var(--muted);
      white-space: nowrap;
    }
    .live-status-pill.health {
      border-color: rgba(16, 185, 129, 0.25);
      color: var(--emerald-500);
      background: rgba(16, 185, 129, 0.08);
    }
    .live-status-pill.roles {
      border-color: rgba(234, 88, 12, 0.25);
      color: var(--brand-text);
      background: var(--brand-soft);
    }
    .pulse-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #10b981;
      display: inline-block;
      animation: pulseAnim 2s infinite;
    }
    .pulse-dot.emerald { background: #10b981; box-shadow: 0 0 6px #10b981; }
    .pulse-dot.cyan { background: #0ea5e9; box-shadow: 0 0 6px #0ea5e9; }
    .pulse-dot.brand { background: var(--brand); box-shadow: 0 0 6px var(--brand); }
    @keyframes pulseAnim {
      0% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
      100% { opacity: 1; transform: scale(1); }
    }
    .top-search-box {
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--surface-hover);
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 12px;
      color: var(--muted);
      min-width: 210px;
      transition: all 0.15s ease;
    }
    .top-search-box:hover {
      border-color: var(--brand);
      background: var(--surface);
      color: var(--fg);
    }
    .top-action-group {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .user-profile-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 4px 10px 4px 4px;
      border-radius: 24px;
      background: var(--surface-hover);
      border: 1px solid var(--border);
      color: var(--fg);
      text-decoration: none;
      transition: all 0.15s ease;
    }
    .user-profile-badge:hover {
      background: var(--surface);
      border-color: var(--brand);
    }
    .user-avatar {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--brand);
      color: #fff;
      font-size: 10.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .user-info-text {
      display: flex;
      flex-direction: column;
      line-height: 1.15;
    }
    .user-name {
      font-size: 11.5px;
      font-weight: 600;
      color: var(--fg);
    }
    .user-role {
      font-size: 9.5px;
      color: var(--muted);
    }

    /* Hero Banner */
    .hero-banner {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 28px 32px;
      box-shadow: var(--shadow-sm);
      margin-bottom: 28px;
      position: relative;
      overflow: hidden;
    }
    .hero-banner::after {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 240px;
      height: 100%;
      background: radial-gradient(circle at top right, var(--brand-soft), transparent 70%);
      pointer-events: none;
    }
    .hero-date {
      font-family: var(--font-mono);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--brand-text);
      font-weight: 600;
      margin-bottom: 6px;
    }
    .hero-heading {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: 38px;
      color: var(--landing);
      line-height: 1.1;
      margin-bottom: 8px;
      letter-spacing: -0.01em;
    }
    .hero-sub {
      font-size: 14.5px;
      color: var(--muted);
      max-width: 680px;
      line-height: 1.5;
    }
    .hero-stats-row {
      display: flex;
      gap: 28px;
      margin-top: 20px;
      padding-top: 18px;
      border-top: 1px solid var(--border);
      flex-wrap: wrap;
    }
    .hero-stat-item {
      display: flex;
      flex-direction: column;
    }
    .hero-stat-val {
      font-family: var(--font-serif);
      font-size: 26px;
      font-weight: 600;
      color: var(--fg);
      line-height: 1.1;
    }
    .hero-stat-label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--faint);
      margin-top: 2px;
    }

    /* Apply Next Hero Target */
    .apply-next-hero {
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 4px solid var(--brand);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }
    .apply-next-tag {
      display: inline-block;
      font-size: 10.5px;
      font-family: var(--font-mono);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--brand-text);
      background: var(--brand-soft);
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 600;
    }

    /* Card Grids & Items */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 18px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.15s ease;
    }
    .card:hover {
      box-shadow: var(--shadow-md);
      border-color: var(--border-light);
    }
    .card-top {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }
    .company-monogram {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      background: var(--brand-soft);
      color: var(--brand-text);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      font-weight: 700;
      flex-shrink: 0;
      border: 1px solid hsl(26 73% 51% / 0.25);
    }
    .card-meta {
      flex: 1;
      min-width: 0;
    }
    .card-company {
      font-size: 12px;
      color: var(--muted);
      font-weight: 500;
    }
    .card-role {
      font-size: 14px;
      font-weight: 600;
      color: var(--fg);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .card-desc {
      font-size: 12.5px;
      color: var(--muted);
      line-height: 1.45;
      margin-bottom: 12px;
    }
    .card-actions {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 14px;
      padding-top: 12px;
      border-top: 1px solid var(--border);
    }
    .score-badge {
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      font-family: var(--font-mono);
      white-space: nowrap;
    }
    .score-badge.priority {
      background: hsl(152 57% 53% / 0.15);
      color: var(--emerald-500);
      border: 1px solid hsl(152 57% 53% / 0.3);
    }
    .score-badge.strong {
      background: hsl(26 73% 51% / 0.15);
      color: var(--brand-text);
      border: 1px solid hsl(26 73% 51% / 0.3);
    }
    .chip-row {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 8px;
    }
    .chip {
      display: inline-flex;
      align-items: center;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 11px;
      background: var(--surface-hover);
      color: var(--muted);
      border: 1px solid var(--border);
    }
    .chip.brand {
      background: var(--brand-soft);
      color: var(--brand-text);
      border-color: transparent;
    }
    .chip.green {
      background: rgba(16, 185, 129, 0.1);
      color: #047857;
      border-color: rgba(16, 185, 129, 0.2);
    }
    .chip.font-mono {
      font-family: var(--font-mono);
    }
    .section-title-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
      margin: 28px 0 14px 0;
    }
    .section-icon {
      font-size: 16px;
    }
    .section-heading {
      font-size: 17px;
      font-weight: 600;
      color: var(--landing);
    }
    .section-hint {
      font-size: 12px;
      color: var(--muted);
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      text-decoration: none;
      border: 1px solid transparent;
      white-space: nowrap;
    }
    .btn-primary {
      background: var(--brand);
      color: #ffffff;
      box-shadow: 0 1px 3px rgba(234, 88, 12, 0.25);
    }
    .btn-primary:hover {
      background: hsl(26 73% 46%);
      transform: translateY(-1px);
    }
    .btn-outline {
      background: var(--surface);
      border-color: var(--border);
      color: var(--fg);
    }
    .btn-outline:hover {
      background: var(--surface-hover);
      border-color: var(--border-light);
    }
    .btn-sm { padding: 5px 10px; font-size: 12px; border-radius: 6px; }
    .btn-xs { padding: 3px 8px; font-size: 11px; border-radius: 4px; }

    /* Inputs & Search */
    .search-input {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 13px;
      color: var(--fg);
      outline: none;
      transition: all 0.15s ease;
    }
    .search-input:focus {
      border-color: var(--brand);
      box-shadow: 0 0 0 3px var(--brand-soft);
    }

    /* Tables */
    .table-container {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
      margin-bottom: 24px;
    }
    .opp-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }
    .opp-table th {
      background: var(--surface-hover);
      padding: 10px 14px;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--muted);
      border-bottom: 1px solid var(--border);
    }
    .opp-table td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      color: var(--fg);
    }
    .opp-table tr:hover td {
      background: var(--surface-hover);
    }

    /* Filter Bar */
    .filter-bar {
      display: flex;
      gap: 12px;
      margin-bottom: 18px;
      flex-wrap: wrap;
      align-items: center;
    }

    /* Command Modal & Dialogs */
    .cmd-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.4);
      backdrop-filter: blur(4px);
      z-index: 1000;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .cmd-modal.open {
      display: flex;
    }
    .cmd-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      width: 580px;
      max-width: 100%;
      box-shadow: var(--shadow-lg);
      padding: 20px;
    }
    .cmd-input {
      width: 100%;
      background: var(--surface-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px 14px;
      font-size: 14px;
      color: var(--fg);
      outline: none;
      margin-bottom: 14px;
    }
    .cmd-input:focus {
      border-color: var(--brand);
    }
    .cmd-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 4px;
      max-height: 280px;
      overflow-y: auto;
    }
    .cmd-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
      color: var(--fg);
    }
    .cmd-item:hover {
      background: var(--surface-hover);
      color: var(--brand-text);
    }

    /* Toast */
    .toast-note {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-left: 4px solid var(--brand);
      padding: 12px 18px;
      border-radius: 8px;
      box-shadow: var(--shadow-lg);
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 2000;
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .toast-note.show {
      transform: translateY(0);
      opacity: 1;
    }

    /* Mobile Header */
    .mobile-header {
      display: none;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 101;
    }

    /* Responsive Breakpoints */
    @media (max-width: 900px) {
      .app-layout { flex-direction: column; }
      .app-sidebar {
        position: fixed;
        left: -280px;
        transition: left 0.25s ease;
        box-shadow: var(--shadow-lg);
      }
      .app-sidebar.mobile-open {
        left: 0;
      }
      .mobile-header {
        display: flex;
      }
      .app-main {
        width: 100%;
        padding: 16px;
      }
    }
    @media (max-width: 600px) {
      .executive-top-bar {
        padding: 10px 12px;
      }
      .top-search-box {
        min-width: 100%;
      }
      .hero-banner {
        padding: 20px 16px;
      }
      .hero-heading {
        font-size: 28px;
      }
      .card-grid {
        grid-template-columns: 1fr;
      }
      .top-bar-right {
        margin-left: 0;
        width: 100%;
        justify-content: space-between;
      }
    }
  </style>"""

content = re.sub(r'<style>[\s\S]*?</style>', CSS_REPLACEMENT, content)

# 2. Update Executive Upper Ribbon Bar & Remove Double Headers
# Replace executive-top-bar and view-today header
RIBBON_AND_TODAY_HTML = """      <!-- Executive Upper Ribbon Bar (Clean, Unified Editorial Navigation) -->
      <header class="executive-top-bar">
        <div class="top-bar-left">
          <div class="ribbon-brand-badge">
            <span class="ribbon-brand-title">FrontierPilot 2.0</span>
            <span class="chip brand">Studio Edition</span>
          </div>
          <div class="live-status-pill health">
            <span class="pulse-dot emerald"></span>
            <span>Live System Health</span>
          </div>
          <div class="live-status-pill roles">
            <span class="pulse-dot brand"></span>
            <span>107 Monitored Roles</span>
          </div>
          <div class="live-status-pill sync">
            <span>📑 Notion & Cloud Synced</span>
          </div>
        </div>

        <div class="top-bar-right">
          <div class="top-search-box" onclick="openCmdPalette()">
            <span>🔍</span>
            <span style="color:var(--muted); font-size:12.5px;">Search pipeline, skills, portals...</span>
            <span class="cmd-key" style="margin-left:auto;">⌘K</span>
          </div>

          <div class="top-action-group">
            <button class="btn btn-primary btn-sm" onclick="openNewLinkedinPostModal()">✨ New Post</button>
            <button class="btn btn-outline btn-sm" onclick="triggerCrossPlatformSync('all')">⚡ Sync All</button>
            <button class="btn btn-outline btn-sm" onclick="exportPipelineCsv()">📥 Export CSV</button>
          </div>

          <button class="btn btn-outline btn-sm" onclick="toggleTheme()" title="Toggle Theme" style="padding:6px 10px;">
            <span id="themeToggleIcon">🌓</span>
          </button>

          <a href="https://github.com/Aryansharma906" target="_blank" class="user-profile-badge">
            <div class="user-avatar">AS</div>
            <div class="user-info-text">
              <div class="user-name">Aryan Sharma</div>
              <div class="user-role">AI & Security Researcher</div>
            </div>
          </a>
        </div>
      </header>

      <!-- ===================================================================
           TAB 1: TODAY COCKPIT (DUAL-LOOP RETENTION)
           =================================================================== -->
      <section id="view-today" class="view-panel">
        <div class="hero-banner">
          <div class="hero-date" id="heroTodayDate">Saturday, November 14</div>
          <h1 class="hero-heading">FrontierPilot Cockpit</h1>
          <p class="hero-sub">The dual-loop career retention engine: automated supply loop matches from zero-token portal scans paired with demand loop employer follow-up cadences.</p>
          
          <div class="hero-stats-row">
            <div class="hero-stat-item">
              <span class="hero-stat-val" id="statFreshMatches">8</span>
              <span class="hero-stat-label">Fresh Matches (7d)</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" id="statFollowupsDue">1</span>
              <span class="hero-stat-label">Follow-ups Due</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" id="statAwaitingDecisions">27</span>
              <span class="hero-stat-label">Awaiting Decision</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" id="statPipelineTotal">107</span>
              <span class="hero-stat-label">Monitored Opportunities</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" style="color:var(--emerald-500);">100%</span>
              <span class="hero-stat-label">Local-First Privacy</span>
            </div>
          </div>
        </div>

        <!-- Section: Follow-ups Due (Demand Loop) -->
        <div id="demandLoopSection" style="display:none;">
          <div class="section-title-wrap">
            <span class="section-icon">📨</span>
            <h2 class="section-heading">Follow-ups due today</h2>
            <span class="section-hint">· Overdue & Urgent outreach</span>
          </div>
          <div class="card-grid" id="followupsDueGrid"></div>
        </div>

        <!-- Section: Awaiting Your Decision -->
        <div class="section-title-wrap">
          <span class="section-icon">❓</span>
          <h2 class="section-heading">Awaiting your decision</h2>
          <span class="section-hint" id="statAwaitingDecisionsBadge">· Ranked by verified match score</span>
        </div>

        <!-- #1 Top Target Hero Banner -->
        <div class="apply-next-hero" id="applyNextCard">
          <span class="apply-next-tag">Apply Next · #1 Priority Target</span>
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-top:10px; gap:16px; flex-wrap:wrap;">
            <div style="display:flex; gap:14px; align-items:flex-start;">
              <div class="company-monogram" style="width:48px; height:48px; font-size:20px;">HS</div>
              <div>
                <h3 style="font-size:18px; font-weight:600; color:var(--fg);" id="applyNextTitle">AI Evaluation Specialist (LLM Reasoning & Safety)</h3>
                <div style="font-size:14px; color:var(--muted); margin-top:2px;" id="applyNextOrg">Handshake (San Francisco) · Remote Worldwide · $25 – $45/hr</div>
              </div>
            </div>
            <div class="score-badge priority" style="font-size:14px; padding:4px 10px;">100 Match</div>
          </div>
          <p style="font-size:13.5px; color:var(--muted); margin:14px 0;" id="applyNextReason">Verified live engagement; systematic evaluation of LLM reasoning, alignment, and adversarial defense.</p>
          <div class="card-actions">
            <a href="https://joinhandshake.com" target="_blank" class="btn btn-primary btn-sm">🚀 Open Job Posting</a>
            <button class="btn btn-outline btn-sm" onclick="switchTab('cvstudio')">📄 Tailor Resume</button>
            <button class="btn btn-outline btn-sm" onclick="copyApplicationPitch('handshake-ai-evaluator')">📋 Copy Pitch</button>
            <button class="btn btn-outline btn-sm" onclick="dispatchSlackApprovalAll()">📢 Send to Slack</button>
            <button class="btn btn-outline btn-sm" onclick="markAppliedQuick('handshake-ai-evaluator')">✓ Mark Applied</button>
            <button class="btn btn-outline btn-sm" style="margin-left:auto; color:var(--faint);" onclick="skipQuick('handshake-ai-evaluator')">✕ Skip</button>
          </div>
        </div>

        <!-- Grouped Decision Cards Grid -->
        <div class="card-grid" id="decisionGrid"></div>
        <div id="decisionCardsGrid" style="display:none;"></div>

        <!-- Section: Fresh matches this week (Supply Loop) -->
        <div class="section-title-wrap">
          <span class="section-icon">✨</span>
          <h2 class="section-heading">Fresh matches this week</h2>
          <span class="section-hint">· Found by free zero-token portal scans</span>
        </div>
        <div class="card-grid" id="freshMatchesGrid"></div>

        <!-- Quick Evaluator Card -->
        <div class="card" style="margin-top:24px;">
          <h3 style="font-size:15px; font-weight:600; color:var(--fg); margin-bottom:6px;">⚡ Quick URL Evaluator</h3>
          <p style="font-size:13px; color:var(--muted); margin-bottom:12px;">Paste any job posting URL or LinkedIn job description to evaluate instant ATS fit and generate tailored bullets.</p>
          <div style="display:flex; gap:10px;">
            <input type="text" id="quickUrlInput" class="search-input" style="flex:1;" placeholder="https://jobs.lever.co/company/role-title">
            <button class="btn btn-primary" onclick="quickEvaluateUrl()">Evaluate Fit</button>
          </div>
        </div>
      </section>"""

# Find start of main and start of tab 2
content = re.sub(
    r'<header class="executive-top-bar">[\s\S]*?</section>\s*(?=<section id="view-explore")',
    RIBBON_AND_TODAY_HTML + "\n\n      ",
    content
)

# 3. Fix LinkedIn Drafts script logic
# Ensure loadData calls setLinkedinDrafts and ALL_LINKEDIN_DRAFTS is properly preserved
content = re.sub(
    r'// LinkedIn Drafts\s*const resDrafts = await fetch\(\'/api/drafts\'\);[\s\S]*?renderLinkedinDrafts\(drafts\);\s*\}',
    """// LinkedIn Drafts
        const resDrafts = await fetch('/api/drafts');
        if (resDrafts.ok) {
          const draftsJson = await resDrafts.json();
          const drafts = Array.isArray(draftsJson) ? draftsJson : (draftsJson.drafts || []);
          setLinkedinDrafts(drafts);
        }""",
    content
)

# Insert setLinkedinDrafts and escapeHtml if not present
if "function setLinkedinDrafts" not in content:
    content = content.replace(
        "function renderLinkedinDrafts(drafts) {",
        """function setLinkedinDrafts(drafts) {
      ALL_LINKEDIN_DRAFTS = drafts || [];
      renderLinkedinDrafts(ALL_LINKEDIN_DRAFTS);
    }

    function renderLinkedinDrafts(drafts) {"""
    )

TARGET_HTML.write_text(content, encoding="utf-8")
DOCS_HTML.write_text(content, encoding="utf-8")
print(f"Updated {TARGET_HTML} ({len(content)} bytes) and {DOCS_HTML}")
