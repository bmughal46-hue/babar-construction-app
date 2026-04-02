import streamlit as st
import pandas as pd
import os
from PIL import Image

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# --- 2. PROFESSIONAL CSS (Dark Blue & Gold Theme) ---
st.markdown("""
<style>
    /* Main Background */
    .stApp { background-color: #f4f7f9; }
    
    /* Top Navigation Header */
    .nav-header {
        background-color: #002e5b;
        color: #ffffff;
        padding: 20px;
        text-align: center;
        border-bottom: 5px solid #c5a059;
        border-radius: 0 0 20px 20px;
        margin-bottom: 30px;
    }
    
    /* Metrics Cards */
    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-top: 5px solid #c5a059;
        text-align: center;
    }
    .metric-card h2 { color: #002e5b; font-size: 35px; margin: 10px 0; }
    .metric-card p { color: #666; font-weight: bold; }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #002e5b;
        color: white;
        border-right: 3px solid #c5a059;
    }
    
    /* Property Table Styling */
    .stDataFrame {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (CEO & LOGO) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    # Profile & Logo Handling
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("---")
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)
    
    st.info("Authorized DHA Phase 8 Specialist\nLahore, Pakistan")

# --- 4. TOP HEADER ---
st.markdown("""
<div class='nav-header'>
    <h1 style='margin:0; font-size:45px;'>BABAR REAL ESTATE</h1>
    <p style='margin:0; color:#c5a059; letter-spacing: 2px;'>TRUSTED PARTNER IN DHA LAHORE</p>
</div>
""", unsafe_allow_html=True)

# --- 5. DASHBOARD METRICS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card'><p>Active Listings</p><h2>1,240</h2><span style='color:green;'>+12 Today</span></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'><p>ROI Potential</p><h2>18.5%</h2><span style='color:blue;'>High Growth</span></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'><p>Market Status</p><h2>Active</h2><span style='color:orange;'>Trending</span></div>", unsafe_allow_html=True)

# --- 6. MARKET LISTINGS TABLE ---
st.write("---")
st.markdown("### 🏠 Current Market Hot-Deals")

inventory = {
    'Area': ['DHA Phase 9 Prism', 'DHA Phase 8 Broadway', 'DHA Phase 7 Sector Z', 'DHA Phase 6'],
    'Size': ['1 Kanal', '1 Kanal', '10 Marla', '2 Kanal'],
    'Price (PKR)': ['3.35 Crore', '7.50 Crore', '1.85 Crore', '14.20 Crore'],
    'Status': ['Hot Deal', 'Commercial', 'Ready to Build', 'Investment']
}

df = pd.DataFrame(inventory)
st.table(df)

# --- 7. FOOTER ---
st.write("---")
st.markdown("""
<div style='text-align:center; padding:20px;'>
    <p style='color:#888;'>© 2026 Babar Real Estate | Premium Property Solutions</p>
    <p style='font-size:12px; color:#aaa;'>Developed for High Command Business Operations</p>
</div>
""", unsafe_allow_html=True)
