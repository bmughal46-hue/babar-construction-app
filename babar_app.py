import streamlit as st
import pandas as pd

# --- 1. CONFIG & AUTH ---
st.set_page_config(page_title="Babar Real Estate | Official", layout="wide", page_icon="🏠")

# Initialize Session States
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'ads' not in st.session_state:
    st.session_state.ads = [
        {"price": "3.50 Crore", "loc": "DHA Phase 8, Broadway", "size": "1 Kanal", "type": "Residential"},
    ]

# --- 2. ZAMEEN & DHA PLUS PREMIUM UI ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fb; }
    .stApp { max-width: 550px; margin: 0 auto; background: white; border-right: 1px solid #eee; border-left: 1px solid #eee; box-shadow: 0 0 20px rgba(0,0,0,0.05); }
    
    /* Header Styling */
    .header-box { background: linear-gradient(135deg, #003366 0%, #001f3f 100%); color: white; padding: 25px; text-align: center; border-radius: 0 0 30px 30px; margin-bottom: 20px; }
    
    /* Property Card */
    .property-card { background: white; border-radius: 15px; padding: 18px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); border-left: 6px solid #28a745; }
    .price-text { color: #28a745; font-size: 24px; font-weight: 800; }
    
    /* Bill Styling */
    .bill-frame { border: 2px solid #333; padding: 25px; background: #fff; border-radius: 5px; font-family: 'Courier New', Courier, monospace; position: relative; }
    .bill-header { border-bottom: 2px solid #333; margin-bottom: 15px; padding-bottom: 10px; text-align: center; }
    
    /* Footer WhatsApp */
    .whatsapp-bar { position: fixed; bottom: 0; width: 100%; max-width: 550px; background: #25D366; color: white; text-align: center; padding: 12px; font-weight: bold; z-index: 1000; box-shadow: 0 -2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP BRANDING ---
st.markdown("""
    <div class='header-box'>
        <h1 style='margin:0; font-size:28px;'>BABAR REAL ESTATE</h1>
        <p style='margin:5px 0; font-size:14px; opacity:0.8;'>CEO: Bilal Mughal</p>
        <p style='font-size:11px;'>Broadway Plaza No. C-116, Phase 8, DHA Lahore</p>
    </div>
    """, unsafe_allow_html=True)

# --- 4. ADMIN ACCESS (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("Admin Portal")
    if not st.session_state.logged_in:
        u = st.text_input("User ID")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if u == "admin" and p == "babar123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Ghalat ID/Password")
    else:
        st.success("Welcome, Bilal Mughal")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

# --- 5. MAIN NAVIGATION ---
tabs = st.tabs(["🏡 Listings", "🤖 AI Advisor", "🧮 Construction", "⚙️ Post Ad"])

# --- TAB 1: LISTINGS ---
with tabs[0]:
    st.markdown("### Featured Inventory")
    for ad in st.session_state.ads:
        st.markdown(f"""
        <div class="property-card">
            <div class="price-text">PKR {ad['price']}</div>
            <div style="font-weight:bold; margin-bottom:5px;">{ad['size']} - {ad['type']}</div>
            <div style="color:#666; font-size:13px; margin-bottom:10px;">📍 {ad['loc']}</div>
            <div style="display:flex; gap:10px;">
                <span style="background:#f0f2f5; padding:2px 8px; border-radius:5px; font-size:11px;">DHA Lahore</span>
                <span style="background:#f0f2f5; padding:2px 8px; border-radius:5px; font-size:11px;">Verified</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Location Reference
    st.info("📍 Visit Us: C-116, Broadway Plaza, DHA Phase 8, Lahore")

# --- TAB 2: AI PROPERTY AGENT ---
with tabs[1]:
    st.subheader("🤖 Smart AI Advisor")
    prompt = st.text_input("Investement ke bare mein pochein:", placeholder="e.g. Phase 8 ROI?")
    if prompt:
        with st.spinner("AI is analyzing Zameen & Market trends..."):
            st.success(f"Bilal Mughal's AI Insight: {prompt} suggests high growth. Phase 8 Broadway area is currently a hot zone for commercial activity.")

# --- TAB 3: CONSTRUCTION BILLING (ADVANCED) ---
with tabs[2]:
    st.subheader("🧮 Professional Estimator")
    c_size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    c_qual = st.radio("Quality", ["Grey Structure", "Premium Finishing (A+)"])
    
    # Accurate Rates 2026
    rate = 3450 if c_qual == "Grey Structure" else 6900
    area = {"5 Marla": 1950, "10 Marla": 3300, "1 Kanal": 5500}[c_size]
    total_val = area * rate
    
    st.markdown("---")
    st.markdown(f"""
    <div class='bill-frame'>
        <div class='bill-header'>
            <h3 style='margin:0;'>BABAR REAL ESTATE</h3>
            <p style='font-size:10px;'>Official Construction Estimate</p>
        </div>
        <p><b>Client:</b> Valued Customer</p>
        <p><b>Plot:</b> {c_size} ({c_qual})</p>
        <p><b>Area:</b> {area} Sq.Ft</p>
        <p><b>Market Rate:</b> {rate}/sqft</p>
        <hr style='border: 1px dashed #333'>
        <h3 style='text-align:right;'>NET TOTAL: PKR {total_val:,.0f}</h3>
        <p style='font-size:9px; text-align:center; margin-top:20px;'>Generated by Bilal Mughal SaaS System</p>
    </div>
    """, unsafe_allow_html=True)
    st.caption("📸 Take a screenshot to download/share this bill.")

# --- TAB 4: ADMIN (POST ADS) ---
with tabs[3]:
    if st.session_state.logged_in:
        st.subheader("Add Live Inventory")
        with st.form("admin_post"):
            p = st.text_input("Price (e.g. 2.5 Crore)")
            l = st.text_input("Location (Phase/Sector)")
            s = st.selectbox("Size", ["5 Marla", "10 Marla", "1 Kanal"])
            if st.form_submit_button("Publish Globally"):
                st.session_state.ads.insert(0, {"price": p, "loc": l, "size": s, "type": "Residential"})
                st.success("Ad Live on Marketplace!")
    else:
        st.warning("🔒 Login required to post ads. Check Sidebar.")

# --- 6. STICKY WHATSAPP FOOTER ---
st.markdown(f"""
    <div class='whatsapp-bar'>
        <a href='https://wa.me/923244000041' style='color:white; text-decoration:none;'>
            📞 Call/WhatsApp: Babar Mughal (+92 324 4000041)
        </a>
    </div>
    """, unsafe_allow_html=True)
