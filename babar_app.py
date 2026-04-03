import streamlit as st

# --- 1. THEME & CUSTOM CSS (Zameen.com Style) ---
st.set_page_config(page_title="Babar Real Estate | CEO Portal", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f5; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 5px solid #002e5b; }
    .cost-card { 
        background-color: #ffffff; padding: 20px; border-radius: 12px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-left: 5px solid #c5a059; 
        margin-bottom: 20px; 
    }
    .total-box { 
        background: linear-gradient(135deg, #002e5b 0%, #0b5394 100%); 
        color: white; padding: 30px; border-radius: 20px; 
        text-align: center; border: 2px solid #c5a059; 
    }
    .sidebar .sidebar-content { background-color: #002e5b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (CEO BRANDING - BILAL MUGHAL) ---
with st.sidebar:
    try:
        st.image("images.jpeg", width=220) # Bilal Mughal CEO Pic
    except:
        st.info("CEO Profile Picture 'images.jpeg' load ho rahi hai...")
    
    st.title("BILAL MUGHAL")
    st.markdown("<p style='color:#c5a059; font-weight:bold;'>CEO & Founder</p>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio("NAVIGATION", [
        "Dashboard Home", 
        "DHA All Pakistan Tracker", 
        "Construction Cost Optimizer", 
        "Factory Inventory", 
        "VIP Client Database"
    ])
    st.write("---")
    st.success("System: Connected 🟢")

# --- 3. DATA & LOGIC ---
if menu == "Dashboard Home":
    st.title("🏛️ Babar Real Estate Executive Dashboard")
    st.markdown("### Welcome back, Bilal Mughal.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Projects", "18", "+2")
    col2.metric("Market Trend", "High", "DHA Lahore")
    col3.metric("Pending Quotes", "5", "Action Required")
    st.image("https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200", caption="Zameen Property Overview")

elif menu == "DHA All Pakistan Tracker":
    st.header("📍 All Pakistan DHA Phase & Block Tracker")
    city = st.selectbox("Select City", ["Lahore", "Multan", "Bahawalpur", "Quetta", "Gujranwala"])
    phase = st.selectbox("Select Phase", [f"Phase {i}" for i in range(1, 14)])
    
    st.write(f"### {city} - {phase} Block Details")
    c1, c2, c3 = st.columns(3)
    for i, b in enumerate(["Block A", "Block B", "Block C", "Block D"]):
        with [c1, c2, c3][i % 3]:
            st.info(f"*{b}* - Possession Available")

elif menu == "Construction Cost Optimizer":
    st.header("🏗️ Pro Construction Cost Optimizer")
    
    col_inp1, col_inp2, col_inp3 = st.columns(3)
    with col_inp1:
        p_size = st.selectbox("Plot Size", [
            "3 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", 
            "16 Marla Building", "1 Kanal", "2 Kanal", "4 Kanal"
        ])
    with col_inp2:
        quality = st.select_slider("Quality", options=["Economy", "Standard", "Premium"])
    with col_inp3:
        finish_type = st.radio("Scope", ["Grey Structure Only", "Full Finishing"])

    # Calculation logic
    m_map = {"3 Marla":3, "5 Marla":5, "7 Marla":7, "8 Marla":8, "10 Marla":10, "16 Marla Building":25, "1 Kanal":20}
    num_marlas = m_map.get(p_size, 10)
    q_mult = {"Economy": 0.9, "Standard": 1.0, "Premium": 1.25}[quality]
    
    bricks = int(num_marlas * 4500 * q_mult)
    cement = int(num_marlas * 95 * q_mult)
    steel = round(num_marlas * 0.45 * q_mult, 2)
    
    grand_total = (bricks * 26) + (cement * 1280) + (steel * 270000)

    st.markdown(f"""
        <div class="total-box">
            <h4 style="color:#c5a059; margin:0;">ESTIMATED PROJECT BUDGET</h4>
            <h1 style="font-size:50px; margin:10px 0;">Rs. {int(grand_total):,}</h1>
        </div>
    """, unsafe_allow_html=True)

    st.write("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="cost-card"><h3>🧱 Bricks</h3><h2>{bricks:,}</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="cost-card"><h3>🧪 Cement</h3><h2>{cement:,}</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="cost-card"><h3>🏗️ Steel</h3><h2>{steel} T</h2></div>', unsafe_allow_html=True)

elif menu == "VIP Client Database":
    st.header("👥 Executive Client Database")
    st.table([
        {"Name": "Sheikh Nadeem Ahmad", "Project": "Crown City", "Status": "VIP"},
        {"Name": "Chaudhary Mudasir", "Project": "Advocate Complex", "Status": "Active"},
        {"Name": "Kiran Usman", "Project": "Express News Studio", "Status": "Completed"}
    ])

elif menu == "Factory Inventory":
    st.header("🏭 Factory Awareness & Rates")
    st.write("Current Awal Brick Rate: *Rs. 26*")
    st.write("Current Steel Rate: *Rs. 270,000 / Ton*")
