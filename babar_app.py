import streamlit as st
import pandas as pd
import os
import plotly.express as px

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f4f7f9; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #004080 100%);
        color: white; padding: 35px; text-align: center;
        border-radius: 0 0 25px 25px; border-bottom: 5px solid #c5a059;
        margin-bottom: 30px;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-top: 5px solid #c5a059;
        text-align: center;
    }
    [data-testid="stSidebar"] { background-color: #002e5b; border-right: 3px solid #c5a059; }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (CEO Profile) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='color:white; text-align:center;'><b>Bilal Mughal</b><br>Real Estate Consultant</p>", unsafe_allow_html=True)
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)

# --- 3. TOP HEADER ---
st.markdown("""
<div class='main-header'>
    <h1 style='margin:0;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059; letter-spacing:2px;'>DHA LAHORE PROPERTY SPECIALIST</p>
</div>
""", unsafe_allow_html=True)

# --- 4. ANALYTICS TABS ---
tab1, tab2 = st.tabs(["📊 Market Dashboard", "📉 Price Trends"])

with tab1:
    # Stats row
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='stat-card'><h3>Listings</h3><h2>1,240</h2><p style='color:green;'>+5%</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='stat-card'><h3>ROI</h3><h2>18.5%</h2><p style='color:blue;'>High</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='stat-card'><h3>Buyers</h3><h2>480+</h2><p style='color:orange;'>Active</p></div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    st.subheader("🏠 Featured Inventory")
    inv_df = pd.DataFrame({
        'Property': ['Phase 8 Broadway', 'Phase 9 Prism', 'Phase 7 Sector Z', 'Phase 6 Commercial'],
        'Size': ['4 Marla', '1 Kanal', '10 Marla', '8 Marla'],
        'Demand': ['8.50 Crore', '3.35 Crore', '1.85 Crore', '12.40 Crore']
    })
    st.table(inv_df)

with tab2:
    st.subheader("📈 DHA Price Index (Last 6 Months)")
    # Sample data for visualization
    trend_data = pd.DataFrame({
        'Month': ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'],
        'Price (Crore)': [2.1, 2.3, 2.2, 2.5, 2.9, 3.35]
    })
    fig = px.line(trend_data, x='Month', y='Price (Crore)', title='Phase 9 Prism 1 Kanal Trend')
    st.plotly_chart(fig, use_container_width=True)

# --- 5. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>© 2026 Babar Real Estate | DHA Broadway Lahore</p>", unsafe_allow_html=True)
