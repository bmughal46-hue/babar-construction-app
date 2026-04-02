[11:46 PM, 4/2/2026] Bilal Mughal: import streamlit as st
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
        "8 Marla": 1800, "10 Marla": 2250, "1 Kanal…
[11:49 PM, 4/2/2026] Bilal Mughal: import streamlit as st

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Group | Master Estimator", layout="wide")

# --- 2. LOGIC ENGINE (2026 DATA) ---
def calculate_babar_estimate(cat, size, finish):
    # Accurate Area Mapping (Double Story Covered Area)
    # 5 Marla = ~2100 sqft, 10 Marla = ~3400 sqft
    sqft_map = {
        "3 Marla": 1215, "4 Marla": 1620, "5 Marla": 2025, "7 Marla": 2678, 
        "8 Marla": 3060, "10 Marla": 3375, "1 Kanal": 6300, "2 Kanal": 11000,
        "4 Marla Comm": 2400, "8 Marla Comm": 4500 # Multi-story assumptions
    }
    area = sqft_map[size]
    
    # LATEST RATES (APRIL 2026)
    if cat == "Residential":
        # Grey: 3300, Standard: 6200, Luxury: 8800
        rates = {"Grey Structure": 3300, "Standard": 6200, "Luxury": 8800}
    else: # Commercial
        rates = {"Grey Structure": 4200, "Standard": 8500, "Luxury": 12000}
        
    rate = rates[finish]
    total = area * rate
    
    # QUANTITIES (Verified by Glorious Builders 2026 Standards)
    # Cement: ~0.45 bags/sqft | Steel: ~3.8kg/sqft | Bricks: ~25/sqft
    materials = {
        "Cement": {"qty": int(area * 0.45), "unit": "Bags", "rate": 1450},
        "Steel (Sarya)": {"qty": round((area * 3.8)/1000, 2), "unit": "Tons", "rate": 275000},
        "Bricks": {"qty": int(area * 25), "unit": "Pcs", "rate": 25},
        "Sand (Ravi)": {"qty": int(area * 3.5), "unit": "cft", "rate": 65},
        "Crush (Sargodha)": {"qty": int(area * 1.6), "unit": "cft", "rate": 135}
    }
    
    return total, area, rate, materials

# --- 3. UI ---
st.title("🏗️ Babar Group | Professional Construction Calculator")
st.markdown("### Powered by Bilal Mughal - April 2026 Market Rates")

with st.sidebar:
    st.header("Project Setup")
    cat = st.radio("Category", ["Residential", "Commercial"])
    
    if cat == "Residential":
        options = ["3 Marla", "4 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", "1 Kanal", "2 Kanal"]
    else:
        options = ["4 Marla Comm", "8 Marla Comm"]
        
    p_size = st.selectbox("Select Plot Size", options)
    p_finish = st.radio("Construction Mode", ["Grey Structure", "Standard", "Luxury"])

total, area, rate_sqft, mats = calculate_babar_estimate(cat, p_size, p_finish)

# Main Stats
c1, c2, c3 = st.columns(3)
c1.metric("Total Estimated Cost", f"PKR {total/1000000:.2f}M")
c2.metric("Market Rate / SqFt", f"PKR {rate_sqft:,}")
c3.metric("Total Covered Area", f"{area:,} sqft")

st.divider()

# Material Breakdown
st.subheader("🛠️ Material & Quantity Requirements")
m_cols = st.columns(len(mats))
for i, (item, data) in enumerate(mats.items()):
    with m_cols[i]:
        st.write(f"*{item}*")
        st.subheader(f"{data['qty']} {data['unit']}")
        st.caption(f"Estimated Market Price: {data['rate']}")

st.info("Note: These estimates include Labor Cost (Avg PKR 500-600/sqft) and premium materials.")
