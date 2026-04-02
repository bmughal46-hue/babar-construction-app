import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import openai

# --- 1. CONFIG & BRANDING ---
st.set_page_config(page_title="Babar Real Estate | CEO Bilal Mughal", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .stApp { max-width: 500px; margin: 0 auto; background: #f8f9fa; border-right: 1px solid #ddd; }
    .header-main { background: #003366; color: white; padding: 20px; text-align: center; border-radius: 0 0 25px 25px; }
    .whatsapp-bar { position: fixed; bottom: 0; width: 100%; max-width: 500px; background: #25D366; color: white; text-align: center; padding: 12px; font-weight: bold; z-index: 1000; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("""
    <div class='header-main'>
        <h2 style='margin:0;'>BABAR REAL ESTATE</h2>
        <p style='font-size:12px; margin:0;'>C-116, Broadway Plaza, DHA Phase 8, Lahore</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. NAVIGATION ---
tab_dash, tab_maps, tab_ai, tab_calc, tab_admin = st.tabs(["🏡 Dash", "📍 Maps", "🤖 AI", "🧮 Calc", "⚙️ Admin"])

# --- TAB 1: DASHBOARD ---
with tab_dash:
    st.subheader("Real-Time Market Metrics 🚀")
    col1, col2 = st.columns(2)
    col1.metric("Active Listings", "1,240", "↑ 12")
    col2.metric("ROI Potential", "18.5%", "High")
    
    st.markdown("---")
    st.write("### Recent Hot Listings 🔥")
    # Sample Data for Display
    st.info("Phase 9 Prism | 1 Kanal | 3.30 Crore")
    st.info("Phase 7 Sector Z | 10 Marla | 1.85 Crore")

# --- TAB 2: MAPS ---
with tab_maps:
    st.subheader("🗺️ Interactive DHA Map")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=13)
    folium.Marker([31.4697, 74.4534], popup="Babar Real Estate Office").add_to(m)
    st_folium(m, width=450, height=350)

# --- TAB 3: AI ADVISOR ---
with tab_ai:
    st.subheader("🤖 AI Property Advisor")
    query = st.text_input("Investement ke bare mein pochein:")
    if query:
        st.success(f"Bilal Mughal's AI Insight: '{query}' ke mutabiq Phase 8 Broadway mein commercial ROI 20% tak ja sakti hai.")

# --- TAB 4: CALCULATOR (BILL GENERATOR) ---
with tab_calc:
    st.subheader("🧮 Smart Bill Generator")
    size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    rate = st.number_input("Current Rate (PKR/sqft)", value=3450)
    area = {"5 Marla": 1950, "10 Marla": 3300, "1 Kanal": 5500}[size]
    total = area * rate
    
    st.markdown(f"""
    <div style='border:2px dashed #333; padding:20px; background:white;'>
        <h3 style='text-align:center;'>BABAR REAL ESTATE</h3>
        <p><b>Plot:</b> {size}</p>
        <p><b>Area:</b> {area} sqft</p>
        <hr>
        <h3 style='text-align:right; color:#28a745;'>Total: PKR {total:,.0f}</h3>
    </div>
    """, unsafe_allow_html=True)
    st.caption("📸 Screenshot le kar share karein.")

# --- TAB 5: ADMIN ---
with tab_admin:
    st.subheader("⚙️ Admin Control Panel")
    pwd = st.text_input("Admin Password", type="password")
    if pwd == "babar123":
        st.success("Welcome, CEO Bilal Mughal")
        st.file_uploader("Upload New DHA CSV Data")
    else:
        st.warning("Password required to access management.")

# --- FOOTER ---
st.markdown("""
    <div class='whatsapp-bar'>
        <a href='https://wa.me/923244000041' style='color:white; text-decoration:none;'>
            WhatsApp: Babar Mughal (+92 324 4000041)
        </a>
    </div>
    """, unsafe_allow_html=True)
