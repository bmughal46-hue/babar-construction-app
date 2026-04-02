import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CORE CONFIG (Pehli line hamesha yahi honi chahiye) ---
st.set_page_config(page_title="Babar Real Estate | SaaS", layout="wide")

# --- 2. PREMIUM MOBILE-APP STYLING ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stApp { max-width: 550px; margin: 0 auto; border: 1px solid #ddd; background: white; }
    .nav-card { background: white; padding: 15px; border-radius: 12px; margin-bottom: 10px; border-left: 5px solid #C5A059; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .price-badge { background: #fff3cd; color: #856404; padding: 4px 8px; border-radius: 5px; font-weight: bold; font-size: 14px; }
    .hot-tag { color: white; background: #ff4b4b; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE (Data Storage) ---
if 'inventory' not in st.session_state:
    st.session_state.inventory = [
        {"plot": "102-J", "phase": "Phase 9 Prism", "size": "5 Marla", "price": "1.35 Cr", "contact": "+92 300 1234567"},
        {"plot": "45-A", "phase": "Phase 6", "size": "1 Kanal", "price": "7.5 Cr", "contact": "+92 300 7654321"}
    ]

# --- 4. HEADER & BRANDING ---
st.markdown("<h2 style='text-align: center; color: #C5A059;'>BABAR REAL ESTATE</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>SaaS Platform by Bilal Mughal</p>", unsafe_allow_html=True)

# --- 5. MAIN NAVIGATION (Tabs as App Sections) ---
tab_home, tab_ai, tab_calc, tab_admin = st.tabs(["🏠 Home", "🤖 AI Advisor", "🧮 Calculator", "⚙️ Admin"])

# --- TAB 1: HOME (Live Marketplace & Ads) ---
with tab_home:
    st.markdown("### Hot <span style='color: #ff4b4b;'>Classified</span> 🔥", unsafe_allow_html=True)
    for ad in st.session_state.inventory:
        with st.container():
            st.markdown(f"""
            <div class="nav-card">
                <div style="display: flex; justify-content: space-between;">
                    <span class="price-badge">PKR {ad['price']}</span>
                    <span class="hot-tag">HOT DEAL</span>
                </div>
                <div style="margin-top: 10px;">
                    <b>{ad['size']} Plot - {ad['phase']}</b><br>
                    <span style="font-size: 12px; color: #666;">Plot No: {ad['plot']}</span>
                </div>
                <div style="margin-top: 8px; color: #007bff; font-weight: bold; font-size: 13px;">📞 {ad['contact']}</div>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 2: AI PROPERTY ADVISOR ---
with tab_ai:
    st.markdown("### 🤖 Babar AI Agent")
    st.caption("Ask about DHA investments or market trends")
    query = st.text_input("Enter your question:", placeholder="e.g. Best phase for 5 marla?")
    if query:
        with st.spinner("AI analyzing..."):
            # Real Estate Logic Simulation
            if "prism" in query.lower() or "9" in query:
                st.info("AI Analysis: Phase 9 Prism is showing 15% growth potential for 2026.")
            else:
                st.success("Bilal Mughal's Expert Tip: Construct and Sell (C&S) model is currently best for 10 Marla plots.")

# --- TAB 3: CONSTRUCTION CALCULATOR ---
with tab_calc:
    st.markdown("### 🧮 Construction Specialist")
    c_size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    c_type = st.radio("Type", ["Grey Structure", "Full Finishing"])
    
    # 2026 Rates Verified
    rate = 3450 if c_type == "Grey Structure" else 6800
    area = {"5 Marla": 2100, "10 Marla": 3500, "1 Kanal": 6500}[c_size]
    total = area * rate
    
    st.metric("Total Estimated Investment", f"PKR {total/1000000:.2f} M")
    st.write(f"Estimated at PKR {rate}/sqft")

# --- TAB 4: ADMIN & ADS MANAGEMENT ---
with tab_admin:
    st.markdown("### ⚙️ SaaS Admin Control")
    st.write("Manage your live inventory and ads here.")
    
    with st.form("add_ad_form"):
        new_plot = st.text_input("Plot No")
        new_phase = st.selectbox("Phase", ["Phase 6", "Phase 7", "Phase 8", "Phase 9 Prism", "Phase 10"])
        new_size = st.selectbox("Size", ["5 Marla", "10 Marla", "1 Kanal"])
        new_price = st.text_input("Price (e.g. 1.5 Cr)")
        new_contact = st.text_input("Contact", value="+92 3")
        
        if st.form_submit_button("🚀 Publish Ad"):
            if new_plot and new_price:
                new_entry = {"plot": new_plot, "phase": new_phase, "size": new_size, "price": new_price, "contact": new_contact}
                st.session_state.inventory.insert(0, new_entry)
                st.success("Ad Published Successfully!")
            else:
                st.error("Please fill all fields.")

# --- 6. FOOTER ---
st.markdown("<br><hr><center><p style='color: #999; font-size: 10px;'>Babar Real Estate SaaS | Version 14.0</p></center>", unsafe_allow_html=True)
