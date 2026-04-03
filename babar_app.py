import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Babar Real Estate & Construction", layout="wide")

# --- 2. DATA (Construction Material Logic) ---
material_per_marla = {
    "Bricks": 4500, "Cement": 90, "Steel": 0.4, "Bajri": 90
}

# --- 3. SIDEBAR (CEO Branding) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg" #
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    st.markdown("<p style='text-align:center; color:white;'><b>Bilal Mughal</b><br>CEO & Founder</p>", unsafe_allow_html=True) #
    st.markdown(f'<a href="https://wa.me/923244000041" style="background-color:#25D366; color:white; padding:10px; text-decoration:none; border-radius:8px; display:block; text-align:center;">💬 WhatsApp Support</a>', unsafe_allow_html=True)

# --- 4. TOP HEADER ---
st.markdown("""
<div style='background-color:#002e5b; color:white; padding:30px; text-align:center; border-radius:0 0 20px 20px; border-bottom: 5px solid #c5a059;'>
    <h1 style='margin:0;'>BABAR REAL ESTATE & CONSTRUCTION</h1>
    <p style='color:#c5a059;'>YOUR TRUSTED PARTNER IN DHA LAHORE</p>
</div>
""", unsafe_allow_html=True) #

# --- 5. MAIN INTERFACE TABS (Fixing the Error) ---
# Yahan humne 4 tabs define kar diye hain
tab1, tab2, tab3, tab4 = st.tabs(["📊 Market Overview", "📋 Live Inventory", "📍 Map View", "🏗️ Construction Calc"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Listings", "1,240", "+12 Today") #
    col2.metric("ROI Potential", "18.5%", "High Growth") #
    col3.metric("Verified Files", "480+", "DHA Certified") #

with tab2:
    st.subheader("Inventory Search (Connect with Zameen CSV soon)")
    st.info("Waiting for Excel Data...")

with tab3:
    st.markdown("### 📍 Interactive Map (Folium)")
    st.write("Office: Plaza No. C-116, DHA Phase 8 Broadway, Lahore")

with tab4:
    st.header("🏗️ Babar Construction Smart Estimator")
    p_size = st.selectbox("Select Plot Size", ["3 Marla", "5 Marla", "10 Marla", "1 Kanal", "2 Kanal", "4 Kanal Commercial"])
    
    # Calculation Logic
    marla_map = {"3 Marla": 3, "5 Marla": 5, "10 Marla": 10, "1 Kanal": 20, "2 Kanal": 40, "4 Kanal Commercial": 80}
    num_marlas = marla_map[p_size]
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bricks (Awal)", f"{int(num_marlas * 4500):,}")
    c2.metric("Cement Bags", f"{int(num_marlas * 90):,}")
    c3.metric("Steel (Tons)", f"{round(num_marlas * 0.4, 2)}")
    c4.metric("Bajri (Cft)", f"{int(num_marlas * 90):,}")

    st.markdown("---")
    st.subheader("🛡️ Quality Awareness: Recommended Brands")
    st.write("- *Steel:* Mughal Steel, Amreli Steel (Grade 60)")
    st.write("- *Cement:* Maple Leaf, Lucky Cement")
    st.write("- *Cables:* Pakistan Cables, Fast Cables")
