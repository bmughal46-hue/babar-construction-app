import streamlit as st
import pandas as pd
import os

# --- 1. ALL PAKISTAN DHA DATABASE (Google & Official Data) ---
# Lahore, Multan, Bahawalpur, Gujranwala, Quetta ke saare blocks
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
    "Multan": {
        "All Sectors": ["Sector A", "Sector B", "Sector C", "Sector D", "Sector E", "Sector F", "Sector G", "Sector H", "Sector I", "Sector K", "Sector L", "Sector M", "Sector N", "Sector P", "Sector Q", "Sector R", "Sector S", "Sector T", "Sector U", "Sector V", "Sector W", "Sector X", "Sector Y"]
    },
    "Bahawalpur": {
        "Phase 1": ["Sector A", "Sector B", "Sector C", "Sector D", "Sector E", "Sector F", "Sector G", "Sector H", "Sector J"]
    },
    "Gujranwala": {
        "Phase 1": ["Sector A", "Sector B", "Sector C", "Sector D", "Sector E", "Sector G", "Sector K", "Sector L", "Sector M"]
    },
    "Quetta": {
        "Smart City": ["Sector A", "Sector B", "Sector C", "Early Bird", "Marketing Block"]
    }
}

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>Babar Real Estate</h2>", unsafe_allow_html=True)
    
    # User Profile
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='text-align:center; color:white;'><b>Babar Mughal</b><br>CEO & Founder</p>", unsafe_allow_html=True)
    
    # WhatsApp Direct
    st.markdown(f'<a href="https://wa.me/923244000041" style="background-color:#25D366; color:white; padding:10px; text-decoration:none; border-radius:8px; display:block; text-align:center;">💬 WhatsApp: 0324-4000041</a>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🎯 Property Filter")
    
    # Step 1: Select City
    selected_city = st.selectbox("Select City", list(all_dha_data.keys()))
    
    # Step 2: Select Phase (Based on City)
    city_phases = all_dha_data[selected_city]
    selected_phase = st.selectbox(f"Select Phase in {selected_city}", list(city_phases.keys()))
    
    # Step 3: Select Block (Based on Phase)
    available_blocks = city_phases[selected_phase]
    selected_block = st.selectbox(f"Select Block", available_blocks)

# --- 3. MAIN INTERFACE ---
st.markdown(f"""
<div style='background-color:#002e5b; color:white; padding:30px; text-align:center; border-radius:0 0 20px 20px; border-bottom: 5px solid #c5a059;'>
    <h1>DHA {selected_city.upper()} PORTAL</h1>
    <p>Viewing {selected_phase} > {selected_block}</p>
</div>
""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# Plot Listing Section
st.header(f"💎 Available Inventory in {selected_block}")
# Sample inventory for each block
plots_df = pd.DataFrame({
    'Plot Number': ['12', '45', '109', '500'],
    'Size': ['1 Kanal', '10 Marla', '1 Kanal', '5 Marla'],
    'Category': ['Residential', 'Residential', 'Commercial', 'Residential'],
    'Price': ['3.40 Crore', '1.80 Crore', '9.20 Crore', '1.15 Crore']
})
st.table(plots_df)

# --- 4. OFFICE FOOTER ---
st.markdown(f"""
<div style='background-color:#eee; padding:20px; border-radius:15px; margin-top:50px; border-left: 10px solid #002e5b;'>
    <h3>📍 Head Office</h3>
    <p><b>Babar Real Estate</b><br>
    Plaza No. C-116, DHA Phase 8 Broadway, Lahore.<br>
    <b>CEO:</b> Babar Mughal | <b>Contact:</b> 0324-4000041</p>
</div>
""", unsafe_allow_html=True)
