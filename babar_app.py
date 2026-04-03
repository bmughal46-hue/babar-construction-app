import streamlit as st
import pandas as pd
import os
import plotly.express as px
from streamlit_folium import folium_static
import folium

# --- 1. CONFIG & STYLING ---
st.set_page_config(page_title="Babar Real Estate | DHA Lahore Specialist", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #004080 100%);
        color: white; padding: 40px; text-align: center;
        border-radius: 0 0 30px 30px; border-bottom: 6px solid #c5a059;
    }
    .stat-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.05); border-top: 5px solid #c5a059;
        text-align: center;
    }
    [data-testid="stSidebar"] { background-color: #002e5b; border-right: 4px solid #c5a059; }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (CEO Branding) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    # Aapki files ke names
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='color:white; text-align:center;'><b>Bilal Mughal</b><br>Real Estate Expert</p>", unsafe_allow_html=True)
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)
    
    st.markdown("---")
    st.subheader("🔍 Fast Search")
    st.selectbox("Select Phase", ["DHA Phase 8 Broadway", "DHA Phase 9 Prism", "DHA Phase 7"])

# --- 3. TOP HEADER ---
st.markdown("""
<div class='main-header'>
    <h1 style='margin:0; font-size:50px;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059; letter-spacing:3px;'>DHA LAHORE PROPERTY SPECIALIST</p>
</div>
""", unsafe_allow_html=True)

# --- 4. DASHBOARD TABS ---
st.write("<br>", unsafe_allow_html=True)
tab1, tab2, tab3 = st.tabs(["🏛 Inventory", "📍 Area Map", "📈 Market Trends"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='stat-card'><h3>Listings</h3><h2>1,240</h2><p style='color:green;'>+12 Today</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='stat-card'><h3>ROI</h3><h2>18.5%</h2><p style='color:blue;'>High</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='stat-card'><h3>Active</h3><h2>480+</h2><p style='color:orange;'>Buyers</p></div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    st.subheader("🏠 Featured Inventory")
    inv_df = pd.DataFrame({
        'Location': ['Phase 8 Broadway', 'Phase 9 Prism', 'Phase 7 Sector Z', 'Phase 6'],
        'Size': ['4 Marla Commercial', '1 Kanal Residential', '10 Marla', '2 Kanal'],
        'Price': ['8.50 Crore', '3.35 Crore', '1.85 Crore', '14.2 Crore']
    })
    st.table(inv_df)

with tab2:
    st.subheader("📍 DHA Lahore Hotspots")
    # Broadway Location Map
    m = folium.Map(location=[31.4697, 74.4500], zoom_start=12)
    folium.Marker([31.4725, 74.4695], popup="Babar Real Estate - Broadway").add_to(m)
    folium_static(m)

with tab3:
    st.subheader("📉 Pricing Trend Analysis")
    trend = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Value': [2.8, 3.1, 3.35, 3.5]
    })
    fig = px.area(trend, x='Month', y='Value', title="Phase 9 Prism Price Growth")
    st.plotly_chart(fig, use_container_width=True)

# --- 5. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>© 2026 Babar Real Estate | Lahore, Pakistan</p>", unsafe_allow_html=True)
