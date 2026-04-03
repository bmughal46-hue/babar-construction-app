import streamlit as st
import pandas as pd
import os
import plotly.express as px
from streamlit_folium import folium_static
import folium

# --- 1. CONFIG & STYLING ---
st.set_page_config(page_title="Babar Real Estate | All Pakistan DHA", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #0b5394 100%);
        color: white; padding: 40px; text-align: center;
        border-radius: 0 0 35px 35px; border-bottom: 6px solid #c5a059;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 5px solid #c5a059;
        text-align: center; margin-bottom: 10px;
    }
    .whatsapp-btn {
        background-color: #25D366; color: white; padding: 12px;
        text-decoration: none; border-radius: 8px; font-weight: bold;
        display: block; text-align: center; margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR (CEO Branding & Global Filters) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='text-align:center; color:white;'><b>Bilal Mughal</b><br>DHA Specialist (All Pakistan)</p>", unsafe_allow_html=True)
    
    whatsapp_url = "https://wa.me/923001234567" # Apna number yahan likhein
    st.markdown(f'<a href="{whatsapp_url}" class="whatsapp-btn">💬 WhatsApp Inquiry</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    selected_city = st.selectbox("Select City", ["Lahore", "Multan", "Bahawalpur", "Gujranwala", "Quetta"])
    
    if selected_city == "Lahore":
        phases = [f"Phase {i}" for i in range(1, 14)] + ["Broadway", "Prism"]
    else:
        phases = ["All Sectors", "Files Only", "Possession Plots"]
        
    st.selectbox("Select Phase/Sector", phases)

# --- 3. TOP HEADER ---
st.markdown(f"""
<div class='main-header'>
    <h1 style='margin:0; font-size:45px;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059; font-size:18px; letter-spacing:3px;'>SPECIALIZED IN DHA {selected_city.upper()} & NATIONWIDE</p>
</div>
""", unsafe_allow_html=True)

# --- 4. MAIN DASHBOARD ---
st.write("<br>", unsafe_allow_html=True)
t1, t2, t3 = st.tabs(["📋 Nationwide Inventory", "📍 Map Locator", "📊 Market Analysis"])

with t1:
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("<div class='stat-card'><h4>DHA Lahore</h4><h2>Phase 1-13</h2></div>", unsafe_allow_html=True)
    with col2: st.markdown("<div class='stat-card'><h4>DHA Multan</h4><h2>All Sectors</h2></div>", unsafe_allow_html=True)
    with col3: st.markdown("<div class='stat-card'><h4>DHA Quetta</h4><h2>Smart City</h2></div>", unsafe_allow_html=True)
    with col4: st.markdown("<div class='stat-card'><h4>DHA G.Wala</h4><h2>Active</h2></div>", unsafe_allow_html=True)
    
    st.subheader(f"🔥 Hot Deals in DHA {selected_city}")
    # Sample Data based on your nationwide coverage
    all_data = {
        'City': ['Lahore', 'Multan', 'Bahawalpur', 'Gujranwala', 'Quetta'],
        'Project': ['Phase 8 Broadway', 'Sector M', 'Phase 1', 'Commercial Area', 'Early Bird'],
        'Size': ['4 Marla', '1 Kanal', '10 Marla', '8 Marla', '1 Kanal File'],
        'Status': ['Possession', 'Allocation', 'Vanguard', 'Trading', 'Open File']
    }
    st.table(pd.DataFrame(all_data))

with t2:
    st.subheader(f"📍 Location Overview: DHA {selected_city}")
    # Coordinates change based on city selection
    city_coords = {
        "Lahore": [31.4697, 74.4500],
        "Multan": [30.2858, 71.5300],
        "Bahawalpur": [29.3550, 71.6911],
        "Gujranwala": [32.1024, 74.1900],
        "Quetta": [30.2500, 66.9500]
    }
    m = folium.Map(location=city_coords[selected_city], zoom_start=12)
    folium.Marker(city_coords[selected_city], popup=f"DHA {selected_city} Center").add_to(m)
    folium_static(m)

with t3:
    st.subheader("📈 Nationwide Investment Growth")
    trend_df = pd.DataFrame({
        'Project': ['Lahore P9', 'Multan', 'Bahawalpur', 'Quetta'],
        'Yearly Growth %': [22, 15, 12, 18]
    })
    fig = px.bar(trend_df, x='Project', y='Yearly Growth %', color='Project', title="ROI Comparison")
    st.plotly_chart(fig, use_container_width=True)

# --- 5. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>All Pakistan DHA Property Consultants | Serving Lahore, Multan, Bahawalpur, Gujranwala & Quetta</p>", unsafe_allow_html=True)
