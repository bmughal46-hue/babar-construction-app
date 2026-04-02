import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Group | Official Estimator", layout="wide")

# --- 2. THEME ---
st.markdown("""
    <style>
    .metric-card {
        background-color: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1); border-top: 5px solid #C5A059;
        text-align: center; margin-bottom: 10px;
    }
    .brand-gold { color: #C5A059; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE ACCURATE ENGINE ---
def get_final_estimate(category, size, finish):
    sqft_map = {
        "3 Marla": 675, "4 Marla": 900, "5 Marla": 1125, "7 Marla": 1575, 
        "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500, "2 Kanal": 9000,
        "4 Marla Comm": 900, "8 Marla Comm": 1800
    }
    area = sqft_map[size]
    
    if category == "Residential":
        rates = {"Grey Structure": 2150, "Standard": 4100, "Luxury": 6000}
    else:
        rates = {"Grey Structure": 2700, "Standard": 5200, "Luxury": 7500}
        
    rate = rates[finish]
    total = area * rate
    
    materials = {
        "Cement": {"qty": int(area * 0.40), "unit": "Bags", "info": "Lucky/Bestway (OPC)"},
        "Steel (Sarya)": {"qty": round((area * 3.6) / 1000, 2), "unit": "Tons", "info": "Grade-60 (Mughal/Ittehad)"},
        "Bricks": {"qty": int(area * 22), "unit": "Pcs", "info": "Awwal (Handmade/Machine)"},
        "Sand (Ravi)": {"qty": int(area * 3.0), "unit": "cft", "info": "Screened Ravi Sand"},
        "Crush (Bajri)": {"qty": int(area * 1.5), "unit": "cft", "info": "Margalla/Sargodha Mix"},
        "Cables": {"qty": "Full", "unit": "Wiring", "info": "Pakistan Cables (99% Copper)"}
    }
    
    return total, area, rate, materials

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 class='brand-gold'>BILAL MUGHAL</h1>", unsafe_allow_html=True)
    st.caption("CEO - Babar Real Estate & Builders")
    st.divider()
    cat = st.radio("Category", ["Residential", "Commercial"])
    if cat == "Residential":
        options = ["3 Marla", "4 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", "1 Kanal", "2 Kanal"]
    else:
        options = ["4 Marla Comm", "8 Marla Comm"]
    selected_size = st.selectbox("Plot Size", options)
    selected_finish = st.radio("Finish Type", ["Grey Structure", "Standard", "Luxury"])

# --- 5. MAIN UI ---
st.title("🏗️ Babar Group Master Estimator")
total_val, total_sqft, per_sqft, mat_list = get_final_estimate(cat, selected_size, selected_finish)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><h4>Total Estimate</h4><h2 class='brand-gold'>PKR {total_val/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><h4>Rate / SqFt</h4><h2>PKR {per_sqft:,}</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><h4>Covered Area</h4><h2>{total_sqft} sqft</h2></div>", unsafe_allow_html=True)

t1, t2 = st.tabs(["📋 Detailed Materials", "✅ Brand Awareness"])

with t1:
    st.subheader(f"Material Breakdown: {selected_size}")
    m_cols = st.columns(3)
    for i, (item, info) in enumerate(mat_list.items()):
        with m_cols[i % 3]:
            st.write(f"*{item}*")
            st.subheader(f"{info['qty']} {info['unit']}")
            st.caption(f"Recommendation: {info['info']}")

with t2:
    st.subheader("Babar Group Quality Standards")
    st.info("Hum sirf behtareen material recommend karte hain:")
    st.markdown("""
    1. *Cement:* DG ya Lucky Cement slab ki mazbooti ke liye behtareen hai.
    2. *Steel:* Grade-60 sarya hi istemal karein (Mughal Supreme recommended).
    3. *Electric:* Sasti wiring se gurez karein, sirf Pakistan Cables use karein.
    4. *Bajri:* Margalla ki bajri grey structure ke liye sab se behtar hai.
    """)

st.markdown("<br><hr><center>Babar Real Estate | Powered by Bilal Mughal © 2026</center>", unsafe_allow_html=True)
