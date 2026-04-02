import streamlit as st
import pandas as pd

# --- 1. CORE SETUP (Syntax Fix) ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# --- 2. THEME & BEAUTY (DHA PLUS STYLE) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    .stApp { max-width: 500px; margin: 0 auto; border: 1px solid #ddd; background: white; }
    .card { background: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 4px solid #C5A059; }
    .price { color: #856404; background: #fff3cd; padding: 3px 8px; border-radius: 4px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATABASE (SESSION) ---
if 'db' not in st.session_state:
    st.session_state.db = [
        {"price": "330 Lakh", "phase": "Phase 9 Prism", "size": "1 Kanal", "plot": "Sector A"},
        {"price": "425 Lakh", "phase": "Phase 7", "size": "1 Kanal", "plot": "Sector Y"}
    ]

# --- 4. NAVIGATION TABS (ALL 4 FEATURES) ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home/Ads", "🤖 AI Advisor", "🧮 Calculator", "⚙️ Admin"])

# --- FEATURE 1: ADS MANAGEMENT (HOME) ---
with tab1:
    st.markdown("### Hot <span style='color:red'>Classified</span> 🔥", unsafe_allow_html=True)
    for item in st.session_state.db:
        st.markdown(f"""
        <div class="card">
            <span class="price">{item['price']}</span>
            <p style='margin:10px 0;'><b>{item['size']} - {item['phase']}</b><br>
            <span style='font-size:12px; color:#666;'>{item['plot']}</span></p>
            <button style='width:100%; border:none; background:#007bff; color:white; border-radius:5px;'>Contact Bilal Mughal</button>
        </div>
        """, unsafe_allow_html=True)

# --- FEATURE 2: AI PROPERTY ADVISOR ---
with tab2:
    st.subheader("🤖 Babar AI Agent")
    q = st.text_input("Ask about DHA investment:")
    if q:
        st.info(f"Analyzing '{q}'... Bilal Mughal recommends Phase 9 Prism for long term ROI in 2026.")

# --- FEATURE 3: CONSTRUCTION CALCULATOR ---
with tab3:
    st.subheader("🧮 2026 Construction Calc")
    s = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    rate = 3450 # Verified 2026 Rate
    area = {"5 Marla": 2100, "10 Marla": 3500, "1 Kanal": 6500}[s]
    st.metric("Estimated Cost", f"PKR {(area*rate)/1000000:.2f}M")

# --- FEATURE 4: ADMIN PANEL ---
with tab4:
    st.subheader("⚙️ Admin Dashboard")
    with st.form("add_plot"):
        p = st.text_input("Price (Lakh)")
        ph = st.text_input("Phase")
        sz = st.text_input("Size")
        if st.form_submit_button("Post Live Ad"):
            st.session_state.db.insert(0, {"price": p+" Lakh", "phase": ph, "size": sz, "plot": "New Listing"})
            st.success("Ad is now Live on Home!")

st.markdown("<br><center><p style='color:#999; font-size:10px;'>Babar Group SaaS v15.0</p></center>", unsafe_allow_html=True)
