import os
import streamlit as st

# ----------------------------------------------------------------------
#  Page config  (must be the first Streamlit call)
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Sreyhong Heng — Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
#  Design system  (injected CSS)
#  Aesthetic: "scientific paper" — cool graph-paper canvas, teal data
#  accent, Space Grotesk display + Inter body + JetBrains Mono readouts.
# ----------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root{
  --ink:#0E1726;
  --paper:#F4F6F8;
  --surface:#FFFFFF;
  --line:rgba(14,23,38,0.10);
  --grid:rgba(14,23,38,0.040);
  --accent:#0FB5A6;
  --accent-ink:#0A8C80;
  --accent-2:#F4794B;
  --muted:#5E6C82;
  --muted-soft:#8A95A6;
}

/* ---- App canvas: faint graph-paper grid ---- */
.stApp{
  background-color:var(--paper);
  background-image:
     linear-gradient(var(--grid) 1px, transparent 1px),
     linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size:30px 30px;
}
.block-container{max-width:1060px; padding-top:2.4rem; padding-bottom:4.5rem;}

/* ---- Base type ---- */
html, body, .stApp, p, li { font-family:'Inter',system-ui,sans-serif; color:var(--ink); }
h1,h2,h3,h4{ font-family:'Space Grotesk',sans-serif; color:var(--ink); letter-spacing:-0.02em; }

