import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Babar Construction | Professional Estimator",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR MODERN UI ---
st.markdown("""
    <style>
    :root {
        --primary-color: #C5A059;
        --secondary-color: #1E293B;
    }
    .main { background-color: #F8FAFC; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #C5A059;
        color: white;
        font-weight: bold;
        height: 3em;
        border: none;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        border-top: 4px solid #C5A059;
    }
    .section-header {
        color: #1E293B;
        font-weight: 800;
        font-size: 24px;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DYNAMIC DATA (CITY & RATES) ---
CITY_RATES = {
    "Lahore": 1.0,
    "Karachi": 1.05,
    "Islamabad": 1.1,
    "Faisalabad": 0.95,
    "Gwadar": 1.2
}

# --- LOGIC & CALCULATIONS ---
def calculate_costs(plot_size, construction_type, city):
    # Size in sqft
    sizes_sqft = {"3 Marla": 675, "5 Marla": 1125, "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500}
    area = sizes_sqft[plot_size]
    
    # Base rates per sqft (Grey + Finishing)
    base_rates = {
        "Grey Structure": 2400,
        "Standard (Grey + Finishing)": 4500,
        "Luxury Construction": 6500
    }
    
    rate = base_rates[construction_type] * CITY_RATES[city]
    total_cost = area * rate
    
    # Breakdown Percentages
    breakdown = {
        "Cement & Sand": total_cost * 0.15,
        "Steel (Sarya)": total_cost * 0.12,
        "Bricks/Blocks": total_cost * 0.10,
        "Labour Cost": total_cost * 0.25,
        "Finishing (Tiles/Paint)": total_cost * 0.28,
        "Electric & Plumbing": total_cost * 0.10
    }
    
    return total_cost, rate, breakdown, area

# --- SIDEBAR BRANDING ---
with st.sidebar:
    st.markdown("<h1 style='color: #C5A059;'>BILAL MUGHAL</h1>", unsafe_allow_html=True)
    st.markdown("### Construction Expert")
    st.divider()
    selected_city = st.selectbox("Select City", list(CITY_RATES.keys()))
    construction_type = st.radio("Construction Type", ["Grey Structure", "Standard (Grey + Finishing)", "Luxury Construction"])
    plot_size = st.select_slider("Plot Size", options=["3 Marla", "5 Marla", "8 Marla", "10 Marla", "1 Kanal"])
    
    st.divider()
    st.info("Rates are updated as of April 2026 based on market analysis.")

# --- MAIN INTERFACE ---
st.markdown(f"<div class='section-header'>🏗️ Construction Cost Estimator - {selected_city}</div>", unsafe_allow_html=True)

total_cost, rate_per_sqft, breakdown, area_sqft = calculate_costs(plot_size, construction_type, selected_city)

# Top Metrics
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f"<div class='metric-card'><h4>Total Estimate</h4><h2 style='color:#C5A059;'>PKR {total_cost/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with m2:
    st.markdown(f"<div class='metric-card'><h4>Cost per SqFt</h4><h2>PKR {rate_per_sqft:,.0f}</h2></div>", unsafe_allow_html=True)
with m3:
    st.markdown(f"<div class='metric-card'><h4>Total Area</h4><h2>{area_sqft} sqft</h2></div>", unsafe_allow_html=True)

st.write("")

# Tabs for detailed view
tab1, tab2, tab3 = st.tabs(["📊 Cost Breakdown", "🧱 Material Quantities", "📈 Market Comparison"])

with tab1:
    c1, c2 = st.columns([1, 1.2])
    with c1:
        st.subheader("Category Wise Split")
        df_breakdown = pd.DataFrame(list(breakdown.items()), columns=['Category', 'Amount'])
        fig = px.pie(df_breakdown, values='Amount', names='Category', hole=.4, 
                     color_discrete_sequence=px.colors.sequential.Gold_r)
        st.plotly_chart(fig, use_container_width=True)
    
    with c2:
        st.subheader("Cost Summary Table")
        st.table(df_breakdown.style.format({"Amount": "PKR {:,.0f}"}))

with tab2:
    st.subheader("Estimated Material Requirements")
    st.write("Based on standard engineering formulas for Grey Structure:")
    # Basic logic for materials
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Cement Bags", f"{int(area_sqft * 0.4)} Bags")
    col_b.metric("Steel (Sarya)", f"{round(area_sqft * 0.003, 1)} Tons")
    col_c.metric("Bricks", f"{int(area_sqft * 25)} Bricks")

with tab3:
    st.subheader("Price Prediction & Comparison")
    # Comparison Chart
    compare_data = {
        "Type": ["Economy", "Standard", "Luxury"],
        "Rate": [2200, 4500, 6500]
    }
    fig_bar = px.bar(compare_data, x="Type", y="Rate", color="Type", 
                     title="Market Rate Comparison (PKR per SqFt)")
    st.plotly_chart(fig_bar, use_container_width=True)

# --- CALL TO ACTION ---
st.divider()
col_left, col_right = st.columns([2, 1])
with col_left:
    st.markdown("### 📄 Need a detailed PDF Report?")
    st.write("Our premium report includes structural drawings, detailed BoQ, and exact material brands.")
with col_right:
    if st.button("Generate Professional Report"):
        st.success("Report generated! Check your downloads.")

st.markdown("<br><center><p style='color: grey;'>Developed by Bilal Mughal | Babar Real Estate & Builders</p></center>", unsafe_allow_html=True)
