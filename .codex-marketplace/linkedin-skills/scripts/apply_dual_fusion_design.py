"""Dual-Application Design Fusion Engine for FrontierPilot 2.0.

Fuses the information architecture and functional workflows of FrontierPilot
with the ultra-premium Cyber-SaaS Dark Glassmorphic aesthetics inspired by Quantix / Nexus.io.
"""
from pathlib import Path
import re

ROOT = Path("/Users/aryansharma/Desktop/linkedin-skills-main")
TARGET_HTML = ROOT / "studio" / "templates" / "frontierpilot.html"
DOCS_HTML = ROOT / "docs" / "frontierpilot.html"

print("Reading target HTML...")
html = TARGET_HTML.read_text(encoding="utf-8")

# 1. NEW FUSED CSS DESIGN TOKENS & SYSTEM
FUSED_CSS = """
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

    :root, html.dark {
      /* Deep Cosmic Void Canvas */
      --bg: #070913;
      --bg-alt: #0b0f1e;
      --bg-nebula: #090d1f;

      /* Frosted Glassmorphism Surfaces */
      --surface: rgba(15, 21, 42, 0.72);
      --surface-hover: rgba(24, 34, 68, 0.85);
      --surface-active: rgba(30, 44, 88, 0.95);
      --surface-card: rgba(13, 18, 36, 0.75);
      --surface-elevated: rgba(18, 25, 52, 0.88);
      
      /* Glass Borders & Edge Highlights */
      --border: rgba(255, 255, 255, 0.08);
      --border-light: rgba(255, 255, 255, 0.15);
      --border-glow: rgba(99, 102, 241, 0.40);

      /* Typography & Contrast Colors */
      --fg: #f8fafc;
      --muted: #94a3b8;
      --faint: #64748b;
      --landing: #f1f5f9;

      /* Luminous Neon & Cyber Accents */
      --brand: #6366f1;
      --brand-text: #818cf8;
      --brand-soft: rgba(99, 102, 241, 0.16);
      --brand-foreground: #ffffff;
      
      --cyan-400: #22d3ee;
      --cyan-500: #06b6d4;
      --purple-400: #c084fc;
      --purple-500: #a855f7;
      --emerald-400: #34d399;
      --emerald-500: #10b981;
      --amber-400: #fbbf24;
      --amber-500: #f59e0b;
      --rose-400: #fb7185;
      --rose-500: #f43f5e;

      /* Gradients */
      --grad-cyan-blue: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
      --grad-purple-indigo: linear-gradient(135deg, #c084fc 0%, #6366f1 100%);
      --grad-emerald: linear-gradient(135deg, #34d399 0%, #059669 100%);
      --grad-amber: linear-gradient(135deg, #fbbf24 0%, #ea580c 100%);
      --grad-glass-card: linear-gradient(180deg, rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0.01) 100%);

      /* Glassmorphism & Shadow Effects */
      --glass-blur: blur(28px) saturate(190%);
      --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.35);
      --shadow-md: 0 8px 24px -4px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
      --shadow-lg: 0 16px 48px -8px rgba(0, 0, 0, 0.70), 0 0 0 1px rgba(255, 255, 255, 0.07) inset;
      --shadow-glow-cyan: 0 0 25px -4px rgba(6, 182, 212, 0.45);
      --shadow-glow-purple: 0 0 25px -4px rgba(168, 85, 247, 0.45);

      /* Typography */
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-serif: 'Instrument Serif', Georgia, serif;
      --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
    }

    html.light {
      --bg: #f5f4ef;
      --bg-alt: #eae8df;
      --surface: rgba(255, 255, 255, 0.85);
      --surface-hover: rgba(245, 243, 236, 0.95);
      --surface-active: #ffffff;
      --surface-card: #ffffff;
      --surface-elevated: #ffffff;
      --border: rgba(0, 0, 0, 0.08);
      --border-light: rgba(0, 0, 0, 0.14);
      --fg: #0f172a;
      --muted: #475569;
      --faint: #64748b;
      --landing: #1e293b;
      --brand: #4f46e5;
      --brand-text: #4338ca;
      --brand-soft: rgba(79, 70, 229, 0.10);
      --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.12);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg);
      color: var(--fg);
      font-family: var(--font-sans);
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
      min-height: 100vh;
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(6, 182, 212, 0.12) 0%, transparent 40%),
        radial-gradient(circle at 60% 85%, rgba(139, 92, 246, 0.14) 0%, transparent 50%),
        radial-gradient(circle at 92% 35%, rgba(99, 102, 241, 0.10) 0%, transparent 35%);
      background-attachment: fixed;
      background-repeat: no-repeat;
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

    /* Sidebar Navigation (Quantix Glass Rail) */
    .app-sidebar {
      width: 270px;
      flex-shrink: 0;
      background: rgba(10, 14, 28, 0.82);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border-right: 1px solid var(--border);
      position: sticky;
      top: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      padding: 24px 18px;
      overflow-y: auto;
      z-index: 50;
      box-shadow: 4px 0 24px rgba(0, 0, 0, 0.4);
    }

    .app-main {
      flex: 1;
      min-width: 0;
      padding: 24px 36px 60px 36px;
      max-width: 1440px;
      margin: 0 auto;
    }

    /* Brand Header */
    .brand-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 22px;
      text-decoration: none;
      color: inherit;
    }
    .brand-mark-orb {
      width: 38px;
      height: 38px;
      border-radius: 12px;
      background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #8b5cf6 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
      flex-shrink: 0;
    }
    .brand-title-wrap {
      display: flex;
      flex-direction: column;
    }
    .brand-title {
      font-family: var(--font-sans);
      font-weight: 700;
      font-size: 19px;
      letter-spacing: -0.02em;
      background: linear-gradient(180deg, #ffffff 30%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.1;
    }
    .brand-subtitle {
      font-size: 11px;
      color: var(--muted);
      letter-spacing: 0.04em;
      margin-top: 2px;
    }
    .brand-version-pill {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      color: var(--cyan-400);
      background: rgba(6, 182, 212, 0.14);
      border: 1px solid rgba(6, 182, 212, 0.3);
      padding: 2px 7px;
      border-radius: 12px;
      margin-left: auto;
    }

    /* Quick Find / Palette Trigger */
    .cmd-trigger {
      display: flex;
      align-items: center;
      gap: 10px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 9px 12px;
      font-size: 12.5px;
      color: var(--muted);
      cursor: pointer;
      margin-bottom: 20px;
      transition: all 0.2s ease;
      width: 100%;
      text-align: left;
    }
    .cmd-trigger:hover {
      border-color: rgba(99, 102, 241, 0.5);
      background: rgba(255, 255, 255, 0.08);
      color: var(--fg);
      box-shadow: 0 0 15px rgba(99, 102, 241, 0.2);
    }
    .cmd-key {
      margin-left: auto;
      font-family: var(--font-mono);
      font-size: 10px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-light);
      padding: 2px 6px;
      border-radius: 5px;
      color: var(--muted);
    }

    /* Navigation Sections */
    .nav-category-label {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--faint);
      margin: 16px 0 8px 10px;
    }
    .nav-list {
      display: flex;
      flex-direction: column;
      gap: 4px;
      list-style: none;
    }
    .nav-btn {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 9px 12px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 500;
      color: var(--muted);
      background: transparent;
      border: 1px solid transparent;
      width: 100%;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s ease;
      text-decoration: none;
    }
    .nav-btn:hover {
      background: rgba(255, 255, 255, 0.05);
      color: var(--fg);
      transform: translateX(2px);
    }
    .nav-btn.active {
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(168, 85, 247, 0.18));
      border: 1px solid rgba(168, 85, 247, 0.35);
      color: #ffffff;
      font-weight: 600;
      box-shadow: 0 0 20px -3px rgba(139, 92, 246, 0.3);
    }
    .nav-btn .icon {
      font-size: 15px;
      width: 18px;
      text-align: center;
      display: inline-block;
    }
    .nav-btn .badge {
      margin-left: auto;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.06);
      color: var(--muted);
      border: 1px solid var(--border);
    }
    .nav-btn.active .badge {
      background: var(--brand);
      color: #fff;
      border-color: transparent;
      box-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
    }

    /* Bottom Quantum Promo Card (Directly from User Uploaded Reference) */
    .quantum-sidebar-card {
      margin-top: auto;
      padding-top: 18px;
    }
    .quantum-card-inner {
      background: linear-gradient(180deg, rgba(24, 30, 60, 0.7) 0%, rgba(15, 18, 36, 0.9) 100%);
      border: 1px solid rgba(168, 85, 247, 0.25);
      border-radius: 14px;
      padding: 16px 14px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4), 0 0 20px -5px rgba(139, 92, 246, 0.25);
    }
    .quantum-card-inner::before {
      content: '';
      position: absolute;
      top: -30px;
      right: -30px;
      width: 90px;
      height: 90px;
      background: radial-gradient(circle, rgba(168, 85, 247, 0.35) 0%, transparent 70%);
      pointer-events: none;
    }
    .quantum-rocket-art {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.3), rgba(168, 85, 247, 0.2));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 10px;
      box-shadow: 0 0 15px rgba(168, 85, 247, 0.3);
    }
    .quantum-card-title {
      font-size: 13.5px;
      font-weight: 600;
      color: #ffffff;
      margin-bottom: 4px;
    }
    .quantum-card-sub {
      font-size: 11px;
      color: var(--muted);
      line-height: 1.4;
      margin-bottom: 12px;
    }
    .btn-quantum-action {
      width: 100%;
      padding: 8px 12px;
      border-radius: 8px;
      background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #d946ef 100%);
      color: #ffffff;
      border: none;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 16px rgba(139, 92, 246, 0.4);
    }
    .btn-quantum-action:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
    }
    .sidebar-copyright {
      font-size: 10px;
      color: var(--faint);
      text-align: center;
      margin-top: 10px;
    }

    /* Executive Top Command Bar */
    .executive-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      background: rgba(13, 18, 36, 0.72);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 12px 20px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-md);
      flex-wrap: wrap;
    }
    .top-bar-left {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }
    .top-search-box {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 6px 12px;
      font-size: 12.5px;
      color: var(--muted);
      cursor: pointer;
      min-width: 220px;
    }
    .top-search-box:hover {
      border-color: rgba(99, 102, 241, 0.4);
    }
    .live-status-pill {
      display: flex;
      align-items: center;
      gap: 7px;
      padding: 5px 11px;
      border-radius: 20px;
      font-size: 11.5px;
      font-weight: 500;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
    }
    .live-status-pill.stream {
      color: var(--cyan-400);
      border-color: rgba(6, 182, 212, 0.25);
      background: rgba(6, 182, 212, 0.06);
    }
    .live-status-pill.health {
      color: var(--emerald-400);
      border-color: rgba(16, 185, 129, 0.25);
      background: rgba(16, 185, 129, 0.06);
    }
    .pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      display: inline-block;
      animation: pulseGlow 2s infinite ease-in-out;
    }
    .pulse-dot.cyan { background: var(--cyan-400); box-shadow: 0 0 8px var(--cyan-400); }
    .pulse-dot.emerald { background: var(--emerald-400); box-shadow: 0 0 8px var(--emerald-400); }
    @keyframes pulseGlow {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    .top-bar-right {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-left: auto;
    }
    .top-btn {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 500;
      color: var(--muted);
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .top-btn:hover {
      background: rgba(255, 255, 255, 0.08);
      color: var(--fg);
    }
    .user-profile-badge {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 4px 10px 4px 4px;
      border-radius: 30px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
    }
    .user-avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: linear-gradient(135deg, #00f2fe, #8b5cf6);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 700;
      color: #fff;
      box-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
    }
    .user-info-text {
      display: flex;
      flex-direction: column;
    }
    .user-name {
      font-size: 12px;
      font-weight: 600;
      color: var(--fg);
      line-height: 1.1;
    }
    .user-role {
      font-size: 10px;
      color: var(--muted);
    }

    /* Cards & Containers (Glassmorphic) */
    .card {
      background: var(--surface-card);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 22px;
      box-shadow: var(--shadow-md);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .card:hover {
      border-color: rgba(255, 255, 255, 0.16);
      box-shadow: var(--shadow-lg);
      transform: translateY(-2px);
    }
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 18px;
      margin-top: 14px;
    }

    /* KPI Matrix & Radial Visualizer Cards */
    .kpi-row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 18px;
      margin-bottom: 24px;
    }
    @media (max-width: 1024px) {
      .kpi-row { grid-template-columns: 1fr; }
    }
    .kpi-card {
      background: var(--surface-card);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 20px 22px;
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }
    .kpi-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }
    .kpi-title {
      font-size: 13px;
      color: var(--muted);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .kpi-chip {
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 12px;
    }
    .kpi-chip.green {
      background: rgba(16, 185, 129, 0.15);
      color: var(--emerald-400);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .kpi-chip.cyan {
      background: rgba(6, 182, 212, 0.15);
      color: var(--cyan-400);
      border: 1px solid rgba(6, 182, 212, 0.3);
    }
    .kpi-chip.purple {
      background: rgba(168, 85, 247, 0.15);
      color: var(--purple-400);
      border: 1px solid rgba(168, 85, 247, 0.3);
    }
    .kpi-val {
      font-size: 32px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.1;
      letter-spacing: -0.02em;
    }
    .kpi-sub {
      font-size: 12px;
      color: var(--muted);
      margin-top: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Alluvial / Sankey & Analytics Row */
    .analytics-duo-row {
      display: grid;
      grid-template-columns: 1.6fr 1.1fr;
      gap: 18px;
      margin-bottom: 24px;
    }
    @media (max-width: 1024px) {
      .analytics-duo-row { grid-template-columns: 1fr; }
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.18s ease;
      text-decoration: none;
      border: 1px solid transparent;
    }
    .btn-primary {
      background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(99, 102, 241, 0.35);
    }
    .btn-primary:hover {
      box-shadow: 0 6px 20px rgba(99, 102, 241, 0.55);
      transform: translateY(-1px);
    }
    .btn-outline {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-light);
      color: var(--fg);
    }
    .btn-outline:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(255, 255, 255, 0.3);
    }
    .btn-sm {
      padding: 5px 10px;
      font-size: 12px;
      border-radius: 6px;
    }

    /* Data Table (Glass Grid) */
    .data-table-wrap {
      background: var(--surface-card);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow-x: auto;
      box-shadow: var(--shadow-md);
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }
    .data-table th {
      padding: 14px 18px;
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--muted);
      border-bottom: 1px solid var(--border);
      background: rgba(0, 0, 0, 0.2);
    }
    .data-table td {
      padding: 14px 18px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: var(--fg);
      vertical-align: middle;
    }
    .data-table tr:hover td {
      background: rgba(255, 255, 255, 0.03);
    }

    /* Chips & Badges */
    .chip {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 9px;
      border-radius: 12px;
      font-size: 11.5px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border);
      color: var(--muted);
    }
    .chip.brand {
      background: rgba(99, 102, 241, 0.14);
      color: var(--brand-text);
      border-color: rgba(99, 102, 241, 0.3);
    }
    .chip.cyan {
      background: rgba(6, 182, 212, 0.14);
      color: var(--cyan-400);
      border-color: rgba(6, 182, 212, 0.3);
    }
    .score-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 4px 10px;
      border-radius: 12px;
      font-weight: 700;
      font-size: 12px;
      font-family: var(--font-mono);
    }
    .score-badge.priority {
      background: linear-gradient(135deg, rgba(6, 182, 212, 0.2), rgba(99, 102, 241, 0.2));
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.4);
      box-shadow: 0 0 12px rgba(6, 182, 212, 0.25);
    }
    .score-badge.strong {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(52, 211, 153, 0.35);
    }

    /* Filter Bars & Tabs */
    .filter-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }
    .search-input {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 8px 14px;
      color: var(--fg);
      font-size: 13px;
      outline: none;
      transition: all 0.2s ease;
    }
    .search-input:focus {
      border-color: var(--brand);
      box-shadow: 0 0 14px rgba(99, 102, 241, 0.3);
    }
    .tab-strip {
      display: flex;
      gap: 6px;
      background: rgba(0, 0, 0, 0.3);
      padding: 4px;
      border-radius: 10px;
      border: 1px solid var(--border);
      width: fit-content;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }
    .tab-strip-btn {
      padding: 6px 14px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 500;
      color: var(--muted);
      background: transparent;
      border: none;
      cursor: pointer;
      transition: all 0.18s ease;
    }
    .tab-strip-btn:hover { color: var(--fg); }
    .tab-strip-btn.active {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      font-weight: 600;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    }

    /* Diff Blocks (CV Studio) */
    .diff-block {
      background: rgba(0, 0, 0, 0.35);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 16px;
    }
    .diff-del {
      background: rgba(244, 63, 94, 0.12);
      border-left: 3px solid var(--rose-500);
      color: #fca5a5;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      font-size: 13px;
      line-height: 1.45;
    }
    .diff-add {
      background: rgba(16, 185, 129, 0.14);
      border-left: 3px solid var(--emerald-500);
      color: #6ee7b7;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      font-size: 13px;
      line-height: 1.45;
    }

    /* Toggle Switch */
    .toggle-switch {
      position: relative;
      display: inline-block;
      width: 36px;
      height: 20px;
    }
    .toggle-switch input { opacity: 0; width: 0; height: 0; }
    .toggle-slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: rgba(255, 255, 255, 0.12);
      transition: .3s;
      border-radius: 20px;
    }
    .toggle-slider:before {
      position: absolute;
      content: "";
      height: 14px;
      width: 14px;
      left: 3px;
      bottom: 3px;
      background-color: white;
      transition: .3s;
      border-radius: 50%;
    }
    input:checked + .toggle-slider {
      background: linear-gradient(135deg, #00f2fe, #4facfe);
    }
    input:checked + .toggle-slider:before {
      transform: translateX(16px);
    }

    /* Mobile Header */
    .mobile-header {
      display: none;
      padding: 14px 20px;
      background: rgba(10, 14, 28, 0.95);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 60;
      backdrop-filter: var(--glass-blur);
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
      .executive-top-bar { display: none; }
    }

    /* Toast Notification */
    .toast-note {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: rgba(15, 21, 42, 0.92);
      backdrop-filter: var(--glass-blur);
      border: 1px solid rgba(168, 85, 247, 0.3);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(139, 92, 246, 0.25);
      padding: 12px 18px;
      border-radius: 12px;
      color: #fff;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 9999;
      opacity: 0;
      pointer-events: none;
      transform: translateY(12px);
      transition: all 0.25s ease;
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
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 9000;
    }
    .cmd-modal.open { display: flex; }
    .cmd-box {
      width: 580px;
      max-width: 90%;
      background: rgba(13, 18, 36, 0.95);
      backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-light);
      border-radius: 16px;
      padding: 20px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(99, 102, 241, 0.3);
    }
"""

