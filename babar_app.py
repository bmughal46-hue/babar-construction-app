[2:46 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from PIL import Image
import os
from fpdf import FPDF
import urllib.parse

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate | CEO Bilal Mughal", layout="wide")

# --- 2. PREMIUM CSS (Zameen Style) ---
st.markdown("""
<style>
    .main-header { background-color: #003366; color: white; padding: 30px; text-align: center; border-radius: 0 0 30px 30px; border-bottom: 5px solid #c5a059; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #f8f9fa; border-radius: 5px; padding: 10px 20px; }
    .property-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0…
[2:59 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import os
from PIL import Image

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# --- 2. LOGO & PROFILE (Jo aapne upload ki hain) ---
with st.sidebar:
    st.header("CEO Portal")
    # Aapki picture wali file ka naam
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    if os.path.exists(profile_img):
        st.image(profile_img, caption="Bilal Mughal", width=200)
    
    # Dusri image (agar logo hai)
    logo_img = "images.jpeg"
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)
    
    st.info("Babar Real Estate | DHA Phase 8 Lahore")

# --- 3. MAIN DASHBOARD ---
st.markdown("<h1 style='text-align: center; color: #003366;'>BABAR REAL ESTATE</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
col1.metric("Active Listings", "1,240")
col2.metric("ROI Potential", "18.5%")

st.subheader("Market Inventory")
data = {
    'Area': ['Phase 9 Prism', 'Phase 8 Broadway', 'Phase 7'],
    'Price': ['3.35 Crore', '7.50 Crore', '1.85 Crore']
}
st.table(pd.DataFrame(data))

st.success("App is now running perfectly with your photos!")
