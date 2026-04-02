import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Babar Real Estate | Zameen Portal", layout="wide")

# Safe CSS (No Decimals Error)
st.markdown("""
<style>
    .stApp { background-color: #f0f2f5; }
    .main-header { background-color: #003366; color: white; padding: 30px; text-align: center; border-radius: 0px 0px 30px 30px; margin-bottom: 25px; border-bottom: 5px solid #c5a059; }
    .zameen-card { background: white; padding: 15px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 15px; box-shadow: 2px 2px 10px #ccc; }
    .wa-footer { background: #25D366; color: white; padding: 10px; text-align: center; position: fixed; bottom: 0; width: 100%; font-weight: bold; z-index: 100; }
</style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("<div class='main-header'><h1>BABAR REAL ESTATE</h1><p>Pakistan's Premium Property Portal | DHA Phase 8 Lahore</p></div>", unsafe_allow_html=True)

# --- 3. DATA ENGINE ---
@st.cache_data
def get_babar_data():
    if os.path.exists("data/dha_sample.csv"):
        return pd.read_csv("data/dha_sample.csv")
    else:
        return pd.DataFrame({
            'Phase': ['Phase 8', 'Phase 9 Prism', 'Phase 6'],
            'Block': ['Broadway', 'Sector A', 'Block L'],
            'Size': ['1 Kanal', '1 Kanal', '10 Marla'],
            'Price': [75000000, 33500000, 45000000],
            'Lat': [31.4697, 31.4450, 31.4880],
            'Lon': [74.4534, 74.4800, 74.4440]
        })

df = get_babar_data()

# --- 4. TABS (THE CORE FUNCTIONS) ---
tabs = st.tabs(["🏡 Home", "📍 Map Search", "🤖 AI Advisor", "🧮 Calculator", "⚙️ Admin"])

# HOME / LISTINGS
with tabs[0]:
    st.subheader("Featured Properties 🏠")
    col_a, col_b = st.columns(2)
    col_a.metric("Total Listings", "1,240", "New")
    col_b.metric("ROI Potential", "18.5%", "High")
    
    for i, row in df.iterrows():
        st.markdown(f"""
        <div class='zameen-card'>
            <h4 style='margin:0; color:#003366;'>PKR {row['Price']:,}</h4>
            <p style='margin:0;'><b>{row['Phase']} - {row['Block']}</b> | {row['Size']}</p>
            <small>Verified by Babar Real Estate</small>
        </div>
        """, unsafe_allow_html=True)

# MAP SEARCH
with tabs[1]:
    st.subheader("📍 DHA Plot Locator")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker([row['Lat'], row['Lon']], popup=f"{row['Phase']} - {row['Price']}").add_to(m)
    st_folium(m, width="100%", height=500)

# AI ADVISOR
with tabs[2]:
    st.subheader("🤖 Smart Property Advisor")
    query = st.text_input("Ask anything (e.g. Best phase for investment?)")
    if query:
        st.info(f"Bilal Mughal's AI Insight: For '{query}', we recommend Phase 9 Prism due to 18.5% ROI.")

# CALCULATOR
with tabs[3]:
    st.subheader("🧮 Construction & Plot Calculator")
    c_size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    c_rate = st.number_input("Rate per Marla", value=1500000)
    marla_val = {"5 Marla": 5, "10 Marla": 10, "1 Kanal": 20}
    total_price = marla_val[c_size] * c_rate
    st.success(f"Estimated Total Price: PKR {total_price:,.0f}")

# ADMIN PANEL
with tabs[4]:
    st.subheader("⚙️ CEO Management Portal")
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if user_id == "admin" and password == "babar123":
            st.success("Welcome, Bilal Mughal! [CEO Mode Active]")
            st.file_uploader("Upload New Inventory (CSV)")
        else:
            st.error("Invalid Credentials")

# --- 5. STICKY FOOTER ---
st.markdown(f"<div class='wa-footer'>📞 Call/WhatsApp CEO Bilal Mughal: +92 324 4000041</div>", unsafe_allow_html=True)
