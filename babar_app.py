import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Group | Accurate Estimator", layout="wide")

# --- 2. THEME & STYLE ---
st.markdown("""
    <style>
    .metric-card {
        background-color: white; padding: 15px; border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-top: 5px solid #C5A059;
        text-align: center; margin-bottom: 15px;
    }
    .brand-gold { color: #C5A059; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. UPDATED CALCULATION ENGINE (Current Market Rates) ---
def get_verified_estimate(b_type, size, finish):
    # Precise Square Footage (Standard Marla = 225 sqft)
    sqft_map = {
        "3 Marla": 675, "4 Marla": 900, "5 Marla": 1125, "7 Marla": 1575, 
        "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500, "2 Kanal": 9000,
        "4 Marla (Comm)": 900, "8 Marla (Comm)": 1800
    }
    area = sqft_map[size]
    
    # Verified 2026 Market Rates (Grey Structure approx 2150-2300)
    # Residential Base Rates
    res_rates = {"Grey Structure": 2200, "Standard": 4300, "Luxury": 6200}
    # Commercial Base Rates (High load bearing requirements)
    com_rates = {"Grey Structure": 2800, "Standard": 5500, "Luxury": 8000}
    
    rate = com_rates[finish] if "Comm" in size else res_rates[finish]
    total = area * rate
    
    # Verified Material Quantities (Engineering Standards)
    # Bags: 0.4 to 0.45 per sqft for residential grey
    # Steel: 3.5kg to 4kg per sqft
    materials = {
        "Cement": {"qty": int(area * 0.42), "unit": "Bags", "brands": "Lucky, Bestway, DG"},
        "Steel (Sarya)": {"qty": round((area * 3.8) / 1000, 2), "unit": "Tons", "brands": "Mughal, Ittehad, Amreli"},
        "Bricks": {"qty": int(area * 24), "unit": "Pcs", "brands": "Awwal Grade Brick"},
        "Sand": {"qty": int(area * 3.2), "unit": "cft", "brands": "Ravi / Chenab"},
        "Crush (Bajri)": {"qty": int(area * 1.6), "unit": "cft", "brands": "Sargodha / Margalla"}
    }
    
    breakdown = {"Labour": total*0.24, "Materials": total*0.58, "Other/Finishing": total*0.18}
    return total, area, materials, breakdown, rate

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 class='brand-gold'>BILAL MUGHAL</h1>", unsafe_allow_html=True)
    st.caption("Babar Real Estate & Builders")
    st.divider()
    
    category = st.radio("Category", ["Residential", "Commercial"])
    
    if category == "Residential":
        sizes = ["3 Marla", "4 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", "1 Kanal", "2 Kanal"]
    else:
        sizes = ["4 Marla (Comm)", "8 Marla (Comm)"]
        
    p_size = st.selectbox("Select Plot Size", sizes)
    p_finish = st.radio("Finish Type", ["Grey Structure", "Standard", "Luxury"])
    st.divider()
    st.info("Note: Rates are based on April 2026 market averages in Punjab.")

# --- 5. MAIN UI ---
st.title("🏗️ Babar Group Real-Time Estimator")
total_val, total_sqft, materials, b_down, per_sqft_rate = get_verified_estimate(category, p_size, p_finish)

# Summary Cards
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><h4>Total Investment</h4><h2 class='brand-gold'>PKR {total_val/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><h4>Rate per SqFt</h4><h2>PKR {per_sqft_rate:,}</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><h4>Total Area</h4><h2>{total_sqft} sqft</h2></div>", unsafe_allow_html=True)

# Detailed Breakdown Tabs
t1, t2, t3 = st.tabs(["🧱 Material Quantities", "📈 Market Analysis", "✅ Quality Checklist"])

with t1:
    st.subheader(f"Material Breakdown for {p_size} ({p_finish})")
    m_cols = st.columns(3)
    for i, (item, info) in enumerate(materials.items()):
        with m_cols[i % 3]:
            st.markdown(f"*{item}*")
            st.write(f"*{info['qty']}* {info['unit']}")
            st.caption(f"Top Brands: {info['brands']}")

with t2:
    st.subheader("Budget Allocation (Percentage)")
    df = pd.DataFrame(list(b_down.items()), columns=['Category', 'Amount'])
    fig = px.pie(df, values='Amount', names='Category', hole=0.5, 
                 color_discrete_sequence=['#C5A059', '#1E293B', '#475569'])
    st.plotly_chart(fig, use_container_width=True)

with t3:
    st.subheader("Babar Group Quality Awareness")
    st.success("Bilal Mughal's Verified Standards:")
    st.markdown("""
    * *Cement:* DG or Lucky Cement is best for slab strength.
    * *Steel:* Always use *Grade 60* Steel for multi-story or commercial.
    * *Bricks:* Ensure 'Awwal' grade with no salt (Shor) content.
    * *Cables:* Use 99% pure copper (Pakistan Cables or Fast).
    """)

st.markdown("<br><hr><center>Babar Real Estate | Bilal Mughal © 2026</center>", unsafe_allow_html=True)
