import streamlit as st
import pandas as pd
import os

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate | DHA Specialist", layout="wide")

# --- 2. PREMIUM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #004080 100%);
        color: white; padding: 40px; text-align: center;
        border-radius: 0 0 30px 30px; border-bottom: 6px solid #c5a059;
        margin-bottom: 30px;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border-top: 5px solid #c5a059;
        text-align: center;
    }
    .contact-box {
        background: #002e5b; color: white; padding: 20px;
        border-radius: 15px; border-left: 10px solid #c5a059;
    }
    [data-testid="stSidebar"] { background-color: #002e5b; border-right: 4px solid #c5a059; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (CEO Profile) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    # Using your uploaded files
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='color:white; text-align:center; font-weight:bold;'>Bilal Mughal</p>", unsafe_allow_html=True)
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)
    
    st.markdown("---")
    st.write("📞 *Contact:* +92 300 xxxxxxx")
    st.write("📍 *Office:* Phase 8 Broadway, Lahore")

# --- 4. TOP HEADER ---
st.markdown("""
<div class='main-header'>
    <h1 style='margin:0; font-size:48px;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059; font-size:18px; letter-spacing:2px;'>YOUR TRUSTED PARTNER IN DHA LAHORE</p>
</div>
""", unsafe_allow_html=True)

# --- 5. TOP METRICS ---
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("<div class='stat-card'><h3>Listings</h3><h2 style='color:#002e5b;'>1,240</h2><p style='color:green;'>+12 Today</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='stat-card'><h3>ROI Potential</h3><h2 style='color:#002e5b;'>18.5%</h2><p style='color:blue;'>High Growth</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown("<div class='stat-card'><h3>Active Buyers</h3><h2 style='color:#002e5b;'>480+</h2><p style='color:orange;'>Trending</p></div>", unsafe_allow_html=True)

# --- 6. PROPERTY & CONTACT SECTION ---
st.write("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("🏠 Featured Inventory")
    data = {
        'Property': ['Phase 8 Broadway', 'Phase 9 Prism', 'Phase 7 Sector Z', 'Phase 6 Commercial'],
        'Size': ['4 Marla', '1 Kanal', '10 Marla', '8 Marla'],
        'Demand': ['8.50 Crore', '3.35 Crore', '1.85 Crore', '12.40 Crore']
    }
    st.table(pd.DataFrame(data))

with col_right:
    st.markdown("<div class='contact-box'><h3>Inquiry Form</h3><p>Submit for call-back</p></div>", unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        interest = st.selectbox("Interest", ["Buying", "Selling", "Investment Advice"])
        submitted = st.form_submit_button("Send Request")
        if submitted:
            st.success("Request Sent! CEO Bilal Mughal will contact you.")

# --- 7. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>© 2026 Babar Real Estate | DHA Lahore Broadway Specialist</p>", unsafe_allow_html=True)
