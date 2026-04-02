[2:13 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from PIL import Image
import openai
from fpdf import FPDF
import urllib.parse
import os

# --- 1. SETTINGS & THEME ---
st.set_page_config(page_title="Babar Real Estate | CEO Bilal Mughal", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .header-box { background: #003366; color: white; padding: 25px; text-align: center; border-radius: 0 0 25px 25px; margin-bottom: 20px; }
    .footer-wa { background: #25D366; color: white; padding: 12px; text-align: center; position: fixed; bottom: 0; width: 100%; font-weight: bold; z-index: 999; }
    .stat-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rg…
[2:14 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from PIL import Image
import openai
from fpdf import FPDF
import urllib.parse
import os

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# CSS fix (using triple quotes and escaping)
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; }
    .header-box { background: #003366; color: white; padding: 25px; text-align: center; border-radius: 0 0 25px 25px; }
    .footer-wa { background: #25D366; color: white; padding: 12px; text-align: center; position: fixed; bottom: 0; width: 100%; font-weight: bold; z-index: 999; }
    .stat-card { background: white; padding: 20px; border-radius: 15px; text-align: center; border-top: 5px solid #C5A059; }
</style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("<div class='header-box'><h1>BABAR REAL ESTATE</h1><p>DHA Phase 8 Broadway, Lahore</p></div>", unsafe_allow_html=True)

# --- 3. DATA ENGINE ---
@st.cache_data
def load_data():
    if os.path.exists("data/dha_sample.csv"):
        return pd.read_csv("data/dha_sample.csv")
    else:
        return pd.DataFrame({
            'Phase': ['Phase 8', 'Phase 9 Prism'], 'Block': ['Broadway', 'Sector A'],
            'PlotSize': ['1 Kanal', '1 Kanal'], 'Price': [75000000, 33500000],
            'Latitude': [31.4697, 31.4450], 'Longitude': [74.4534, 74.4800]
        })

df = load_data()

# --- 4. TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Dashboard", "📍 Maps", "🤖 AI Advisor", "🧮 Calculator", "⚙️ Admin"])

with tab1:
    st.subheader("Market Overview 🚀")
    m1, m2 = st.columns(2)
    m1.metric("Total Listings", "1,240", "↑ 12")
    m2.metric("ROI Potential", "18.5%", "High")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("🗺️ DHA Map")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=str(row['Phase'])).add_to(m)
    st_folium(m, width="100%", height=450)

with tab3:
    st.subheader("🤖 AI Advisor")
    if st.text_input("Sawal poochein:"):
        st.info("Bilal Mughal's AI: Phase 9 Prism investment ke liye behtareen hai.")

with tab4:
    st.subheader("🧮 Bill Generator")
    size = st.selectbox("Size", ["5 Marla", "10 Marla", "1 Kanal"])
    rate = st.number_input("Rate per Marla", value=1200000)
    total = ({"5 Marla": 1950, "10 Marla": 3300, "1 Kanal": 5500}[size] / 225) * rate
    st.success(f"Total Estimate: PKR {total:,.0f}")

with tab5:
    st.subheader("⚙️ Admin Portal")
    if st.text_input("Password", type="password") == "babar123":
        st.success("Welcome, Bilal Mughal")
        st.file_uploader("Upload CSV")

# --- 5. FOOTER ---
st.markdown("<div class='footer-wa'><a href='https://wa.me/923244000041' style='color:white; text-decoration:none;'>WhatsApp: Babar Mughal (+92 324 4000041)</a></div>", unsafe_allow_html=True)