/* ---- Sidebar ---- */
[data-testid="stSidebar"]{ background:var(--ink); border-right:1px solid rgba(255,255,255,0.06); }
[data-testid="stSidebar"] *{ color:#E8EDF4; }
.side-brand{ font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:1.25rem; color:#fff; line-height:1.1; margin:0.2rem 0 0.15rem; }
.side-tag{ font-family:'JetBrains Mono',monospace; font-size:0.66rem; letter-spacing:0.16em; text-transform:uppercase; color:var(--accent); margin-bottom:1.4rem; }
.side-foot{ font-family:'JetBrains Mono',monospace; font-size:0.66rem; color:rgba(232,237,244,0.45); letter-spacing:0.06em; margin-top:1.3rem; line-height:1.6; }
[data-testid="stSidebar"] a{ color:var(--accent); text-decoration:none; }

/* radio nav */
[data-testid="stSidebar"] .stRadio div[role="radiogroup"]{ gap:0.15rem; }
[data-testid="stSidebar"] .stRadio label{
  font-family:'JetBrains Mono',monospace; font-size:0.85rem; letter-spacing:0.02em;
  padding:0.42rem 0.55rem; border-radius:8px; transition:background .15s ease;
}
[data-testid="stSidebar"] .stRadio label:hover{ background:rgba(255,255,255,0.05); }

/* ---- Shared bits ---- */
.eyebrow{
  font-family:'JetBrains Mono',monospace; font-size:0.72rem; font-weight:500;
  letter-spacing:0.18em; text-transform:uppercase; color:var(--accent-ink);
  display:inline-flex; align-items:center; gap:.55rem; margin-bottom:1rem;
}
.eyebrow::before{ content:""; width:26px; height:2px; background:var(--accent); display:inline-block; }
.lead{ font-size:1.12rem; line-height:1.7; color:var(--muted); max-width:60ch; margin:0.4rem 0 0; }

/* ---- Hero ---- */
.hero-name{ font-size:clamp(2.6rem,7vw,4.3rem); font-weight:700; line-height:1.02; margin:0; }
.hero-role{ font-family:'Space Grotesk',sans-serif; font-size:clamp(1.05rem,2.6vw,1.4rem); font-weight:500; color:var(--ink); margin:0.7rem 0 1.1rem; }
.hero-role .sep{ color:var(--accent); padding:0 0.35rem; }
.readout{ display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:1.6rem; }
.readout span{
  font-family:'JetBrains Mono',monospace; font-size:0.78rem; color:var(--muted);
  background:var(--surface); border:1px solid var(--line); border-radius:999px; padding:0.4rem 0.85rem;
}
.readout b{ color:var(--accent-ink); font-weight:600; }

/* ---- Stat tiles ---- */
.stat-grid{ display:grid; grid-template-columns:repeat(3,1fr); gap:0.9rem; margin-top:2.4rem; }
.stat{ background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:1.1rem 1.2rem; }
.stat-num{ font-family:'JetBrains Mono',monospace; font-size:1.9rem; font-weight:600; color:var(--ink); line-height:1; }
.stat-label{ font-size:0.8rem; color:var(--muted); margin-top:0.5rem; }

/* ---- Section heading ---- */
.section-title{ font-size:clamp(1.8rem,4vw,2.5rem); font-weight:700; margin:0 0 0.4rem; }

/* ---- Project panels ---- */
.panel{
  background:var(--surface); border:1px solid var(--line); border-left:3px solid var(--accent);
  border-radius:14px; padding:1.4rem 1.5rem; margin-bottom:1rem;
  transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.panel:hover{ transform:translateY(-3px); box-shadow:0 14px 30px -18px rgba(14,23,38,0.35); border-left-color:var(--accent-2); }
.panel-head{ display:flex; justify-content:space-between; align-items:center; margin-bottom:0.7rem; }
.tag{ font-family:'JetBrains Mono',monospace; font-size:0.66rem; letter-spacing:0.14em; text-transform:uppercase; color:var(--accent-ink); background:rgba(15,181,166,0.10); border:1px solid rgba(15,181,166,0.22); padding:0.25rem 0.6rem; border-radius:6px; }
.panel-index{ font-family:'JetBrains Mono',monospace; font-size:0.85rem; color:var(--muted-soft); }
.panel-title{ font-size:1.3rem; font-weight:600; margin:0 0 0.45rem; }
.panel-body{ color:var(--muted); line-height:1.65; margin:0 0 1rem; font-size:0.97rem; }
.panel-foot{ display:flex; flex-wrap:wrap; gap:0.45rem; }
.metric{ font-family:'JetBrains Mono',monospace; font-size:0.74rem; color:var(--ink); background:var(--paper); border:1px solid var(--line); border-radius:7px; padding:0.3rem 0.6rem; }
.metric b{ color:var(--muted-soft); font-weight:500; }

/* ---- Skills ---- */
.skill-block{ margin-bottom:1.1rem; }
.skill-label{ font-family:'JetBrains Mono',monospace; font-size:0.72rem; letter-spacing:0.1em; text-transform:uppercase; color:var(--muted-soft); margin-bottom:0.55rem; }
.chips{ display:flex; flex-wrap:wrap; gap:0.45rem; }
.chip{ font-size:0.85rem; color:var(--ink); background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:0.4rem 0.8rem; transition:border-color .15s ease, color .15s ease; }
.chip:hover{ border-color:var(--accent); color:var(--accent-ink); }

/* ---- Contact ---- */
.contact-grid{ display:grid; grid-template-columns:repeat(2,1fr); gap:0.9rem; margin-top:0.6rem; }
.contact-card{ display:block; background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:1.1rem 1.3rem; text-decoration:none; transition:border-color .15s ease, transform .15s ease; }
.contact-card:hover{ border-color:var(--accent); transform:translateY(-2px); }
.cc-label{ font-family:'JetBrains Mono',monospace; font-size:0.68rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--accent-ink); margin-bottom:0.35rem; }
.cc-value{ font-size:1rem; color:var(--ink); font-weight:500; word-break:break-all; }

/* ---- Footer rule ---- */
.foot{ margin-top:3rem; padding-top:1.2rem; border-top:1px solid var(--line); font-family:'JetBrains Mono',monospace; font-size:0.72rem; color:var(--muted-soft); letter-spacing:0.05em; }

/* ---- Download button ---- */
.stDownloadButton button{
  font-family:'JetBrains Mono',monospace !important; font-weight:500 !important;
  background:var(--ink) !important; color:#fff !important; border:none !important;
  border-radius:10px !important; padding:0.6rem 1.2rem !important;
}
.stDownloadButton button:hover{ background:var(--accent-ink) !important; color:#fff !important; }

/* ---- Responsive ---- */
@media (max-width:640px){
  .stat-grid{ grid-template-columns:1fr 1fr; }
  .contact-grid{ grid-template-columns:1fr; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------
#  Content  (edit these to make the portfolio yours)
# ----------------------------------------------------------------------
PROJECTS = [
    {
        "tag": "MACHINE LEARNING",
        "idx": "01",
        "title": "Customer Churn Prediction",
        "body": "A logistic regression model trained on telecom customer data to flag who is "
                "likely to leave — and surface the factors that drive the decision.",
        "metrics": [("accuracy", "0.81"), ("model", "logistic reg."), ("data", "telecom")],
    },
    {
        "tag": "FORECASTING",
        "idx": "02",
        "title": "Cambodia Import / Export Forecasting",
        "body": "A regression model that predicts Cambodia's trade flows from historical "
                "import and export records.",
        "metrics": [("method", "regression"), ("scope", "trade flows"), ("source", "historical")],
    },
]

SKILLS = [
    ("languages", ["Python", "SQL", "R"]),
    ("ml & stats", ["scikit-learn", "PyTorch", "Regression", "Classification", "Statistics"]),
    ("data & viz", ["pandas", "NumPy", "Matplotlib", "Streamlit"]),
]

CONTACTS = [
    ("email", "hong86097@gmail.com", "mailto:hong86097@gmail.com"),
    ("phone", "+855 955 355 82", "tel:+85595535582"),
    ("github", "github.com/yourusername", "https://github.com/yourusername"),
    ("linkedin", "linkedin.com/in/yourusername", "https://linkedin.com/in/yourusername"),
]


# ----------------------------------------------------------------------
#  Small HTML helpers
# ----------------------------------------------------------------------
def header(eyebrow, title):
    st.markdown(
        f'<div class="eyebrow">{eyebrow}</div><h2 class="section-title">{title}</h2>',
        unsafe_allow_html=True,
    )


def panel_html(p):
    metrics = "".join(f'<span class="metric"><b>{k}</b> {v}</span>' for k, v in p["metrics"])
    return f"""<div class="panel">
  <div class="panel-head"><span class="tag">{p['tag']}</span><span class="panel-index">{p['idx']}</span></div>
  <h3 class="panel-title">{p['title']}</h3>
  <p class="panel-body">{p['body']}</p>
  <div class="panel-foot">{metrics}</div>
</div>"""


def skill_html(label, items):
    chips = "".join(f'<span class="chip">{i}</span>' for i in items)
    return f'<div class="skill-block"><div class="skill-label">{label}</div><div class="chips">{chips}</div></div>'


def contact_html(label, value, href):
    return (
        f'<a class="contact-card" href="{href}" target="_blank">'
        f'<div class="cc-label">{label}</div><div class="cc-value">{value}</div></a>'
    )


# ----------------------------------------------------------------------
#  Sidebar / navigation
# ----------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        '<div class="side-brand">Sreyhong Heng</div>'
        '<div class="side-tag">data · ml · viz</div>',
        unsafe_allow_html=True,
    )
    page = st.radio("Navigate", ["Home", "Projects", "Resume", "Contact"], label_visibility="collapsed")
    st.markdown('<div class="side-foot">ITC · Phnom Penh<br>© 2026</div>', unsafe_allow_html=True)


# ----------------------------------------------------------------------
#  Pages
# ----------------------------------------------------------------------
if page == "Home":
    st.markdown(
        """
<div class="eyebrow">PORTFOLIO // PHNOM PENH, KH</div>
<h1 class="hero-name">Sreyhong&nbsp;Heng</h1>
<div class="hero-role">Data Analyst <span class="sep">/</span> Machine Learning Enthusiast</div>
<p class="lead">Third-year Applied Mathematics &amp; Statistics student at the Institute of Technology
of Cambodia. I turn messy data into models that hold up — and into visuals that make the story obvious.</p>
<div class="readout">
  <span><b>focus</b> = analysis · modeling · visualization</span>
  <span><b>tools</b> = python · pandas · scikit-learn</span>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
<div class="stat-grid">
  <div class="stat"><div class="stat-num">03</div><div class="stat-label">current year at ITC</div></div>
  <div class="stat"><div class="stat-num">02</div><div class="stat-label">featured projects</div></div>
  <div class="stat"><div class="stat-num">0.81</div><div class="stat-label">best model accuracy</div></div>
</div>
""",
        unsafe_allow_html=True,
    )

elif page == "Projects":
    header("WORK // SELECTED", "Projects")
    st.markdown(
        '<p class="lead" style="margin-bottom:2rem">A few things I have built while learning to let the data talk.</p>',
        unsafe_allow_html=True,
    )
    for p in PROJECTS:
        st.markdown(panel_html(p), unsafe_allow_html=True)

    st.markdown('<div style="height:2.2rem"></div>', unsafe_allow_html=True)
    header("TOOLKIT // STACK", "What I work with")
    st.markdown("".join(skill_html(label, items) for label, items in SKILLS), unsafe_allow_html=True)

elif page == "Resume":
    header("CV // DOWNLOAD", "Resume")
    st.markdown(
        '<p class="lead">Grab the full PDF — education, projects, and the tools above, on a single page.</p>',
        unsafe_allow_html=True,
    )
    st.markdown('<div style="height:0.8rem"></div>', unsafe_allow_html=True)

    cv_path = "Mycv_HENGSREYHONG.pdf"
    if os.path.exists(cv_path):
        with open(cv_path, "rb") as f:
            st.download_button(
                "↓  Download CV (PDF)",
                f,
                file_name="Sreyhong_Heng_CV.pdf",
                mime="application/pdf",
            )
    else:
        st.info(
            "Place your CV file (named **Mycv_HENGSREYHONG.pdf**) in the same folder as "
            "this script to switch on the download button."
        )

elif page == "Contact":
    header("REACH OUT // SAY HI", "Contact")
    st.markdown(
        '<p class="lead">Open to internships, data projects, and good conversations about models.</p>',
        unsafe_allow_html=True,
    )
    cards = "".join(contact_html(label, value, href) for label, value, href in CONTACTS)
    st.markdown(f'<div class="contact-grid">{cards}</div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------
#  Footer (every page)
# ----------------------------------------------------------------------
st.markdown(
    '<div class="foot">designed &amp; built by Sreyhong Heng · streamlit · 2026</div>',
    unsafe_allow_html=True,
)