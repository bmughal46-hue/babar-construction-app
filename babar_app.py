import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Group | Construction Expert", layout="wide")

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .metric-card {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 8px solid #C5A059;
        text-align: center; margin-bottom: 20px;
    }
    .brand-text { color: #C5A059; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIC & DATA ---
def calculate_all(building_type, size, category):
    # Mapping all requested sizes
    size_map = {
        "3 Marla": 675, "4 Marla": 900, "5 Marla": 1125, "7 Marla": 1575, 
        "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500, "2 Kanal": 9000,
        "4 Marla (Commercial)": 900, "8 Marla (Commercial)": 1800
    }
    area = size_map[size]
    
    # Rates
    base_rates = {"Grey Structure": 2500, "Standard": 4800, "Luxury": 7500}
    if "Commercial" in size:
        base_rates = {k: v * 1.3 for k, v in base_rates.items()} # Commercial is 30% costlier
        
    total = area * base_rates[category]
    
    # Material Logic
    materials = {
        "Cement": {"qty": int(area * 0.55), "unit": "Bags", "brands": "Lucky, Bestway, Maple Leaf"},
        "Steel (Sarya)": {"qty": round(area * 0.004, 2), "unit": "Tons", "brands": "Ittehad, Mughal, Amreli"},
        "Bricks (Awwal)": {"qty": int(area * 28), "unit": "Pcs", "brands": "Local Awwal Quality"},
        "Sand (Ravi/Chenab)": {"qty": int(area * 3.5), "unit": "cft", "brands": "Sargodha/Ravi"},
        "Crush (Bajri)": {"qty": int(area * 1.8), "unit": "cft", "brands": "Margalla/Sargodha"},
        "Electric Cables": {"qty": "Full House", "unit": "Wiring", "brands": "Pakistan Cables, Fast Cables"}
    }
    
    breakdown = {"Labour": total*0.25, "Materials": total*0.55, "Finishing": total*0.20}
    
    return total, area, materials, breakdown

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 class='brand-text'>BILAL MUGHAL</h1>", unsafe_allow_html=True)
    st.write("CEO - Babar Real Estate")
    st.divider()
    
    b_type = st.radio("Building Category", ["Residential", "Commercial"])
    
    if b_type == "Residential":
        options = ["3 Marla", "4 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", "1 Kanal", "2 Kanal"]
    else:
        options = ["4 Marla (Commercial)", "8 Marla (Commercial)"]
        
    selected_size = st.selectbox("Select Plot Size", options)
    selected_cat = st.radio("Finish Level", ["Grey Structure", "Standard", "Luxury"])
    st.divider()
    st.success("Expert Tip: Always use 60-Grade Steel for Commercial Projects.")

# --- 5. MAIN CONTENT ---
st.title("🏗️ Babar Group Construction Estimator")
total_inv, total_area, mat_data, b_down = calculate_all(b_type, selected_size, selected_cat)

# Top Metrics
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><h4>Total Investment</h4><h2 class='brand-text'>PKR {total_inv/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><h4>Covered Area</h4><h2>{total_area} sqft</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><h4>Type</h4><h2>{selected_cat}</h2></div>", unsafe_allow_html=True)

# Tabs
t1, t2, t3 = st.tabs(["📋 Material Quantities", "📊 Cost Analysis", "🏢 Recommended Brands"])

with t1:
    st.subheader(f"Required Materials for {selected_size}")
    # Display materials in a nice grid
    m_cols = st.columns(3)
    for i, (item, info) in enumerate(mat_data.items()):
        m_cols[i % 3].metric(item, f"{info['qty']} {info['unit']}")
        m_cols[i % 3].caption(f"Top Brands: {info['brands']}")

with t2:
    st.subheader("Budget Allocation")
    df = pd.DataFrame(list(b_down.items()), columns=['Category', 'Amount'])
    fig = px.pie(df, values='Amount', names='Category', hole=0.5, color_discrete_sequence=['#C5A059', '#2C3E50', '#95A5A6'])
    st.plotly_chart(fig, use_container_width=True)

with t3:
    st.subheader("Awareness: Quality Materials Guide")
    st.info("Babar Group believes in Quality. Here are our verified partners:")
    st.write("*1. Cement:* Use Bestway or Lucky for faster setting.")
    st.write("*2. Steel:* Mughal Supreme 60-Grade is recommended for Commercial.")
    st.write("*3. Cables:* Pakistan Cables (Pure Copper) reduces electricity bills.")
    st.write("*4. Paints:* Jotun or Dulux for long-lasting luxury finish.")

st.markdown("<br><hr><center>Babar Real Estate & Builders | Bilal Mughal © 2026</center>", unsafe_allow_html=True)
