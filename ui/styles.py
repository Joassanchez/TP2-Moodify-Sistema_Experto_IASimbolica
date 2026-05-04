from __future__ import annotations

import streamlit as st

PALETA = {
    "bg": "#0B0F0C",
    "surface": "#151A16",
    "surface_2": "#1B211C",
    "border": "#2A322B",
    "accent": "#B7FF3C",
    "accent_soft": "#D6FF72",
    "accent_muted": "#78A83B",
    "text_primary": "#F5F7F5",
    "text_secondary": "#AAB3AA",
    "text_muted": "#7F8B80",
}


def inject_custom_css() -> None:
    """Inyecta el sistema visual dark premium de Moodify."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

        :root {
            --bg: #0B0F0C;
            --surface: #151A16;
            --surface-2: #1B211C;
            --border: #2A322B;
            --accent: #B7FF3C;
            --accent-soft: #D6FF72;
            --accent-muted: #78A83B;
            --text-primary: #F5F7F5;
            --text-secondary: #AAB3AA;
            --text-muted: #7F8B80;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(183, 255, 60, 0.12), transparent 28%),
                radial-gradient(circle at top right, rgba(120, 168, 59, 0.10), transparent 24%),
                linear-gradient(180deg, #0B0F0C 0%, #0A0D0A 100%);
            color: var(--text-primary);
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111611 0%, #0C100D 100%);
            border-right: 1px solid rgba(183, 255, 60, 0.08);
        }

        section[data-testid="stSidebar"] > div {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
        }

        section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] label {
            color: var(--text-secondary);
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background: rgba(21, 26, 22, 0.96);
            border: 1px solid rgba(42, 50, 43, 0.9);
            border-radius: 14px;
            min-height: 3rem;
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.16);
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] span {
            color: var(--text-primary);
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] svg {
            fill: var(--accent-soft);
        }

        div.stButton > button {
            width: 100%;
            border: 1px solid rgba(183, 255, 60, 0.18) !important;
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-soft) 100%) !important;
            color: #0B0F0C !important;
            border-radius: 16px !important;
            font-weight: 900 !important;
            letter-spacing: 0.01em;
            padding: 0.85rem 1rem !important;
            box-shadow: 0 14px 32px rgba(183, 255, 60, 0.18);
            transition: transform 0.16s ease, box-shadow 0.16s ease, filter 0.16s ease;
        }

        div.stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 18px 40px rgba(183, 255, 60, 0.24);
            filter: brightness(1.02);
        }

        div.stButton > button:active {
            transform: translateY(0);
        }

        .moodify-hero {
            background: linear-gradient(180deg, rgba(21, 26, 22, 0.98) 0%, rgba(13, 17, 14, 0.98) 100%);
            border: 1px solid rgba(183, 255, 60, 0.12);
            border-radius: 28px;
            padding: 1.6rem 1.6rem 1.45rem;
            margin-bottom: 1.15rem;
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.28);
            position: relative;
            overflow: hidden;
        }

        .moodify-hero:before {
            content: "";
            position: absolute;
            inset: -40% auto auto -8%;
            width: 340px;
            height: 340px;
            border-radius: 999px;
            background: radial-gradient(circle, rgba(183, 255, 60, 0.16), transparent 68%);
            filter: blur(10px);
            pointer-events: none;
        }

        .hero-kicker, .chip-row, .hero-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
        }

        .hero-kicker, .hero-meta {
            position: relative;
            z-index: 1;
        }

        .hero-title {
            position: relative;
            z-index: 1;
            font-size: clamp(2.2rem, 5vw, 3.8rem);
            line-height: 1.02;
            margin: 0.15rem 0 0;
            font-weight: 900;
            letter-spacing: -0.05em;
            color: var(--text-primary);
        }

        .hero-subtitle {
            position: relative;
            z-index: 1;
            max-width: 820px;
            margin-top: 0.8rem;
            color: var(--text-secondary);
            font-size: 1.02rem;
            line-height: 1.65;
        }

        .hero-pill, .chip, .track-tag, .conf-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            border-radius: 999px;
            font-weight: 800;
            letter-spacing: 0.01em;
            line-height: 1;
        }

        .hero-pill, .chip {
            padding: 0.5rem 0.8rem;
            border: 1px solid rgba(42, 50, 43, 0.9);
            background: rgba(11, 15, 12, 0.72);
            color: var(--text-secondary);
            font-size: 0.78rem;
        }

        .chip.accent, .hero-pill.accent {
            border-color: rgba(183, 255, 60, 0.28);
            background: linear-gradient(135deg, rgba(183, 255, 60, 0.13), rgba(118, 168, 59, 0.11));
            color: var(--accent-soft);
        }

        .section-card {
            background: linear-gradient(180deg, rgba(21, 26, 22, 0.98) 0%, rgba(16, 20, 17, 0.98) 100%);
            border: 1px solid rgba(42, 50, 43, 0.96);
            border-radius: 24px;
            padding: 1.2rem;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.24);
            margin-bottom: 1rem;
        }

        .section-head {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .section-title {
            font-size: 1.22rem;
            font-weight: 900;
            letter-spacing: -0.03em;
            margin: 0;
            color: var(--text-primary);
        }

        .section-caption {
            margin-top: 0.25rem;
            color: var(--text-secondary);
            font-size: 0.86rem;
            line-height: 1.55;
        }

        .sidebar-shell {
            margin-bottom: 0.75rem;
        }

        .sidebar-kicker {
            color: var(--accent-soft);
            text-transform: uppercase;
            letter-spacing: 0.18em;
            font-size: 0.72rem;
            font-weight: 900;
            margin-bottom: 0.45rem;
        }

        .sidebar-title {
            color: var(--text-primary);
            font-size: 1.15rem;
            font-weight: 900;
            line-height: 1.08;
            margin: 0;
            letter-spacing: -0.03em;
        }

        .sidebar-text {
            color: var(--text-secondary);
            font-size: 0.86rem;
            line-height: 1.55;
            margin-top: 0.5rem;
        }

        .sidebar-section-label {
            color: var(--text-primary);
            text-transform: uppercase;
            letter-spacing: 0.13em;
            font-size: 0.72rem;
            font-weight: 900;
            margin: 0.95rem 0 0.5rem;
        }

        .query-block {
            background: #0B0F0C;
            border: 1px solid rgba(183, 255, 60, 0.16);
            border-radius: 16px;
            padding: 0.95rem 1rem;
            color: #EDF6E0;
            font-family: 'JetBrains Mono', 'SFMono-Regular', Consolas, monospace;
            font-size: 0.84rem;
            line-height: 1.55;
            white-space: pre-wrap;
            overflow-x: auto;
            box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.02);
        }

        .badge-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.55rem;
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 0.8rem;
        }

        .stat-card {
            background: rgba(11, 15, 12, 0.82);
            border: 1px solid rgba(42, 50, 43, 0.95);
            border-radius: 18px;
            padding: 0.9rem;
            min-height: 84px;
        }

        .stat-label {
            color: var(--text-muted);
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            margin-bottom: 0.35rem;
            font-weight: 800;
        }

        .stat-value {
            color: var(--text-primary);
            font-size: 0.96rem;
            line-height: 1.45;
            font-weight: 700;
        }

        .stat-value.badge {
            display: inline-flex;
            width: auto;
            padding: 0.4rem 0.7rem;
            border-radius: 999px;
            background: rgba(183, 255, 60, 0.12);
            border: 1px solid rgba(183, 255, 60, 0.30);
            color: var(--accent-soft);
        }

        .note-box {
            margin-top: 0.9rem;
            padding: 0.95rem 1rem;
            border-radius: 16px;
            background: rgba(11, 15, 12, 0.74);
            border: 1px solid rgba(183, 255, 60, 0.14);
            color: var(--text-secondary);
            line-height: 1.55;
            font-size: 0.88rem;
        }

        .conf-wrap {
            margin-top: 0.9rem;
            padding: 1rem;
            border-radius: 18px;
            background: linear-gradient(180deg, rgba(11, 15, 12, 0.88), rgba(21, 26, 22, 0.82));
            border: 1px solid rgba(183, 255, 60, 0.12);
        }

        .conf-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .conf-pct {
            font-size: 2rem;
            font-weight: 900;
            letter-spacing: -0.05em;
            color: var(--accent);
            line-height: 1;
        }

        .conf-desc {
            margin-top: 0.3rem;
            color: var(--text-secondary);
            font-size: 0.84rem;
            line-height: 1.45;
        }

        .conf-badge {
            padding: 0.45rem 0.75rem;
            font-size: 0.74rem;
        }

        .conf-high {
            background: rgba(183, 255, 60, 0.14);
            color: var(--accent-soft);
            border: 1px solid rgba(183, 255, 60, 0.34);
        }

        .conf-mid {
            background: rgba(214, 255, 114, 0.10);
            color: var(--accent-soft);
            border: 1px solid rgba(214, 255, 114, 0.24);
        }

        .conf-low {
            background: rgba(255, 184, 77, 0.10);
            color: #FFD69A;
            border: 1px solid rgba(255, 184, 77, 0.24);
        }

        .progress-shell {
            margin-top: 0.85rem;
            width: 100%;
            height: 12px;
            border-radius: 999px;
            overflow: hidden;
            background: rgba(42, 50, 43, 0.95);
            border: 1px solid rgba(183, 255, 60, 0.12);
        }

        .progress-fill {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, #B7FF3C 0%, #D6FF72 100%);
            box-shadow: 0 0 14px rgba(183, 255, 60, 0.28);
        }

        .track-card {
            background: linear-gradient(180deg, rgba(21, 26, 22, 0.96) 0%, rgba(16, 20, 17, 0.96) 100%);
            border: 1px solid rgba(42, 50, 43, 0.95);
            border-radius: 18px;
            padding: 0.85rem;
            margin-bottom: 0;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.20);
            min-height: 312px;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
        }

        .track-card:hover {
            transform: translateY(-2px);
            border-color: rgba(183, 255, 60, 0.24);
            box-shadow: 0 16px 34px rgba(0, 0, 0, 0.26);
        }

        .track-top {
            display: flex;
            gap: 0.65rem;
            align-items: center;
        }

        .track-index {
            width: 1.45rem;
            height: 1.45rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            background: rgba(183, 255, 60, 0.14);
            color: var(--accent-soft);
            border: 1px solid rgba(183, 255, 60, 0.28);
            font-size: 0.72rem;
            font-weight: 900;
            flex: 0 0 auto;
        }

        .track-cover {
            width: 100%;
            aspect-ratio: 1 / 1;
            border-radius: 10px;
            object-fit: cover;
            display: block;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.24);
            border: 1px solid rgba(255, 255, 255, 0.06);
        }

        .track-cover-fallback {
            width: 100%;
            aspect-ratio: 1 / 1;
            border-radius: 10px;
            border: 1px dashed rgba(183, 255, 60, 0.28);
            background: linear-gradient(180deg, rgba(11, 15, 12, 0.88), rgba(21, 26, 22, 0.82));
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: #AAB3AA;
            font-size: 0.72rem;
            text-align: center;
            padding: 0.25rem;
            line-height: 1.2;
        }

        .track-title {
            color: var(--text-primary);
            font-size: 0.98rem;
            font-weight: 800;
            line-height: 1.25;
            margin-bottom: 0.1rem;
        }

        .track-artist {
            color: var(--text-secondary);
            font-size: 0.84rem;
            line-height: 1.3;
        }

        .track-album {
            color: var(--text-muted);
            font-size: 0.78rem;
            margin-top: 0.14rem;
            line-height: 1.25;
        }

        .track-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.7rem;
            flex-wrap: wrap;
            margin-top: auto;
        }

        .track-link {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.42rem 0.72rem;
            border-radius: 999px;
            background: linear-gradient(135deg, rgba(183, 255, 60, 0.95), rgba(214, 255, 114, 0.92));
            color: #0B0F0C !important;
            font-size: 0.77rem;
            font-weight: 900;
            text-decoration: none;
            box-shadow: 0 10px 22px rgba(183, 255, 60, 0.18);
        }

        .track-link:hover {
            filter: brightness(1.03);
        }

        .track-tag {
            padding: 0.35rem 0.62rem;
            background: rgba(118, 168, 59, 0.14);
            color: var(--accent-soft);
            border: 1px solid rgba(118, 168, 59, 0.28);
            font-size: 0.72rem;
        }

        .empty-state {
            padding: 1rem;
            border-radius: 16px;
            background: rgba(11, 15, 12, 0.74);
            border: 1px solid rgba(183, 255, 60, 0.14);
            color: var(--text-secondary);
            line-height: 1.55;
        }

        div[data-testid="stDataFrame"] {
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(42, 50, 43, 0.88);
        }

        div[data-testid="stExpander"] details {
            border: 1px solid rgba(42, 50, 43, 0.95);
            border-radius: 16px;
            background: rgba(17, 21, 18, 0.76);
        }

        div[data-testid="stExpander"] summary {
            color: var(--text-primary) !important;
            font-weight: 800;
        }

        .stAlert {
            border-radius: 16px;
        }

        div[data-testid="stCodeBlock"] {
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(183, 255, 60, 0.14);
        }

        div[data-testid="stCodeBlock"] pre {
            background-color: #0B0F0C !important;
            color: #EDF6E0 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
