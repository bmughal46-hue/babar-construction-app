# app.py
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from PIL import Image
import openai
from fpdf import FPDF
import urllib.parse

# -----------------------------
# CONFIG & API KEY
# -----------------------------
st.set_page_config(page_title="Babar Real Estate | CEO Babar Mughal", layout="wide")
openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

# -----------------------------
# ASSETS
# -----------------------------
logo = Image.open("assets/logo.png")  # Add your logo.png in assets folder
ceo = Image.open("assets/ceo.png")    # Add your CEO image

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.header { background-color:#003366; color:white; padding:20px; border-radius:0 0 20px 20px; text-align:center; }
.footer { background-color:#003366; color:white; padding:12px; text-align:center; position:fixed; bottom:0; width:100%; }
.metric-box { background-color:#f8f9fa; border-radius:10px; padding:10px; text-align:center; margin:5px; }
.listing { border-left:4px solid gold; padding:8px; margin:5px; background:#fff; border-radius:5px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.image(logo, width=200)
st.markdown("<div class='header'><h2>BABAR REAL ESTATE</h2><p>C-116, Broadway Plaza, DHA Phase 8, Lahore</p></div>", unsafe_allow_html=True)

# -----------------------------
# TABS
# -----------------------------
tabs = st.tabs(["🏡 Dashboard","📍 Maps","🤖 AI Advisor","🧮 Calculator","⚙️ Admin"])

# -----------------------------
# SAMPLE DHA DATA
# -----------------------------
data = [
    {"Phase":"Phase 9","Block":"Prism","PlotNumber":1,"PlotSize":"1 Kanal","Price":33000000,"Type":"Residential","Latitude":31.4697,"Longitude":74.4534,"NearbySchools":"School A","NearbyParks":"Park A","NearbyMarkets":"Market A","Masjid":"Masjid A"},
    {"Phase":"Phase 7","Block":"Sector Z","PlotNumber":2,"PlotSize":"10 Marla","Price":18500000,"Type":"Residential","Latitude":31.4720,"Longitude":74.4550,"NearbySchools":"School B","NearbyParks":"Park B","NearbyMarkets":"Market B","Masjid":"Masjid B"}
]
df = pd.DataFrame(data)

# -----------------------------
# DASHBOARD
# -----------------------------
with tabs[0]:
    st.subheader("Real-Time Market Metrics 🚀")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Listings", len(df))
    col2.metric("ROI Potential", "18.5%")
    col3.metric("Hot Phase", "Phase 9 Prism")
    
    st.markdown("---")
    st.write("### Recent Hot Listings 🔥")
    for _, row in df.iterrows():
        st.markdown(f"<div class='listing'>{row['Phase']} {row['Block']} | {row['PlotSize']} | PKR {row['Price']:,}</div>", unsafe_allow_html=True)

# -----------------------------
# MAPS
# -----------------------------
with tabs[1]:
    st.subheader("🗺️ Interactive DHA Map")
    m = folium.Map(location=[31.5204, 74.3587], zoom_start=12)
    for _, row in df.iterrows():
        popup_text = f"{row['Phase']} {row['Block']} | {row['PlotSize']} | PKR {row['Price']:,}\nSchools:{row['NearbySchools']}\nParks:{row['NearbyParks']}\nMarkets:{row['NearbyMarkets']}\nMasjid:{row['Masjid']}"
        folium.Marker([row['Latitude'], row['Longitude']], popup=popup_text).add_to(m)
    st_folium(m, width=700, height=500)

# -----------------------------
# AI ADVISOR
# -----------------------------
with tabs[2]:
    st.subheader("🤖 AI Property Advisor")
    query = st.text_input("Ask about DHA investment, ROI, construction:")
    if query:
        with st.spinner("Fetching AI advice..."):
            if openai.api_key:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role":"user","content":query}]
                )
                answer = response['choices'][0]['message']['content']
                st.success(answer)
            else:
                st.warning("Add your OpenAI API Key in Streamlit Secrets!")

# -----------------------------
# CONSTRUCTION CALCULATOR + PDF + WHATSAPP
# -----------------------------
with tabs[3]:
    st.subheader("🧮 Smart Construction Calculator")
    size = st.selectbox("Plot Size", ["5 Marla","10 Marla","1 Kanal","2 Kanal","4 Marla","8 Marla"])
    rate = st.number_input("Rate per Marla (PKR)", value=1000000)
    sqft_map = {"5 Marla":1950,"10 Marla":3300,"1 Kanal":5500,"2 Kanal":11000,"4 Marla":1500,"8 Marla":3300}
    area = sqft_map.get(size, 2000)
    total = area * rate
    st.markdown(f"""
        <div style='border:2px dashed #003366; padding:20px; border-radius:10px; background:white;'>
        <h3 style='text-align:center;'>BABAR REAL ESTATE</h3>
        <p><b>Plot:</b> {size}</p>
        <p><b>Area:</b> {area} sqft</p>
        <hr>
        <h3 style='text-align:right; color:#28a745;'>Total: PKR {total:,.0f}</h3>
        </div>
    """, unsafe_allow_html=True)

    # PDF Generation
    pdf_btn = st.button("Download PDF")
    if pdf_btn:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Babar Real Estate Construction Calculation", ln=True, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Plot Size: {size}", ln=True)
        pdf.cell(0, 10, f"Area: {area} sqft", ln=True)
        pdf.cell(0, 10, f"Total: PKR {total:,}", ln=True)
        pdf.output("construction_calculation.pdf")
        st.success("PDF Generated: construction_calculation.pdf")

    # WhatsApp Share
    wa_text = f"Plot Size: {size}\nArea: {area} sqft\nTotal: PKR {total:,}"
    wa_url = f"https://wa.me/?text={urllib.parse.quote(wa_text)}"
    st.markdown(f"[Share on WhatsApp]({wa_url})", unsafe_allow_html=True)

# -----------------------------
# ADMIN PANEL
# -----------------------------
with tabs[4]:
    st.subheader("⚙️ Admin Control Panel")
    pwd = st.text_input("Enter Admin Password", type="password")
    if pwd == "babar123":
        st.success("Welcome, CEO Babar Mughal")
        st.file_uploader("Upload DHA CSV Data", type=["csv"])
        st.button("Update Listings")
    else:
        st.warning("Password required to access management.")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(f"<div class='footer'>WhatsApp: <a href='https://wa.me/923244000041' style='color:white;'>Babar Mughal (+92 324 4000041)</a></div>", unsafe_allow_html=True)
streamlit run app.py
