import streamlit as st
import pandas as pd

# --- 1. GLOBAL SETTINGS & STYLING ---
st.set_page_config(page_title="Babar Real Estate | CEO Portal", layout="wide", page_icon="🏗️")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-top: 5px solid #1a73e8; }
    .css-10trblm { color: #1a73e8 !important; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e3192, #1bffff); color: white; }
    .z-header { font-size: 32px; font-weight: bold; color: #004d40; border-bottom: 3px solid #8bc34a; padding-bottom: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (CEO BRANDING & NAVIGATION) ---
with st.sidebar:
    try:
        st.image("images.jpeg", width=220, caption="BILAL MUGHAL - CEO")
    except:
        st.error("CEO Photo (images.jpeg) missing in GitHub!")
    
    st.title("Main Menu")
    menu = st.radio("Go to:", [
        "Dashboard Home", 
        "DHA Phase Tracker (All Cities)", 
        "Material & Cost Calculator", 
        "Factory Inventory & Rates", 
        "VIP Client Database",
        "Project Reports"
    ])
    st.write("---")
    st.markdown("### 📞 Helpline\n+92 300 1234567")
    st.success("Server Status: Active 🟢")

# --- 3. DATA ENGINE ---
market_rates = {"Bricks": 16.5, "Cement": 1320, "Steel": 272000, "Bajri": 118}

# Comprehensive DHA Data
dha_registry = {
    "DHA Lahore": [f"Phase {i}" for i in range(1, 14)],
    "DHA Bahawalpur": ["Sector A", "Sector B", "Sector C", "Sector N", "Villas"],
    "DHA Multan": ["Sector A", "Sector H", "Sector M", "Sector R", "Rumanza"],
    "DHA Quetta": ["Sector A", "Sector B", "Early Bird", "Smart City"],
    "DHA Gujranwala": ["Phase 1", "Commercial Zone", "Executive Block"]
}

# --- 4. PAGE LOGIC ---

if menu == "Dashboard Home":
    st.markdown('<div class="z-header">WELCOME TO BABAR REAL ESTATE PORTAL</div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Active Projects", "24", "+2 New")
    c2.metric("Total Clients", "1,450", "Active")
    c3.metric("Inventory Value", "Rs. 4.2B", "+15%")
    c4.metric("Market Sentiment", "Bullish 📈")
    
    st.image("https://images.unsplash.com/photo-1582408921715-18e7806365c1?auto=format&fit=crop&w=1200", caption="Zameen.com Style Property Insights")

elif menu == "DHA Phase Tracker (All Cities)":
    st.markdown('<div class="z-header">📍 ALL PAKISTAN DHA TRACKER</div>', unsafe_allow_html=True)
    city_col, phase_col = st.columns(2)
    
    with city_col:
        city = st.selectbox("Select City", list(dha_registry.keys()))
    with phase_col:
        phase = st.selectbox("Select Phase/Sector", dha_registry[city])
    
    st.write(f"### Showing Details for {city} - {phase}")
    blocks = ["Block A", "Block B", "Block C", "Block D", "Block E"]
    
    cols = st.columns(3)
    for i, b in enumerate(blocks):
        with cols[i % 3]:
            st.info(f"*{b}*")
            st.write("Status: Possession / Developed")
            st.write(f"Avg Price: Rs. {22 + i}.4 Million")

elif menu == "Material & Cost Calculator":
    st.markdown('<div class="z-header">🏗️ MATERIAL & COST ESTIMATOR (APRIL 2026)</div>', unsafe_allow_html=True)
    
    unit = st.selectbox("Property Category:", [
        "5 Marla Residential", "10 Marla Residential", "1 Kanal Residential", "2 Kanal Residential",
        "4 Marla Commercial Building", "8 Marla Commercial Building", "16 Marla Commercial Building"
    ])
    
    m_map = {"5 Marla": 5, "10 Marla": 10, "1 Kanal": 20, "2 Kanal": 40, "4 Marla Commercial": 10, "8 Marla Commercial": 20, "16 Marla Commercial": 40}
    m = next((v for k, v in m_map.items() if k in unit), 10)
    
    st.write("---")
    res = {"Bricks": 4600 * m, "Cement": 98 * m, "Steel": 0.48 * m, "Bajri": 110 * m}
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bricks (Qty)", f"{int(res['Bricks']):,}", f"Rs.{int(res['Bricks']*market_rates['Bricks']):,}")
    c2.metric("Cement (Bags)", f"{int(res['Cement']):,}", f"Rs.{int(res['Cement']*market_rates['Cement']):,}")
    c3.metric("Steel (Tons)", f"{res['Steel']:.2f}", f"Rs.{int(res['Steel']*market_rates['Steel']):,}")
    c4.metric("Bajri (Cft)", f"{int(res['Bajri']):,}", f"Rs.{int(res['Bajri']*market_rates['Bajri']):,}")

elif menu == "Factory Inventory & Rates":
    st.markdown('<div class="z-header">🏭 BABAR FACTORY INVENTORY</div>', unsafe_allow_html=True)
    st.table([
        {"Item": "Awal Brick (Special)", "Stock": "500,000", "Current Rate": f"Rs. {market_rates['Bricks']}"},
        {"Item": "Grade 60 Steel", "Stock": "120 Tons", "Current Rate": f"Rs. {market_rates['Steel']}"},
        {"Item": "Premium Bajri (Sargodha)", "Stock": "5,000 Cft", "Current Rate": f"Rs. {market_rates['Bajri']}"}
    ])
    st.info("💡 Awareness: Commercial buildings require reinforced piling. Consult our engineer for 16 Marla projects.")

elif menu == "VIP Client Database":
    st.markdown('<div class="z-header">👥 EXECUTIVE CLIENTS</div>', unsafe_allow_html=True)
    clients = [
        {"Name": "Malik Riaz Ahmad", "Project": "Bahria Executive", "Category": "Gold"},
        {"Name": "Mian Mansha Sahab", "Project": "Gulberg Greens", "Category": "Platinum"},
        {"Name": "Sardar Usman Buzdar", "Project": "Taunsa Development", "Category": "Silver"},
        {"Name": "Chaudhary Pervaiz Elahi", "Project": "Gujrat Industrial Zone", "Category": "Gold"}
    ]
    st.table(clients)

elif menu == "Project Reports":
    st.markdown('<div class="z-header">📑 LIVE PROJECT STATUS</div>', unsafe_allow_html=True)
    st.json({
        "DHA Phase 6 Villa": "Finishing Stage",
        "Bahawalpur Commercial Hub": "Structure Complete",
        "Multan Rumanza Plot 12": "Land Clearing",
        "Quetta Smart Block": "Planning Phase"
    })
