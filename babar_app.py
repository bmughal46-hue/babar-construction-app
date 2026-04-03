import streamlit as st
import pandas as pd
import os

# --- 1. DATA DICTIONARY (Phases & Blocks) ---
# Yahan hum saara data connect kar rahe hain
dha_data = {
    "Phase 1": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L", "Block M", "Block N", "Block P"],
    "Phase 2": ["Block J", "Block K", "Block L", "Block M", "Block N", "Block P", "Block Q", "Block R", "Block S", "Block T"],
    "Phase 3": ["Block W", "Block X", "Block Y", "Block Z"],
    "Phase 4": ["Block AA", "Block BB", "Block CC", "Block DD", "Block EE", "Block FF", "Block GG"],
    "Phase 5": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L", "Block M"],
    "Phase 6": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L"],
    "Phase 7": ["Block P", "Block Q", "Block R", "Block S", "Block T", "Block U", "Block V", "Block W", "Block X", "Block Y", "Block Z"],
    "Phase 8": ["Block S", "Block T", "Block U", "Block V", "Block W", "Block X", "Block Y", "Ivy Green", "Ex-Air Avenue", "Park View"],
    "Broadway": ["Phase 8 Commercial", "CCA 1", "CCA 2", "Plaza C-116 Sector"],
    "Phase 9 Prism": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J", "Block K", "Block L", "Block M", "Block N", "Block P", "Block Q", "Block R"],
    "Phase 9 Town": ["Block A", "Block B", "Block C", "Block D", "Block E"],
    "Phase 10": ["Planning Stage", "Sector A", "Sector B"],
    "Phase 11 (Rahbar)": ["Phase 1", "Phase 2", "Phase 3", "Phase 4"],
    "Phase 12 (EME)": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block F", "Block G", "Block H", "Block J"],
    "Phase 13": ["Master Plan", "Sector 1", "Sector 2", "Sector 3"]
}

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    # User Branding
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='text-align:center; color:white;'><b>Babar Mughal</b><br>CEO & Founder</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("📍 Precise Location Selector")
    
    # 1. City (Lahore for now)
    city = "Lahore"
    
    # 2. Phase Selection
    selected_phase = st.selectbox("Select Phase", list(dha_data.keys()))
    
    # 3. Dynamic Block Selection (Connects data based on Phase)
    available_blocks = dha_data[selected_phase]
    selected_block = st.selectbox(f"Select Block in {selected_phase}", available_blocks)

# --- 3. MAIN DISPLAY ---
st.title(f"🏠 Babar Real Estate | {selected_phase} Specialist")
st.info(f"Currently viewing: *{selected_phase}* > *{selected_block}*")

# Statistics Section
c1, c2, c3 = st.columns(3)
with c1: st.metric("Market Status", "Hot", "+5%")
with c2: st.metric("Avg Price (1 Kanal)", "3.50 Cr", "Trending")
with c3: st.metric("Active Dealers", "480+", "Verified")

# Inventory Table (Placeholder for Plot Details)
st.subheader(f"Available Plots in {selected_block}")
sample_plots = pd.DataFrame({
    'Plot No': ['12', '45/A', '102-B', '500'],
    'Size': ['1 Kanal', '10 Marla', '1 Kanal', '5 Marla'],
    'Demand': ['3.40 Cr', '1.85 Cr', '3.55 Cr', '1.10 Cr'],
    'Contact': ['WhatsApp CEO', 'WhatsApp CEO', 'WhatsApp CEO', 'WhatsApp CEO']
})
st.dataframe(sample_plots, use_container_width=True)

# Contact Footer
st.markdown(f"""
<div style='background-color:#002e5b; color:white; padding:20px; border-radius:15px; text-align:center;'>
    <p><b>📍 Office:</b> Plaza No. C-116, DHA Phase 8 Broadway, Lahore</p>
    <p><b>📞 Contact Babar Mughal:</b> 0324-4000041</p>
</div>
""", unsafe_allow_html=True)
