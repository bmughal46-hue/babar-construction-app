import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Babar Group | Construction Intelligence", layout="wide")

# 2. Premium UI Styling
st.markdown("""
<style>
    .main { background-color: #022c22; }
    [data-testid="stSidebar"] { background-color: #064e3b !important; border-right: 2px solid #fbbf24; }
    [data-testid="stSidebar"] * { color: #fef3c7 !important; }
    .header-box { 
        background: linear-gradient(135deg, #064e3b 0%, #022c22 100%); 
        padding: 25px; border-radius: 15px; text-align: center; 
        border: 1px solid #fbbf24; margin-bottom: 20px;
    }
    .card { 
        background: #ffffff; padding: 20px; border-radius: 15px; 
        box-shadow: 0 4px 15px rgba(0,0,0,0.3); border-top: 6px solid #fbbf24;
        margin-bottom: 20px; color: #1e293b;
    }
    .brand-badge {
        background: #fef3c7; color: #92400e; padding: 5px 12px;
        border-radius: 20px; font-weight: bold; font-size: 14px;
        border: 1px solid #fbbf24; display: inline-block; margin: 5px;
    }
    .stButton>button {
        background-color: #fbbf24 !important; color: #022c22 !important;
        font-weight: bold; width: 100%; border-radius: 10px; border: none;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Profile
st.sidebar.markdown(f"<h2 style='color:#fbbf24;'>BABAR GROUP</h2>", unsafe_allow_html=True)
st.sidebar.write(f"*CEO:* Bilal Mughal")
st.sidebar.write("📞 0324-4000041")
st.sidebar.markdown("---")
menu = st.sidebar.radio("SYSTEM MENU", [
    "🏗️ Construction Estimator", 
    "🏭 Ultimate Brand Directory",
    "📝 Client Lead Manager", 
    "📞 Contact Us"
])

# --- DATA ENGINE ---
prop_data = {
    "3 Marla": {"sqft": 1100, "bricks": 35000, "steel": 2.5, "cement": 650, "sand": 3200, "crush": 1600},
    "5 Marla": {"sqft": 1800, "bricks": 56000, "steel": 3.8, "cement": 1150, "sand": 5500, "crush": 2800},
    "7 Marla": {"sqft": 2400, "bricks": 75000, "steel": 5.2, "cement": 1500, "sand": 7200, "crush": 3600},
    "8 Marla": {"sqft": 2800, "bricks": 88000, "steel": 6.1, "cement": 1800, "sand": 8500, "crush": 4200},
    "10 Marla": {"sqft": 3400, "bricks": 98000, "steel": 7.5, "cement": 1950, "sand": 10500, "crush": 5200},
    "1 Kanal": {"sqft": 5500, "bricks": 175000, "steel": 14.5, "cement": 3200, "sand": 18000, "crush": 9000},
    "4 Marla Commercial": {"sqft": 4500, "bricks": 120000, "steel": 12.0, "cement": 2500, "sand": 14000, "crush": 7000}
}

if menu == "🏗️ Construction Estimator":
    st.markdown('<div class="header-box"><h1 style="color:#fbbf24;">Babar Group Estimator</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    p_size = st.selectbox("Select Plot Size", list(prop_data.keys()))
    cost = prop_data[p_size]["sqft"] * 5200 # Updated base rate
    st.write(f"### Total Investment: *PKR {cost/10000000:.2f} Cr*")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"🧱 *Bricks (Gutka):* {prop_data[p_size]['bricks']:,}")
        st.write(f"🏗️ *Steel (Loha):* {prop_data[p_size]['steel']} Tons")
        st.write(f"🥡 *Cement:* {prop_data[p_size]['cement']:,} Bags")
    with col2:
        st.write(f"⏳ *Sand (Ravi):* {prop_data[p_size]['sand']:,} cft")
        st.write(f"⛰️ *Crush (Bajri):* {prop_data[p_size]['crush']:,} cft")
        st.write(f"⚡ *Electric:* Pakistan Cables")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🏭 Ultimate Brand Directory":
    st.markdown('<div class="header-box"><h1 style="color:#fbbf24;">Official Material Partners</h1></div>', unsafe_allow_html=True)
    
    brands = {
        "🏗️ Steel (Sariya)": ["Mughal Steel (G-60)", "Amreli Steels", "Ittehad Steel"],
        "🥡 Cement": ["Maple Leaf", "Bestway", "Lucky Cement", "DG Khan"],
        "🧱 Bricks & Aggregates": ["A-Grade Gutka (Sargodha)", "Ravi Sand", "Lawrencepur Sand"],
        "⚡ Cables & Electric": ["Pakistan Cables", "Fast Cables", "GM Cables"],
        "🎨 Paint & Finish": ["Jotun", "Dulux", "Brighto"],
        "🚿 Sanitary & Tiles": ["Master Tiles", "Faisal Tiles", "Porta", "Sonex"],
        "🪟 Windows & Glass": ["Chawla Aluminium", "Prime Aluminium", "Ghani Glass"]
    }
    
    for category, list_names in brands.items():
        st.markdown(f'<div class="card"><h4>{category}</h4>', unsafe_allow_html=True)
        for b in list_names:
            st.markdown(f'<span class="brand-badge">{b}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📝 Client Lead Manager":
    st.markdown('<div class="header-box"><h1 style="color:#fbbf24;">Client Inventory</h1></div>', unsafe_allow_html=True)
    # Form logic same as before...
    st.info("Leads management system is active.")

elif menu == "📞 Contact Us":
    st.markdown('<div class="header-box"><h1 style="color:#fbbf24;">Get In Touch</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="card" style="text-align: center;">', unsafe_allow_html=True)
    st.write("### 🏢 Babar Real Estate & Builders")
    st.write("📍 DHA Phase 6, Lahore, Pakistan")
    st.write("📞 *Phone:* 0324-4000041")
    st.write("✉️ *CEO:* Bilal Mughal")
    st.markdown("---")
    st.button("Chat on WhatsApp")
    st.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center;'>Post By Bilal Mughal</p>", unsafe_allow_html=True)