[3:09 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import os
import plotly.express as px

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f4f7f9; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #004080 100%);
        color: white; padding: 35px; text-align: center;
        border-radius: 0 0 25px 25px; border-bottom: 5px solid #c5a059;
        margin-bottom: 30px;
    }
    .stat-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08); border-top: 5px solid #c5a059;
        text-align: center;
    }
    [data-testid="stSidebar"] { background-color: #002e5b; border-right: 3px …
[3:12 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import os
import plotly.express as px

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Real Estate | Premium Portal", layout="wide")

# --- 2. THEME & STYLING ---
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .main-header {
        background: linear-gradient(135deg, #002e5b 0%, #004080 100%);
        color: white; padding: 40px; text-align: center;
        border-radius: 0 0 30px 30px; border-bottom: 5px solid #c5a059;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .stat-card {
        background: white; padding: 25px; border-radius: 20px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.05); border-top: 5px solid #c5a059;
        text-align: center;
    }
    [data-testid="stSidebar"] { background-color: #002e5b; border-right: 4px solid #c5a059; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (CEO & Branding) ---
with st.sidebar:
    st.markdown("<h2 style='color:#c5a059; text-align:center;'>CEO PORTAL</h2>", unsafe_allow_html=True)
    
    # Files management based on your uploads
    profile_img = "3f4c835c-be62-407e-aa66-9aefc3ca48f5.jpg"
    logo_img = "images.jpeg"
    
    if os.path.exists(profile_img):
        st.image(profile_img, use_container_width=True)
    
    st.markdown("<p style='color:white; text-align:center;'><b>Bilal Mughal</b><br>Real Estate Consultant</p>", unsafe_allow_html=True)
    
    if os.path.exists(logo_img):
        st.image(logo_img, width=150)
    
    st.markdown("---")
    st.markdown("### 🔍 Property Search")
    st.selectbox("Category", ["Residential Plots", "Commercial Broadway", "Constructed Houses"])
    st.slider("Price Range (Crore)", 1.0, 50.0, (2.5, 15.0))

# --- 4. MAIN HEADER ---
st.markdown("""
<div class='main-header'>
    <h1 style='margin:0; font-size:55px;'>BABAR REAL ESTATE</h1>
    <p style='color:#c5a059; font-size:20px; letter-spacing:3px;'>THE AUTHORITY IN DHA LAHORE PROPERTIES</p>
</div>
""", unsafe_allow_html=True)

# --- 5. INTERACTIVE DASHBOARD ---
tab1, tab2, tab3 = st.tabs(["📊 Market Overview", "📌 Hot Listings", "📬 Direct Inquiry"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("<div class='stat-card'><h3>Listings</h3><h2 style='color:#002e5b;'>1,240</h2><p style='color:green;'>↑ 5%</p></div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='stat-card'><h3>ROI Forecast</h3><h2 style='color:#002e5b;'>18.5%</h2><p style='color:blue;'>High</p></div>", unsafe_allow_html=True)
    with c3: st.markdown("<div class='stat-card'><h3>Active Buyers</h3><h2 style='color:#002e5b;'>480+</h2><p style='color:orange;'>Trending</p></div>", unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    # Trend Chart
    trend_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Price Index': [2.8, 3.1, 3.35, 3.5]
    })
    fig = px.area(trend_data, x='Month', y='Price Index', title="DHA Lahore Phase 9 Prism Growth")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("🏠 Broadway & Phase 9 Top Picks")
    inventory = {
        'Location': ['Phase 8 Broadway', 'Phase 9 Prism Sector A', 'Phase 7 Sector Z', 'Phase 6 Main'],
        'Size': ['4 Marla Commercial', '1 Kanal Residential', '10 Marla Plot', '2 Kanal Corner'],
        'Demand': ['8.50 Crore', '3.35 Crore', '1.85 Crore', '14.2 Crore'],
        'Status': ['Hot', 'Best ROI', 'Ready', 'Premium']
    }
    st.table(pd.DataFrame(inventory))

with tab3:
    st.markdown("### 📧 Get Exclusive Investment Deals")
    with st.form("contact"):
        name = st.text_input("Full Name")
        phone = st.text_input("WhatsApp Number")
        msg = st.text_area("Your Requirement")
        if st.form_submit_button("Contact Bilal Mughal"):
            st.success("Details sent! We will contact you on WhatsApp shortly.")

# --- 6. FOOTER ---
st.markdown("<br><hr><p style='text-align:center; color:#888;'>© 2026 Babar Real Estate | Specialized in DHA Lahore Broadway & Prism</p>", unsafe_allow_html=True)
