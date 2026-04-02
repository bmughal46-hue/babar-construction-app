import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. PAGE SETUP ---
st.set_page_config(
    page_title="Babar Real Estate | Construction Pro",
    page_icon="🏗️",
    layout="wide"
)

# --- 2. CUSTOM STYLE (Gold & Dark Theme) ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 5px solid #C5A059;
        text-align: center;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #e9ecef;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] { background-color: #C5A059 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC CALCULATIONS ---
def get_construction_data(plot_size, category, city):
    # Mapping sizes to sqft
    sqft_map = {"3 Marla": 675, "5 Marla": 1125, "8 Marla": 1800, "10 Marla": 2250, "1 Kanal": 4500}
    area = sqft_map[plot_size]
    
    # Base Rates (Per SqFt)
    rates = {"Grey Structure": 2400, "Standard (Grey + Finishing)": 4500, "Luxury Construction": 6500}
    city_factor = {"Lahore": 1.0, "Karachi": 1.05, "Islamabad": 1.1, "Gwadar": 1.15}
    
    base_rate = rates[category] * city_factor.get(city, 1.0)
    total = area * base_rate
    
    # Breakdown Data
    breakdown = {
        "Labour": total * 0.25,
        "Bricks & Sand": total * 0.20,
        "Cement": total * 0.12,
        "Steel (Sarya)": total * 0.15,
        "Finishing & Tiles": total * 0.28
    }
    return total, base_rate, area, breakdown

# --- 4. SIDEBAR (User Inputs) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/609/609803.png", width=80)
    st.title("BILAL MUGHAL")
    st.subheader("Construction Expert")
    st.divider()
    
    city = st.selectbox("Select City", ["Lahore", "Karachi", "Islamabad", "Gwadar"])
    c_type = st.radio("Construction Type", ["Grey Structure", "Standard (Grey + Finishing)", "Luxury Construction"])
    size = st.select_slider("Plot Size", options=["3 Marla", "5 Marla", "8 Marla", "10 Marla", "1 Kanal"])
    
    st.write("---")
    st.caption("Developed for Babar Real Estate & Builders")

# --- 5. MAIN DASHBOARD ---
st.header(f"🏗️ Construction Estimator - {city}")

total_cost, rate_sqft, total_area, breakdown_dict = get_construction_data(size, c_type, city)

# Top Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='metric-box'><h4>Total Estimate</h4><h2 style='color:#C5A059;'>PKR {total_cost/1000000:.2f}M</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-box'><h4>Cost per SqFt</h4><h2>PKR {rate_sqft:,.0f}</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-box'><h4>Total Area</h4><h2>{total_area} sqft</h2></div>", unsafe_allow_html=True)

st.write("---")

# Tabs for details
tab1, tab2, tab3 = st.tabs(["📊 Cost Breakdown", "🧱 Material Estimates", "📜 About Us"])

with tab1:
    st.subheader("Cost Distribution")
    df = pd.DataFrame(list(breakdown_dict.items()), columns=['Item', 'Cost'])
    
    # Modern Pie Chart (Simplified to avoid errors)
    fig = px.pie(df, values='Cost', names='Item', hole=0.4, 
                 color_discrete_sequence=px.colors.sequential.Gold)
    st.plotly_chart(fig, use_container_width=True)
    
    st.table(df.style.format({"Cost": "PKR {:,.0f}"}))

with tab2:
    st.subheader("Estimated Materials (Grey Structure Only)")
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("Cement Bags", f"{int(total_area * 0.45)} Bags")
    m_col2.metric("Bricks (Approx)", f"{int(total_area * 26)} Pcs")
    m_col3.metric("Steel (Sarya)", f"{round(total_area * 0.0035, 1)} Tons")

with tab3:
    st.subheader("Babar Real Estate & Builders")
    st.write("We provide premium construction services in Lahore and major cities of Pakistan.")
    st.button("Contact Bilal Mughal (WhatsApp)")

st.markdown("<br><hr><center>Property Portal Powered by Bilal Mughal © 2026</center>", unsafe_allow_html=True)
