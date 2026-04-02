import streamlit as st
import pandas as pd
import os
from PIL import Image

# --- 1. CONFIG (Naam change kar diya) ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# --- 2. LOGO & PROFILE LOADING ---
with st.sidebar:
    st.header("Babar Real Estate")
    # Jo images aapne bahar upload ki hain
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, width=200)
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)
    
    st.info("DHA Phase 8, Lahore | Broadway Specialist")

# --- 3. MAIN HEADER ---
st.markdown("<h1 style='text-align: center; color: #003366;'>BABAR REAL ESTATE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your Trusted Partner in DHA Lahore</p>", unsafe_allow_html=True)

# --- 4. DASHBOARD METRICS ---
col1, col2 = st.columns(2)
col1.metric("Active Listings", "1,240")
col2.metric("ROI Potential", "18.5%")

# --- 5. INVENTORY TABLE ---
st.write("---")
st.subheader("Current Market Hot-Deals")
inventory = {
    'Area': ['Phase 9 Prism', 'Phase 8 Broadway', 'Phase 7 Sector Z'],
    'Size': ['1 Kanal', '1 Kanal', '10 Marla'],
    'Price': ['3.35 Crore', '7.50 Crore', '1.85 Crore']
}
st.table(pd.DataFrame(inventory))

# Footer
st.write("---")
st.caption("© 2026 Babar Real Estate | Digital Portal")
