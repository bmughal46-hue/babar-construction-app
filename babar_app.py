import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from PIL import Image
import os
from fpdf import FPDF
import urllib.parse

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate | CEO Bilal Mughal", layout="wide")

# --- 2. PREMIUM CSS (Zameen Style) ---
st.markdown("""
<style>
    .main-header { background-color: #003366; color: white; padding: 30px; text-align: center; border-radius: 0 0 30px 30px; border-bottom: 5px solid #c5a059; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #f8f9fa; border-radius: 5px; padding: 10px 20px; }
    .property-card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); border-left: 8px solid #28a745; margin-bottom: 20px; }
    .wa-btn { background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; }
</style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR CEO PROFILE ---
with st.sidebar:
    logo_path = "assets/logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)
    st.title("CEO Portal")
    st.info("Bilal Mughal\nSocial Media Marketer & Real Estate Expert")
    st.markdown("---")
    admin_pass = st.text_input("Admin Access", type="password")

# --- 4. HEADER ---
st.markdown("<div class='main-header'><h1>BABAR REAL ESTATE</h1><p>C-116, Broadway Plaza, DHA Phase 8, Lahore</p></div>", unsafe_allow_html=True)

# --- 5. DATA ENGINE ---
data = [
    {"Phase":"Phase 9","Block":"Prism","Size":"1 Kanal","Price":33000000,"Lat":31.4697,"Lon":74.4534},
    {"Phase":"Phase 8","Block":"Broadway","Size":"1 Kanal","Price":75000000,"Lat":31.4720,"Lon":74.4550},
    {"Phase":"Phase 7","Block":"Sector Z","Size":"10 Marla","Price":18500000,"Lat":31.4880,"Lon":74.4440}
]
df = pd.DataFrame(data)

# --- 6. TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🏡 Listings", "📍 Map Search", "🧮 Construction Calc", "⚙️ Management"])

with tab1:
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Active Listings", "1,240", "+12")
    col_b.metric("ROI Potential", "18.5%", "High")
    col_c.metric("Hot Area", "DHA Phase 9")
    
    st.markdown("### Featured Properties")
    for _, row in df.iterrows():
        st.markdown(f"""
        <div class='property-card'>
            <h3>PKR {row['Price']:,}</h3>
            <p><b>{row['Phase']} - {row['Block']}</b> | {row['Size']}</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("Interactive Property Map")
    m = folium.Map(location=[31.4697, 74.4534], zoom_start=12)
    for _, row in df.iterrows():
        folium.Marker([row['Lat'], row['Lon']], popup=f"{row['Phase']}: {row['Price']}").add_to(m)
    st_folium(m, width="100%", height=500)

with tab3:
    st.subheader("Smart Bill & Construction Generator")
    p_size = st.selectbox("Select Plot", ["5 Marla", "10 Marla", "1 Kanal"])
    p_rate = st.number_input("Rate per sqft", value=3450)
    sqft = {"5 Marla": 1125, "10 Marla": 2250, "1 Kanal": 4500}[p_size]
    total = sqft * p_rate
    
    st.success(f"Total Construction Estimate: PKR {total:,.0f}")
    
    # WhatsApp Integration
    wa_msg = f"Babar Real Estate Estimate:\nPlot: {p_size}\nTotal: PKR {total:,}"
    wa_url = f"https://wa.me/923244000041?text={urllib.parse.quote(wa_msg)}"
    st.markdown(f"<a href='{wa_url}' class='wa-btn'>Send Estimate to WhatsApp</a>", unsafe_allow_html=True)

with tab4:
    if admin_pass == "babar123":
        st.success("Welcome, CEO Bilal Mughal!")
        st.file_uploader("Update Market Data (CSV)")
        st.button("Sync with Zameen Cloud")
    else:
        st.warning("Please enter Admin Password in Sidebar to access Management.")

# --- FOOTER ---
st.markdown("<br><br><div style='text-align:center; color:grey;'>© 2026 Babar Real Estate | Developed by Bilal Mughal</div>", unsafe_allow_html=True)
