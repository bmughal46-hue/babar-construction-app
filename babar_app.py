import streamlit as st
import pandas as pd
import os

# --- 1. SETTINGS & THEME ---
st.set_page_config(page_title="Babar Real Estate | CEO Bilal Mughal", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    /* Top Header Bar */
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #004080 100%);
        color: white; padding: 40px; text-align: center;
        border-radius: 0 0 30px 30px; border-bottom: 6px solid #c5a059;
        margin-bottom: 40px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    /* Stats Cards */
    .stat-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08); border-top: 6px solid #c5a059;
        text-align: center; transition: transform 0.3s;
    }
    .stat-card:hover { transform: translateY(-5px); }
    .stat-card h2 { color: #002e5b; margin: 10px 0; font-size: 38px; }
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #002e5b; border-right: 4px solid #c5a059; }
    .sidebar-text { color: white; text-align: center; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (Professional CEO Profile) ---
with st.sidebar:
    st.markdown("<h2 class='sidebar-text'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    # Files handling for the specific names you uploaded
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p class='sidebar-text'>Bilal Mughal</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=160)
    
    st.markdown("---")
    # Interactive Search for Professionalism
    st.subheader("Quick Search")
    st.selectbox("Select Phase", ["DHA Phase 8", "DHA Phase 9 Prism", "DHA Phase 7", "DHA Phase 6"])
    st.slider("Budget (Crores)", 1, 20, (3, 8))

# --- 3. TOP NAVIGATION HEADER ---
st.markdown("""
<div class='main-header'>
    <h1 style='font-size: 50px; margin-bottom: 0;'>BABAR REAL ESTATE</h1>
    <p style='color: #c5a059; font-size: 20px; font-weight: 300; letter-spacing: 3px;'>THE AUTHORITY IN DHA LAHORE BROADWAY</p>
</div>
""", unsafe_allow_html=True)

# --- 4. DASHBOARD STATS ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='stat-card'><p style='color:#666;'>Market Inventory</p><h2>1,240</h2><p style='color:green; font-weight:bold;'>↑ 5% this month</p></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='stat-card'><p style='color:#666;'>Daily ROI Forecast</p><h2>18.5%</h2><p style='color:blue; font-weight:bold;'>Optimal Growth</p></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='stat-card'><p style='color:#666;'>Active Buyers</p><h2>480+</h2><p style='color:orange; font-weight:bold;'>Trending Now</p></div>", unsafe_allow_html=True)

# --- 5. PROPERTY LISTINGS TABLE ---
st.write("<br>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["💎 Hot Deals (DHA)", "📈 Market Trends"])

with tab1:
    st.markdown("### 🏠 Featured Broadway & Phase 9 Inventory")
    inventory_data = {
        'Property Details': ['Phase 8 Broadway Commercial', 'Phase 9 Prism Sector A', 'Phase 7 Sector Z', 'Phase 6 Commercial'],
        'Size': ['4 Marla', '1 Kanal', '10 Marla', '8 Marla'],
        'Demand (PKR)': ['8.50 Crore', '3.35 Crore', '1.85 Crore', '12.40 Crore'],
        'ROI Status': ['Extreme High', 'High', 'Moderate', 'Very High']
    }
    st.table(pd.DataFrame(inventory_data))

with tab2:
    st.markdown("### 📊 Market Value Analysis")
    st.line_chart(pd.DataFrame([1.2, 1.5, 1.8, 2.1, 2.8, 3.2, 3.5], columns=['Price Index (Crores)']))

# --- 6. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>© 2026 Babar Real Estate | Premium Real Estate Management Portal</p>", unsafe_allow_html=True)