print("Injecting Fused CSS tokens...")
html = re.sub(r'<style>[\s\S]*?</style>', f'<style>{FUSED_CSS}</style>', html, count=1)

# 2. UPDATE SIDEBAR (Categorized + Quantum AI Promo Card matching reference)
FUSED_SIDEBAR = """    <aside class="app-sidebar" id="appSidebar">
      <a href="#" onclick="switchTab('today'); return false;" class="brand-header">
        <div class="brand-mark-orb">⚡</div>
        <div class="brand-title-wrap">
          <div class="brand-title">FrontierPilot</div>
          <div class="brand-subtitle">Autonomous Creator Studio</div>
        </div>
        <span class="brand-version-pill">2.0</span>
      </a>

      <button class="cmd-trigger" onclick="openCmdPalette()">
        <span>🔍 Search roles, actions...</span>
        <span class="cmd-key">⌘K</span>
      </button>

      <div class="nav-category-label">GENERAL</div>
      <ul class="nav-list">
        <li>
          <button class="nav-btn active" data-tab="today" onclick="switchTab('today')">
            <span class="icon">📊</span>
            <span>Dashboard / Today</span>
            <span class="badge" id="navBadgeToday">8 fresh</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="pipeline" onclick="switchTab('pipeline')">
            <span class="icon">📋</span>
            <span>Pipeline Triage</span>
            <span class="badge" id="navBadgePipeline">27</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="explore" onclick="switchTab('explore')">
            <span class="icon">🧭</span>
            <span>Explore Portals</span>
            <span class="badge" style="background:rgba(6,182,212,0.15); color:#22d3ee; border-color:transparent;">NEW</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="compare" onclick="switchTab('compare')">
            <span class="icon">⚖️</span>
            <span>Compare Matrix</span>
          </button>
        </li>
      </ul>

      <div class="nav-category-label">STUDIO ENGINES</div>
      <ul class="nav-list">
        <li>
          <button class="nav-btn" data-tab="cvstudio" onclick="switchTab('cvstudio')">
            <span class="icon">📝</span>
            <span>CV Studio (X-Y-Z)</span>
            <span class="badge">ATS</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="linkedin" onclick="switchTab('linkedin')">
            <span class="icon">🚀</span>
            <span>LinkedIn Studio</span>
            <span class="badge" style="background:rgba(168,85,247,0.15); color:#c084fc; border-color:transparent;">AI</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="wix" onclick="switchTab('wix')">
            <span class="icon">🌐</span>
            <span>Wix Studio Hub</span>
            <span class="badge">CMS</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="intelligence" onclick="switchTab('intelligence')">
            <span class="icon">🧠</span>
            <span>Intelligence Radar</span>
            <span class="badge" style="background:rgba(16,185,129,0.15); color:#34d399; border-color:transparent;">Active</span>
          </button>
        </li>
      </ul>

      <div class="nav-category-label">SYSTEM & RADAR</div>
      <ul class="nav-list">
        <li>
          <button class="nav-btn" data-tab="portals" onclick="switchTab('portals')">
            <span class="icon">📡</span>
            <span>Portals Health</span>
            <span class="badge">10 live</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="followups" onclick="switchTab('followups')">
            <span class="icon">📨</span>
            <span>Follow-ups Radar</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="scheduled" onclick="switchTab('scheduled')">
            <span class="icon">📅</span>
            <span>Scheduled Scans</span>
          </button>
        </li>
        <li>
          <button class="nav-btn" data-tab="profile" onclick="switchTab('profile')">
            <span class="icon">👤</span>
            <span>Profile & Config</span>
          </button>
        </li>
      </ul>

      <!-- Quantix Style Bottom Promo Card -->
      <div class="quantum-sidebar-card">
        <div class="quantum-card-inner">
          <div class="quantum-rocket-art">🚀</div>
          <div class="quantum-card-title">Autonomous AI Cycle</div>
          <div class="quantum-card-sub">Self-improving telemetry & ATS calibration loop</div>
          <button class="btn-quantum-action" onclick="triggerIntelligenceOptimization()">
            <span>Activate Quantum AI</span>
            <span>⚡</span>
          </button>
          <div class="sidebar-copyright">© 2026 Orbitron AI · Nexus Frontier</div>
        </div>
      </div>
    </aside>"""

