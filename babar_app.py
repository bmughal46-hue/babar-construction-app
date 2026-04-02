[2:07 AM, 4/3/2026] Bilal Mughal: babar-construction-app/data/dha_sample.csv
Columns: Phase,Block,PlotNumber,PlotSize,Price,Type,Latitude,Longitude,NearbySchools,NearbyParks,NearbyMarkets,Masjid
[2:11 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from PIL import Image
import openai
from fpdf import FPDF
import urllib.parse
import os

# --- 1. CONFIG & SYSTEM ---
st.set_page_config(page_title="Babar Real Estate | CEO Bilal Mughal", layout="wide")
openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

# --- 2. PREMIUM CSS ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    .main-header { background: #003366; color: white; padding: 25px; text-align: center; border-radius: 0 0 20px 20px; }
    .footer-wa { background-color: #25D366; color: white; padding: 12px; text-align: center; position: fixed; bottom: 0; width: 100%; font-weight: bold; z-index: 1000; }
    .bill-box { border: 2px dashed #003366; padding: 20px; background: white; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- 3. ASSETS & HEADER ---
col_logo, col_ceo = st.columns([4, 1])
with col_logo:
    if os.path.exists("assets/logo.png"): st.image("assets/logo.png", width=200)
    else: st.title("BABAR REAL ESTATE")
with col_ceo:
    if os.path.exists("assets/ceo.png"): st.image("assets/ceo.png", width=80)

st.markdown("<div class='main-header'><h2>BABAR REAL ESTATE</h2><p>C-116, Broadway Plaza, DHA Phase 8, Lahore</p></div>", unsafe_allow_html=True)

# --- 4. DATA LOADING ---
@st.cache_data
def get_data():
    if os.path.exists("data/dha_sample.csv"): return pd.read_csv("data/dha_sample.csv")
    return pd.DataFrame({
        'Phase': ['Phase 8', 'Phase 9 Prism'], 'Block': ['Broadway', 'Sector A'],
        'PlotSize': ['1 Kanal', '1 Kanal'], 'Price': [75000000, 33000000],
        'Latitude': [31.4697, 31.4450], 'Longitude': [74.4534, 74.4800]
    })

df = get_data()

# --- 5. TABS NAVIGATION ---
tabs = st.tabs(["📊 Dashboard", "📍 Maps", "🤖 AI Advisor", "🧮 Calculator", "⚙️ Admin"])

with tabs[0]: # Dashboard
    st.subheader("Market Insights 🚀")
    c1, c2 = st.columns(2)
    c1.metric("Active Listings", len(df))
    c2.metric("ROI Potential", "18.5%")
    st.dataframe(df, use_container_width=True)

with tabs[1]: # Maps
    st.subheader("🗺️ Interactive DHA Map")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=f"{row['Phase']} - {row['Price']}").add_to(m)
    st_folium(m, width="100%", height=450)

with tabs[2]: # AI Advisor
    st.subheader("🤖 AI Investment Advisor")
    query = st.text_input("Investement ke bare mein poochein:")
    if query:
        st.info(f"Bilal Mughal's AI Insight: '{query}' ke liye Phase 9 Prism behtareen hai.")

with tabs[3]: # Calculator + PDF
    st.subheader("🧮 Bill Generator")
    p_size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    p_rate = st.number_input("Rate per Marla", value=1200000)
    
    area_map = {"5 Marla": 1950, "10 Marla": 3300, "1 Kanal": 5500}
    total_val = (area_map[p_size] / 225) * p_rate

    st.markdown(f"<div class='bill-box'><h3>PKR {total_val:,.0f}</h3><p>{p_size} Construction Estimate</p></div>", unsafe_allow_html=True)
    
    # PDF Download
    pdf = FPDF()
    pdf.add_page(); pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "BABAR REAL ESTATE ESTIMATE", ln=True, align='C')
    pdf.set_font("Arial", '', 12); pdf.cell(0, 10, f"Plot: {p_size} | Total: {total_val:,.0f}", ln=True)
    st.download_button("📥 Download PDF Bill", data=pdf.output(dest='S').encode('latin-1'), file_name="Babar_Estimate.pdf")

with tabs[4]: # Admin
    if st.text_input("Password", type="password") == "babar123":
        st.success("Welcome, CEO Bilal Mughal")
        st.file_uploader("Upload New CSV")

# --- 6. FOOTER ---
st.markdown("<div class='footer-wa'><a href='https://wa.me/923244000041' style='color:white; text-decoration:none;'>WhatsApp: Bilal Mughal (+92 324 4000041)</a></div>", unsafe_allow_html=True)
