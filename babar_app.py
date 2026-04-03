import streamlit as st
import pandas as pd
import os
import plotly.express as px
from streamlit_folium import folium_static
import folium

# --- 1. CONFIG & STYLING ---
st.set_page_config(page_title="Babar Real Estate | DHA Specialist", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #0b5394 100%);
        color: white; padding: 40px; text-align: center;
        border-radius: 0 0 35px 35px; border-bottom: 6px solid #c5a059;
    }
    .footer-box {
        background-color: #002e5b; color: white; padding: 20px;
        border-radius: 15px; margin-top: 30px; text-align: center;
        border-top: 4px solid #c5a059;
    }
    .whatsapp-btn {
        background-color: #25D366; color: white; padding: 12px;
        text-decoration: none; border-radius: 8px; font-weight: bold;
        display: block; text-align: center; margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (CEO Branding & Smart Filters) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='text-align:center; color:white; font-size:18px;'><b>Babar Mughal</b><br>CEO & Founder</p>", unsafe_allow_html=True)
    
    # Official WhatsApp
    whatsapp_url = "https://wa.me/923244000041"
    st.markdown(f'<a href="{whatsapp_url}" class="whatsapp-btn">💬 Chat on WhatsApp</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🔍 Property Finder")
    city = st.selectbox("Select City", ["Lahore", "Multan", "Bahawalpur", "Gujranwala", "Quetta"])
    
    # Phase Selection
    if city == "Lahore":
        phase = st.selectbox("Select Phase", [f"Phase {i}" for i in range(1, 14)] + ["Broadway", "Prism"])
        block = st.selectbox("Select Block", ["Block A", "Block B", "Block C", "Commercial Broadway"])
    else:
        phase = st.selectbox("Select Sector", ["Sector A", "Sector B", "Sector C", "Files"])
        block = st.selectbox("Select Category", ["1 Kanal", "10 Marla", "5 Marla", "Commercial"])

# --- 3. TOP HEADER ---
st.markdown(f"""
<div class='main-header'>
    <h1 style='margin:0; font-size:45px;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059; font-size:18px; letter-spacing:3px;'>OFFICIAL DEALER: DHA {city.upper()} & NATIONWIDE</p>
</div>
""", unsafe_allow_html=True)

# --- 4. MAIN CONTENT ---
st.write("<br>", unsafe_allow_html=True)
t1, t2, t3 = st.tabs(["📋 Inventory", "📍 Map View", "📊 Trends"])

with t1:
    st.subheader(f"Available Plots: {city} {phase} ({block})")
    # Sample Drill-down Data
    sample_data = pd.DataFrame({
        'Plot No': ['101', '55-C', '12', '99/1'],
        'Type': ['Residential', 'Residential', 'Commercial', 'Residential'],
        'Price': ['3.45 Crore', '1.90 Crore', '8.50 Crore', '2.15 Crore'],
        'Status': ['Direct Deal', 'Available', 'Hot Listing', 'Available']
    })
    st.dataframe(sample_data, use_container_width=True)

with t2:
    st.subheader("Strategic Location Map")
    m = folium.Map(location=[31.4697, 74.4500], zoom_start=12)
    # Broadway Office Marker
    folium.Marker([31.4725, 74.4695], popup="Babar Real Estate - Plaza C-116", tooltip="Broadway Office").add_to(m)
    folium_static(m)

with t3:
    st.subheader("Investment Growth Analysis")
    trend_df = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Growth': [10, 15, 18, 22]})
    fig = px.area(trend_df, x='Month', y='Growth', title="Market Momentum")
    st.plotly_chart(fig, use_container_width=True)

# --- 5. OFFICIAL FOOTER (With Address) ---
st.markdown(f"""
<div class='footer-box'>
    <p><b>📍 Address:</b> DHA Phase 8 Broadway, Plaza No. C-116, Lahore, Pakistan</p>
    <p><b>📞 WhatsApp:</b> +92 324 4000041 | <b>✉ CEO:</b> Babar Mughal</p>
    <p style='font-size:12px; color:#ccc;'>© 2026 Babar Real Estate | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