print("Injecting Fused Sidebar...")
html = re.sub(r'<aside class="app-sidebar" id="appSidebar">[\s\S]*?</aside>', FUSED_SIDEBAR, html, count=1)

# 3. EXECUTIVE TOP COMMAND BAR (Inserted right after <main class="app-main">)
EXECUTIVE_TOP_BAR = """
      <!-- Executive Top Command Bar (Directly Inspired by Quantix/Nexus) -->
      <header class="executive-top-bar">
        <div class="top-bar-left">
          <div class="top-search-box" onclick="openCmdPalette()">
            <span>🔍</span>
            <span style="color:var(--muted); font-size:12.5px;">Search pipeline, skills, portals...</span>
            <span class="cmd-key" style="margin-left:auto;">⌘ + F</span>
          </div>
          <div class="live-status-pill stream">
            <span class="pulse-dot cyan"></span>
            <span>Data streaming</span>
            <span>⚡</span>
          </div>
          <div class="live-status-pill health">
            <span class="pulse-dot emerald"></span>
            <span>Live system health</span>
          </div>
        </div>
        <div class="top-bar-right">
          <div class="top-btn" style="color:var(--muted); font-family:var(--font-mono);">
            <span>📅 Oct 18 - Nov 18 · Monthly ▾</span>
          </div>
          <button class="top-btn" onclick="openCmdPalette()" title="Filter">
            <span>⚙️ Filter</span>
          </button>
          <button class="top-btn" onclick="exportPipelineCsv()" title="Export CSV">
            <span>📥 Export</span>
          </button>
          <div class="user-profile-badge">
            <div class="user-avatar">AS</div>
            <div class="user-info-text">
              <div class="user-name">Aryan Sharma</div>
              <div class="user-role">AI Systems & Red-Teamer</div>
            </div>
          </div>
        </div>
      </header>
"""

