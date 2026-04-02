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
    .bill-box { border: 2px dash…
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
    .stat-card { background: white; padding: 20px; border-radius: 15px; text-align: center; border-t…
[2:16 AM, 4/3/2026] Bilal Mughal: import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# --- 2. SIMPLE HEADER ---
st.title("🏠 BABAR REAL ESTATE")
st.write("DHA Phase 8 Broadway, Lahore | CEO Bilal Mughal")
st.markdown("---")

# --- 3. DATA LOADING ---
@st.cache_data
def load_data():
    if os.path.exists("data/dha_sample.csv"):
        return pd.read_csv("data/dha_sample.csv")
    else:
        return pd.DataFrame({
            'Phase': ['Phase 8', 'Phase 9 Prism'], 
            'Price': [75000000, 33500000],
            'Latitude': [31.4697, 31.4450], 
            'Longitude': [74.4534, 74.4800]
        })

df = load_data()

# --- 4. TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📍 Maps", "🧮 Calculator", "⚙️ Admin"])

with tab1:
    st.subheader("Market Overview 🚀")
    st.metric("ROI Potential", "18.5%", "High")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("🗺️ DHA Map")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=str(row['Phase'])).add_to(m)
    st_folium(m, width="100%", height=450)

with tab3:
    st.subheader("🧮 Price Calculator")
    size = st.selectbox("Size", ["5 Marla", "10 Marla", "1 Kanal"])
    rate = st.number_input("Rate per Marla", value=1200000)
    # Simple calculation: Marla size * Rate
    marla_count = {"5 Marla": 5, "10 Marla": 10, "1 Kanal": 20}[size]
    total = marla_count * rate
    st.success(f"Total Estimate: PKR {total:,.0f}")

with tab4:
    st.subheader("⚙️ Admin")
    if st.text_input("Password", type="password") == "babar123":
        st.success("Welcome, Bilal Mughal")
        st.file_uploader("Upload CSV")

# --- 5. FOOTER ---
st.markdown("---")
st.write("📞 WhatsApp: Babar Mughal (+92 324 4000041)")
