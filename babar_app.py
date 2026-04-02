[11:41 PM, 4/2/2026] Bilal Mughal: import streamlit as st
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
[11:43 PM, 4/2/2026] Bilal Mughal: import streamlit as st
import pandas as pd

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
    # Accurate Sqft Mapping
    sqft_map = {
        "3 Marla": 675, "4 Marla": 900, "5 Marla": 1125, "7 Marla": 1575, 
        "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500, "2 Kanal": 9000,
        "4 Marla Comm": 900, "8 Marla Comm": 1800
    }
    area = sqft_map[size]
    
    # APRIL 2026 MARKET RATES (Verified)
    if category == "Residential":
        rates = {"Grey Structure": 2150, "Standard": 4100, "Luxury": 6000}
    else: # Commercial
        rates = {"Grey Structure": 2700, "Standard": 5200, "Luxury": 7500}
        
    rate = rates[finish]
    total = area * rate
    
    # Material Ratios (Contractor Standards)
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
    
    st.divider()
    st.warning("Rates vary based on plot location & design complexity.")

# --- 5. MAIN UI ---
st.title("🏗️ Babar Group Master Estimator")
total_val, total_sqft, per_sqft, mat_list = get_final_estimate(cat, selected_size, selected_finish)

# Summary Row
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"<div class='metric-card'><h4>Total Estimate</h4><h2 class='brand-gold'>PKR {total_val/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='metric-card'><h4>Rate / SqFt</h4><h2>PKR {per_sqft:,}</h2></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='metric-card'><h4>Covered Area</h4><h2>{total_sqft} sqft</h2></div>", unsafe_allow_html=True)

# Tabs
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