# Check if executive top bar is already in app-main
if '<header class="executive-top-bar">' not in html:
    print("Injecting Executive Top Command Bar...")
    html = html.replace('<main class="app-main">', '<main class="app-main">\n' + EXECUTIVE_TOP_BAR)

# 4. ENHANCED TODAY COCKPIT WITH CHARTS (Radial Arc, Velocity Sparklines, Sankey Flow, Cohort Bars, Donut, Connections)
FUSED_TODAY_VIEW = """      <section id="view-today" class="view-panel">
        
        <!-- ROW 1: KPI MATRIX & RADIAL GAUGE (QUANTIX AESTHETIC) -->
        <div class="kpi-row">
          
          <!-- Card 1: Global Growth Score (Radial Gauge Arc) -->
          <div class="kpi-card">
            <div class="kpi-header">
              <span class="kpi-title">🎯 Global Match Score</span>
              <span class="kpi-chip green">+18.4% ATS</span>
            </div>
            <div style="display:flex; align-items:center; justify-content:space-between; margin-top:4px;">
              <div>
                <div class="kpi-val" id="kpiGrowthScore">94%</div>
                <div class="kpi-sub">
                  <span style="color:var(--emerald-400);">●</span>
                  <span>Top 1% Candidate Alignment</span>
                </div>
              </div>
              <!-- Glowing Radial Arc Gauge SVG -->
              <div style="width:72px; height:72px; position:relative;">
                <svg viewBox="0 0 36 36" style="width:100%; height:100%; transform: rotate(-90deg);">
                  <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="3.5" />
                  <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="url(#arcGrad)" stroke-width="3.8" stroke-dasharray="94, 100" stroke-linecap="round" />
                  <defs>
                    <linearGradient id="arcGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                      <stop offset="0%" stop-color="#00f2fe" />
                      <stop offset="100%" stop-color="#8b5cf6" />
                    </linearGradient>
                  </defs>
                </svg>
                <div style="position:absolute; top:0; left:0; width:100%; height:100%; display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:700; color:var(--cyan-400);">94%</div>
              </div>
            </div>
          </div>

          <!-- Card 2: Recurring Compensation & Staged Roles -->
          <div class="kpi-card">
            <div class="kpi-header">
              <span class="kpi-title">💼 Recurring Target Comp</span>
              <span class="kpi-chip cyan">27 Roles</span>
            </div>
            <div style="display:flex; align-items:flex-end; justify-content:space-between; margin-top:4px;">
              <div>
                <div class="kpi-val">$185,000</div>
                <div class="kpi-sub">
                  <span style="color:var(--cyan-400);">▲ 15.5%</span>
                  <span>vs Market Avg ($142k)</span>
                </div>
              </div>
              <!-- Glowing Cyan Sparkline SVG -->
              <div style="width:110px; height:38px;">
                <svg viewBox="0 0 100 35" style="width:100%; height:100%;">
                  <path d="M0 28 Q 20 20, 40 24 T 70 12 T 100 4" fill="none" stroke="#00f2fe" stroke-width="2.5" />
                  <path d="M0 28 Q 20 20, 40 24 T 70 12 T 100 4 L 100 35 L 0 35 Z" fill="rgba(0, 242, 254, 0.12)" />
                </svg>
              </div>
            </div>
          </div>

          <!-- Card 3: Active Application Conversion Rate -->
          <div class="kpi-card">
            <div class="kpi-header">
              <span class="kpi-title">⚡ Conversion Velocity</span>
              <span class="kpi-chip purple">31.5%</span>
            </div>
            <div style="display:flex; align-items:flex-end; justify-content:space-between; margin-top:4px;">
              <div>
                <div class="kpi-val">31.5%</div>
                <div class="kpi-sub">
                  <span style="color:var(--emerald-400);">▲ 8.3%</span>
                  <span>Interview Rate Lift</span>
                </div>
              </div>
              <!-- Glowing Emerald Sparkline SVG -->
              <div style="width:110px; height:38px;">
                <svg viewBox="0 0 100 35" style="width:100%; height:100%;">
                  <path d="M0 30 Q 25 15, 50 22 T 80 8 T 100 2" fill="none" stroke="#10b981" stroke-width="2.5" />
                  <path d="M0 30 Q 25 15, 50 22 T 80 8 T 100 2 L 100 35 L 0 35 Z" fill="rgba(16, 185, 129, 0.12)" />
                </svg>
              </div>
            </div>
          </div>

        </div>

        <!-- ROW 2: DEEP ANALYTICS & FLOW VISUALIZATION -->
        <div class="analytics-duo-row">
          
          <!-- Left: Cross-Platform Pipeline Growth (Interactive Alluvial / Sankey Flow) -->
          <div class="card" style="display:flex; flex-direction:column;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <div>
                <h3 style="font-size:16px; font-weight:600; color:#fff;">🌊 Cross-Platform Pipeline Flow</h3>
                <div style="font-size:12px; color:var(--muted); margin-top:2px;">Discovered (135) → Staged (27) → Applied (8) → Interview (2) → Offer (1)</div>
              </div>
              <div style="display:flex; gap:6px;">
                <span class="chip cyan">Active Cycle</span>
                <span class="chip font-mono">100% Verified</span>
              </div>
            </div>

            <!-- Alluvial Flow Diagram Ribbon SVG -->
            <div style="background:rgba(0,0,0,0.25); border-radius:12px; border:1px solid rgba(255,255,255,0.06); padding:16px 12px; flex:1;">
              <svg viewBox="0 0 540 130" style="width:100%; height:130px; display:block;">
                <defs>
                  <linearGradient id="flowGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.6" />
                    <stop offset="100%" stop-color="#6366f1" stop-opacity="0.6" />
                  </linearGradient>
                  <linearGradient id="flowGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#6366f1" stop-opacity="0.6" />
                    <stop offset="100%" stop-color="#a855f7" stop-opacity="0.6" />
                  </linearGradient>
                  <linearGradient id="flowGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#a855f7" stop-opacity="0.6" />
                    <stop offset="100%" stop-color="#10b981" stop-opacity="0.6" />
                  </linearGradient>
                </defs>
                <!-- Flow Ribbons -->
                <path d="M 40 25 C 120 25, 120 45, 190 45 L 190 75 C 120 75, 120 45, 40 45 Z" fill="url(#flowGrad1)" />
                <path d="M 190 45 C 260 45, 260 30, 340 30 L 340 55 C 260 55, 260 75, 190 75 Z" fill="url(#flowGrad2)" />
                <path d="M 340 30 C 410 30, 410 50, 490 50 L 490 70 C 410 70, 410 55, 340 55 Z" fill="url(#flowGrad3)" />
                
                <!-- Stage Pillar Nodes -->
                <rect x="25" y="15" width="16" height="40" rx="4" fill="#00f2fe" />
                <text x="33" y="70" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="monospace">DISCOVER</text>
                
                <rect x="182" y="35" width="16" height="50" rx="4" fill="#6366f1" />
                <text x="190" y="100" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="monospace">STAGED (27)</text>

                <rect x="332" y="22" width="16" height="42" rx="4" fill="#a855f7" />
                <text x="340" y="80" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="monospace">APPLIED (8)</text>

                <rect x="482" y="42" width="16" height="34" rx="4" fill="#10b981" />
                <text x="490" y="92" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="monospace">OFFER (1)</text>
              </svg>
            </div>
          </div>

          <!-- Right: Recruiter Touch Cohort Retention (Neon Bars) -->
          <div class="card" style="display:flex; flex-direction:column;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <div>
                <h3 style="font-size:16px; font-weight:600; color:#fff;">📊 Weekly Recruiter Velocity</h3>
                <div style="font-size:12px; color:var(--muted); margin-top:2px;">Touches & Inbound Conversions</div>
              </div>
              <span class="chip green">● Live</span>
            </div>

            <!-- Neon Gradient Bars -->
            <div style="display:flex; align-items:flex-end; justify-content:space-between; height:130px; padding:10px 10px 0 10px; background:rgba(0,0,0,0.25); border-radius:12px; border:1px solid rgba(255,255,255,0.06);">
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:85px; border-radius:6px; background:linear-gradient(180deg, #c084fc, #6366f1); box-shadow:0 0 12px rgba(99,102,241,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Sun</span>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:105px; border-radius:6px; background:linear-gradient(180deg, #38bdf8, #0284c7); box-shadow:0 0 12px rgba(6,182,212,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Mon</span>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:95px; border-radius:6px; background:linear-gradient(180deg, #34d399, #059669); box-shadow:0 0 12px rgba(16,185,129,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Tue</span>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:115px; border-radius:6px; background:linear-gradient(180deg, #fbbf24, #ea580c); box-shadow:0 0 12px rgba(245,158,11,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Wed</span>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:80px; border-radius:6px; background:linear-gradient(180deg, #f472b6, #db2777); box-shadow:0 0 12px rgba(244,63,94,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Thu</span>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:90px; border-radius:6px; background:linear-gradient(180deg, #a78bfa, #7c3aed); box-shadow:0 0 12px rgba(139,92,246,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Fri</span>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
                <div style="width:24px; height:60px; border-radius:6px; background:linear-gradient(180deg, #fb7185, #e11d48); box-shadow:0 0 12px rgba(225,29,72,0.4);"></div>
                <span style="font-size:10px; color:var(--muted);">Sat</span>
              </div>
            </div>
          </div>

        </div>

        <!-- ROW 3: SUPERPOWER MIX (DONUT) & SYSTEM CONNECTIONS (INTEGRATION TABLE) -->
        <div class="analytics-duo-row">
          
          <!-- Left: Superpower Alignment Donut Chart -->
          <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <h3 style="font-size:16px; font-weight:600; color:#fff;">🍩 Superpower Alignment Mix</h3>
              <span class="chip purple">4 Core Clusters</span>
            </div>
            <div style="display:flex; align-items:center; justify-content:space-around; gap:16px; flex-wrap:wrap;">
              <!-- 3D Donut SVG -->
              <div style="width:120px; height:120px; position:relative;">
                <svg viewBox="0 0 42 42" style="width:100%; height:100%; transform:rotate(-90deg);">
                  <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#00f2fe" stroke-width="6" stroke-dasharray="35 65" stroke-dashoffset="0" />
                  <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#6366f1" stroke-width="6" stroke-dasharray="30 70" stroke-dashoffset="-35" />
                  <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#a855f7" stroke-width="6" stroke-dasharray="25 75" stroke-dashoffset="-65" />
                  <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#f59e0b" stroke-width="6" stroke-dasharray="10 90" stroke-dashoffset="-90" />
                </svg>
                <div style="position:absolute; top:0; left:0; width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                  <span style="font-size:16px; font-weight:700; color:#fff;">94%</span>
                  <span style="font-size:9px; color:var(--muted);">FIT</span>
                </div>
              </div>
              <div style="display:flex; flex-direction:column; gap:8px;">
                <div style="display:flex; align-items:center; gap:8px; font-size:12px;">
                  <span style="width:8px; height:8px; border-radius:50%; background:#00f2fe;"></span>
                  <span>Adversarial Prompt Security (35%)</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px; font-size:12px;">
                  <span style="width:8px; height:8px; border-radius:50%; background:#6366f1;"></span>
                  <span>LLM Evaluation & Alignment (30%)</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px; font-size:12px;">
                  <span style="width:8px; height:8px; border-radius:50%; background:#a855f7;"></span>
                  <span>Agentic Automation Pipelines (25%)</span>
                </div>
                <div style="display:flex; align-items:center; gap:8px; font-size:12px;">
                  <span style="width:8px; height:8px; border-radius:50%; background:#f59e0b;"></span>
                  <span>Linux Systems & High-Velocity (10%)</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Right: System Connections Grid (Directly from Reference Image) -->
          <div class="card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
              <h3 style="font-size:16px; font-weight:600; color:#fff;">🔌 System Connections & Health</h3>
              <a href="#" onclick="switchTab('portals'); return false;" style="font-size:12px; color:var(--cyan-400); text-decoration:none;">See All ↗</a>
            </div>
            
            <table style="width:100%; border-collapse:collapse; font-size:12px;">
              <thead>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.08); color:var(--muted); text-align:left;">
                  <th style="padding-bottom:8px;">Application</th>
                  <th style="padding-bottom:8px;">Health</th>
                  <th style="padding-bottom:8px;">Frequency</th>
                  <th style="padding-bottom:8px; text-align:right;">State</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
                  <td style="padding:10px 0; font-weight:500;">🤖 Google Gemini 2.0</td>
                  <td><span style="color:#10b981;">●●●●</span></td>
                  <td style="color:var(--muted); font-family:monospace;">Realtime</td>
                  <td style="text-align:right;">
                    <label class="toggle-switch"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                  </td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
                  <td style="padding:10px 0; font-weight:500;">📑 Notion Sync Hub</td>
                  <td><span style="color:#10b981;">●●●○</span></td>
                  <td style="color:var(--muted); font-family:monospace;">15m sync</td>
                  <td style="text-align:right;">
                    <label class="toggle-switch"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                  </td>
                </tr>
                <tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
                  <td style="padding:10px 0; font-weight:500;">🌐 Wix Headless CMS</td>
                  <td><span style="color:#10b981;">●●●●</span></td>
                  <td style="color:var(--muted); font-family:monospace;">Staged hook</td>
                  <td style="text-align:right;">
                    <label class="toggle-switch"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                  </td>
                </tr>
                <tr>
                  <td style="padding:10px 0; font-weight:500;">📢 Slack Approver</td>
                  <td><span style="color:#10b981;">●●●●</span></td>
                  <td style="color:var(--muted); font-family:monospace;">Instant dispatch</td>
                  <td style="text-align:right;">
                    <label class="toggle-switch"><input type="checkbox" checked><span class="toggle-slider"></span></label>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

        </div>

        <!-- Section: Awaiting Your Decision (Immediate Action Queue) -->
        <div style="display:flex; align-items:center; justify-content:space-between; margin:28px 0 16px 0;">
          <div style="display:flex; align-items:center; gap:10px;">
            <span style="font-size:18px;">❓</span>
            <h2 style="font-size:20px; font-weight:700; color:#fff;">Awaiting Your Immediate Decision</h2>
            <span style="font-size:13px; color:var(--muted);">· Ranked by verified match score</span>
          </div>
          <span class="chip cyan" id="statAwaitingDecisionsBadge">27 in Pipeline</span>
        </div>

        <!-- #1 Top Target Hero Banner -->
        <div class="card" id="applyNextCard" style="background:linear-gradient(135deg, rgba(15,21,42,0.85), rgba(30,27,75,0.85)); border:1px solid rgba(99,102,241,0.35); margin-bottom:20px; box-shadow:0 10px 30px rgba(0,0,0,0.5), 0 0 20px rgba(99,102,241,0.2);">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <span class="chip brand" style="font-weight:600; letter-spacing:0.04em;">Apply Next · #1 Priority Target</span>
            <div class="score-badge priority" style="font-size:13px; padding:4px 10px;">100 Match</div>
          </div>
          <div style="display:flex; gap:16px; align-items:flex-start; margin-top:10px; flex-wrap:wrap;">
            <div style="width:48px; height:48px; border-radius:12px; background:linear-gradient(135deg, #00f2fe, #6366f1); display:flex; align-items:center; justify-content:center; font-size:20px; font-weight:700; color:#fff; box-shadow:0 0 15px rgba(0,242,254,0.4);">HS</div>
            <div style="flex:1;">
              <h3 style="font-size:18px; font-weight:600; color:#fff;" id="applyNextTitle">AI Evaluation Specialist (LLM Reasoning & Safety)</h3>
              <div style="font-size:13.5px; color:var(--muted); margin-top:2px;" id="applyNextOrg">Handshake (San Francisco) · Remote Worldwide · $25 – $45/hr</div>
            </div>
          </div>
          <p style="font-size:13.5px; color:var(--fg); margin:14px 0; line-height:1.5;" id="applyNextReason">Verified live engagement; systematic evaluation of LLM reasoning, alignment, and adversarial defense.</p>
          <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:12px;">
            <a href="https://joinhandshake.com" target="_blank" class="btn btn-primary btn-sm">🚀 Open Job Posting</a>
            <button class="btn btn-outline btn-sm" onclick="copyApplicationPitch('handshake-ai-evaluator')">📋 Copy Tailored Pitch</button>
            <button class="btn btn-outline btn-sm" onclick="markAppliedQuick('handshake-ai-evaluator')">✓ Mark Applied</button>
            <button class="btn btn-outline btn-sm" style="margin-left:auto; color:var(--faint);" onclick="skipQuick('handshake-ai-evaluator')">✕ Skip</button>
          </div>
        </div>

        <!-- Grouped Decision Cards Grid -->
        <div class="card-grid" id="decisionGrid"></div>

        <!-- Section: Fresh matches this week (Supply Loop) -->
        <div style="display:flex; align-items:center; gap:10px; margin:32px 0 16px 0;">
          <span style="font-size:18px;">✨</span>
          <h2 style="font-size:20px; font-weight:700; color:#fff;">Fresh matches this week</h2>
          <span style="font-size:13px; color:var(--muted);">· Found by free zero-token portal scans</span>
        </div>
        <div class="card-grid" id="freshMatchesGrid"></div>

        <!-- Quick Evaluator Card -->
        <div class="card" style="margin-top:24px;">
          <h3 style="font-size:15px; font-weight:600; color:#fff; margin-bottom:6px;">⚡ Quick URL Evaluator</h3>
          <p style="font-size:13px; color:var(--muted); margin-bottom:12px;">Paste any job posting URL or LinkedIn job description to evaluate instant ATS fit and generate tailored bullets.</p>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <input type="text" id="quickUrlInput" class="search-input" style="flex:1; min-width:240px;" placeholder="https://jobs.lever.co/company/role-title">
            <button class="btn btn-primary" onclick="quickEvaluateUrl()">Evaluate Fit</button>
          </div>
        </div>
      </section>"""

print("Injecting Fused Today Cockpit view...")
html = re.sub(r'<section id="view-today" class="view-panel">[\s\S]*?</section>', FUSED_TODAY_VIEW, html, count=1)

print("Writing updated HTML to studio/templates/frontierpilot.html...")
TARGET_HTML.write_text(html, encoding="utf-8")
print("Syncing to docs/frontierpilot.html...")
DOCS_HTML.write_text(html, encoding="utf-8")

print(f"Successfully fused and wrote {len(html)} bytes to both files!")
