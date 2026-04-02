import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

# --- 1. BASIC SETTINGS ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# --- 2. HEADER (Saada aur Mazboot) ---
st.header("🏠 BABAR REAL ESTATE")
st.write("Broadway Plaza, DHA Phase 8, Lahore | CEO Bilal Mughal")
st.markdown("---")

# --- 3. DATA LOADING ---
@st.cache_data
def load_babar_data():
    if os.path.exists("data/dha_sample.csv"):
        return pd.read_csv("data/dha_sample.csv")
    else:
        # Fallback Data agar file na mile
        return pd.DataFrame({
            'Phase': ['Phase 8', 'Phase 9 Prism'], 
            'Price': [75000000, 33500000],
            'Lat': [31.4697, 31.4450], 
            'Lon': [74.4534, 74.4800]
        })

df = load_babar_data()

# --- 4. TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📍 Maps", "🧮 Calculator", "⚙️ Admin"])

with tab1:
    st.subheader("Real-Time Market Metrics 🚀")
    c1, c2 = st.columns(2)
    c1.metric("Listings", "1,240")
    c2.metric("ROI Potential", "18.5%")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("🗺️ DHA Plot Map")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker([row['Lat'], row['Lon']], popup=str(row['Phase'])).add_to(m)
    st_folium(m, width="100%", height=400)

with tab3:
    st.subheader("🧮 Price Estimator")
    size = st.selectbox("Select Plot", ["5 Marla", "10 Marla", "1 Kanal"])
    rate = st.number_input("Rate per Marla", value=1200000)
    count = {"5 Marla": 5, "10 Marla": 10, "1 Kanal": 20}[size]
    total = count * rate
    st.success(f"Estimated Price: PKR {total:,.0f}")

with tab4:
    st.subheader("⚙️ CEO Login")
    pw = st.text_input("Enter Password", type="password")
    if pw == "babar123":
        st.success("Welcome, Bilal Mughal")
        st.file_uploader("Upload New Data (CSV)")

# --- 5. FOOTER ---
st.markdown("---")
st.info("📞 Contact: +92 324 4000041")
