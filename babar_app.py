import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="Babar Real Estate | Official", layout="wide")

# --- 2. DATABASE (Lahore Phases & Blocks) ---
all_dha_data = {
    "Lahore": {
        "Phase 1": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L", "Block M", "Block N", "Block P"],
        "Phase 2": ["Block J", "Block K", "Block L", "Block M", "Block N", "Block P", "Block Q", "Block R", "Block S", "Block T"],
        "Phase 3": ["Block W", "Block X", "Block Y", "Block Z"],
        "Phase 4": ["Block AA", "Block BB", "Block CC", "Block DD", "Block EE", "Block FF", "Block GG"],
        "Phase 5": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L", "Block M"],
        "Phase 6": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L"],
        "Phase 7": ["Block P", "Block Q", "Block R", "Block S", "Block T", "Block U", "Block V", "Block W", "Block X", "Block Y", "Block Z"],
        "Phase 8": ["Block S", "Block T", "Block U", "Block V", "Block W", "Block X", "Block Y", "Ivy Green", "Ex-Air Avenue"],
        "Phase 8 Broadway": ["Sector A", "Sector B", "Sector C", "Sector D", "Plaza C-116"],
        "Phase 9 Prism": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L", "Block M", "Block N", "Block P", "Block Q", "Block R"],
        "Phase 9 Town": ["Block A", "Block B", "Block C", "Block D", "Block E"],
        "Phase 10": ["Sector A", "Sector B", "Sector C"],
        "Phase 11 (Rahbar)": ["Halloki Garden", "Phase 1", "Phase 2", "Phase 3"],
        "Phase 12 (EME)": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J"],
        "Phase 13": ["Sector 1", "Sector 2", "Sector 3", "Sector 4", "Sector 5"]
    },
    "Multan": {"Phase 1": ["Sector A", "Sector B", "Sector M", "Sector V"]},
    "Quetta": {"Smart City": ["Early Bird", "Sector A"]}
}

# --- 3. SIDEBAR (CEO Branding) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    st.markdown("<p style='text-align:center; color:white;'><b>Babar Mughal</b><br>CEO & Founder</p>", unsafe_allow_html=True)
    st.markdown(f'<a href="https://wa.me/923244000041" style="background-color:#25D366; color:white; padding:10px; text-decoration:none; border-radius:8px; display:block; text-align:center;">💬 WhatsApp: 0324-4000041</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    selected_city = st.selectbox("Select City", list(all_dha_data.keys()))
    selected_phase = st.selectbox(f"Select Phase", list(all_dha_data[selected_city].keys()))
    selected_block = st.selectbox(f"Select Block", all_dha_data[selected_city][selected_phase])

# --- 4. TOP BANNER (From Old Design) ---
st.markdown(f"""
<div style='background-color:#002e5b; color:white; padding:30px; text-align:center; border-radius:0 0 20px 20px; border-bottom: 5px solid #c5a059;'>
    <h1 style='margin:0;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059;'>DHA LAHORE PROPERTY SPECIALIST</p>
</div>
""", unsafe_allow_html=True)

# --- 5. MAIN DASHBOARD TABS (Connects Old & New) ---
tab1, tab2, tab3 = st.tabs(["📊 Market Overview", "📋 Live Inventory", "📍 Map View"])

with tab1:
    # Purana Stats Section
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Active Listings", "1,240", "+12 Today")
    with col2: st.metric("ROI Potential", "18.5%", "High Growth")
    with col3: st.metric("Verified Buyers", "480+", "DHA Certified")
    
    # Purana Bar Chart
    st.subheader("Investment Trends")
    trend_df = pd.DataFrame({'Area': ['Phase 8', 'Phase 9', 'Prism', 'Broadway'], 'ROI %': [15, 18, 22, 12]})
    fig = px.bar(trend_df, x='Area', y='ROI %', color='Area')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Naya Drill-down Inventory Section
    st.header(f"💎 Inventory: {selected_phase} ({selected_block})")
    plots_df = pd.DataFrame({
        'Plot Number': ['12', '45', '109', '500'],
        'Size': ['1 Kanal', '10 Marla', '1 Kanal', '5 Marla'],
        'Category': ['Residential', 'Residential', 'Commercial', 'Residential'],
        'Price': ['3.40 Crore', '1.80 Crore', '9.20 Crore', '1.15 Crore']
    })
    st.table(plots_df)

with tab3:
    st.info("Interactive Map Loading... (DHA Phase 8 Broadway Focus)")
    st.markdown("📍 *Office Location:* Plaza No. C-116, DHA Phase 8 Broadway, Lahore")

# --- 6. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>© 2026 Babar Real Estate | Serving All Pakistan DHA</p>", unsafe_allow_html=True)
