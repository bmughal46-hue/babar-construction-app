import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. PAGE SETUP (Professional Look) ---
st.set_page_config(
    page_title="Babar Real Estate | Construction Pro",
    page_icon="🏗️",
    layout="wide"
)

# --- 2. CUSTOM CSS (Gold & Premium Theme) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        border-top: 6px solid #C5A059;
        text-align: center;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f3f5;
        border-radius: 8px;
        padding: 10px 25px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. CALCULATION ENGINE ---
def get_data(plot_size, category, city):
    # Area mapping
    sqft_dict = {"3 Marla": 675, "5 Marla": 1125, "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500}
    area = sqft_dict[plot_size]
    
    # Rates per SqFt
    rates = {"Grey Structure": 2450, "Standard (Grey + Finishing)": 4600, "Luxury Construction": 6800}
    city_rates = {"Lahore": 1.0, "Karachi": 1.05, "Islamabad": 1.1, "Gwadar": 1.15}
    
    base_rate = rates[category] * city_rates.get(city, 1.0)
    total = area * base_rate
    
    # Cost Breakdown
    breakdown = {
        "Labour Cost": total * 0.25,
        "Bricks & Sand": total * 0.20,
        "Cement": total * 0.12,
        "Steel (Sarya)": total * 0.15,
        "Finishing & Wood": total * 0.28
    }
    return total, base_rate, area, breakdown

# --- 4. SIDEBAR BRANDING ---
with st.sidebar:
    st.markdown("<h2 style='color: #C5A059;'>BILAL MUGHAL</h2>", unsafe_allow_html=True)
    st.write("Construction Specialist")
    st.divider()
    
    selected_city = st.selectbox("Select City", ["Lahore", "Karachi", "Islamabad", "Gwadar"])
    con_type = st.radio("Construction Type", ["Grey Structure", "Standard (Grey + Finishing)", "Luxury Construction"])
    plot_size = st.select_slider("Select Plot Size", options=["3 Marla", "5 Marla", "8 Marla", "10 Marla", "1 Kanal"])
    
    st.divider()
    st.info("Babar Real Estate & Builders - Trusted Name in DHA Lahore.")

# --- 5. MAIN DASHBOARD ---
st.markdown(f"### 🏗️ BABAR GROUP - Construction Estimator ({selected_city})")

total_cost, rate_sqft, area_sqft, breakdown_data = get_data(plot_size, con_type, selected_city)

# High-Level Metrics
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(f"<div class='metric-box'><h4>Total Estimated Investment</h4><h2 style='color:#C5A059;'>PKR {total_cost/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with m2:
    st.markdown(f"<div class='metric-box'><h4>Current Rate / SqFt</h4><h2>PKR {rate_sqft:,.0f}</h2></div>", unsafe_allow_html=True)
with m3:
    st.markdown(f"<div class='metric-box'><h4>Total Covered Area</h4><h2>{area_sqft} sqft</h2></div>", unsafe_allow_html=True)

# Detailed Tabs
tab_charts, tab_materials = st.tabs(["📊 Cost Analysis", "🧱 Material Estimates"])

with tab_charts:
    st.subheader("Where will your money go?")
    df = pd.DataFrame(list(breakdown_data.items()), columns=['Category', 'Amount'])
    
    # FIXED PLOTLY PIE CHART (No more AttributeErrors)
    fig = px.pie(df, values='Amount', names='Category', hole=0.4,
                 color_discrete_sequence=['#C5A059', '#1E293B', '#334155', '#64748b', '#94a3b8'])
    st.plotly_chart(fig, use_container_width=True)
    
    st.table(df.style.format({"Amount": "PKR {:,.0f}"}))

with tab_materials:
    st.subheader("Approximate Material Quantities")
    c1, c2, c3 = st.columns(3)
    c1.metric("Cement Bags", f"{int(area_sqft * 0.45)} Bags")
    c2.metric("Bricks Count", f"{int(area_sqft * 26)} Pcs")
    c3.metric("Steel (Tons)", f"{round(area_sqft * 0.0035, 2)} Tons")

st.markdown("<br><hr><center>Babar Real Estate & Builders | Bilal Mughal © 2026</center>", unsafe_allow_html=True)
