import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Babar Real Estate & Construction", layout="wide", page_icon="🏗️")

# --- Custom Styling (Heavy Look) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .header-style { font-size: 40px; font-weight: bold; color: #1e3d59; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar / Navigation ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Babar Real Estate Logo") # Yahan apna logo link dalien
    st.title("CEO PORTAL")
    st.write("---")
    page = st.radio("Navigation", ["Material Calculator", "Project Reports", "Client Database"])

# --- Calculation Logic ---
def calculate_material(size):
    # Base Values per Marla
    base = {"bricks": 4500, "cement": 95, "steel": 0.45, "bajri": 100}
    
    # Mapping and Multipliers
    multipliers = {
        "3 Marla": 3, "5 Marla": 5, "7 Marla": 7, "8 Marla": 8, "10 Marla": 10,
        "1 Kanal": 20, "2 Kanal": 40, "4 Kanal": 80,
        "4 Marla Commercial": 6.5,
        "8 Marla Commercial": 13,
        "16 Marla Commercial": 26
    }
    
    m = multipliers.get(size, 0)
    return {k: round(v * m, 1) for k, v in base.items()}

# --- Main Page Content ---
if page == "Material Calculator":
    st.markdown('<div class="header-style">BABAR REAL ESTATE & CONSTRUCTION</div>', unsafe_allow_html=True)
    
    # Selection Row
    col_a, col_b = st.columns([2, 1])
    with col_a:
        selection = st.selectbox("Select Property Size or Commercial Unit:", [
            "3 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", 
            "1 Kanal", "2 Kanal", "4 Kanal",
            "4 Marla Commercial", "8 Marla Commercial", "16 Marla Commercial"
        ])
    
    st.write("---")
    
    # Results Display
    data = calculate_material(selection)
    
    st.subheader(f"📊 Material Estimate for {selection}")
    m1, m2, m3, m4 = st.columns(4)
    
    m1.metric("Bricks (Awal)", f"{int(data['bricks']):,}")
    m2.metric("Cement (Bags)", f"{int(data['cement']):,}")
    m3.metric("Steel (Tons)", f"{data['steel']}")
    m4.metric("Bajri (Cft)", f"{int(data['bajri']):,}")

    st.write("---")
    
    # Additional Features (Heavy Level)
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 *Pro Tip:* Commercial buildings require 25% more steel for foundation strength.")
    with col2:
        st.success("✅ Rates updated according to current market standards (April 2026).")

elif page == "Project Reports":
    st.header("Project Status")
    st.warning("Feature under development...")
