import streamlit as st

# --- 1. SETTINGS ---
st.set_page_config(page_title="Babar Real Estate | CEO Portal", layout="wide")

# --- 2. SIDEBAR (CEO BRANDING) ---
with st.sidebar:
    st.image("images.jpeg", width=200) # Bilal Mughal (CEO)
    st.title("BILAL MUGHAL")
    st.caption("CEO - Babar Real Estate")
    st.write("---")
    menu = st.radio("MAIN MENU", 
        ["DHA Phase 1-13 Tracker", "Material Calculator", "Factory Products", "Client Database"])
    st.write("---")
    st.success("App Status: Live 🟢")

# --- 3. PAGE LOGIC ---

if menu == "DHA Phase 1-13 Tracker":
    st.title("📍 DHA PHASE 1 TO 13 - BLOCK DETAILS")
    
    # Phase Selection
    phase = st.selectbox("Select DHA Phase:", [f"DHA Phase {i}" for i in range(1, 14)])
    
    # Block Data (Sample logic for all phases)
    # Aap isme har phase ke blocks aur prices ki list barha sakte hain
    blocks_data = {
        "DHA Phase 1": ["Block A", "Block B", "Block C", "Block D"],
        "DHA Phase 5": ["Block G", "Block H", "Block J", "Block K", "Block L"],
        "DHA Phase 6": ["Block A", "Block B", "Block C", "Block D", "Block E", "Block H", "Block L"],
        "DHA Phase 7": ["Block P", "Block Q", "Block R", "Block S", "Block T"],
        "DHA Phase 8": ["Block S", "Block T", "Block U", "Block V", "Ivy Green"],
        "DHA Phase 9": ["Prism", "Town"],
    }
    
    current_blocks = blocks_data.get(phase, ["Block A", "Block B", "Block C"]) # Default blocks
    
    st.subheader(f"Current Status: {phase}")
    
    # Layout for Blocks
    cols = st.columns(3)
    for i, block in enumerate(current_blocks):
        with cols[i % 3]:
            st.info(f"*{block}*")
            st.write("Status: Possession Available")
            st.write(f"Latest Rate: Rs. {25 + i}.5 Million (Approx)")

elif menu == "Material Calculator":
    st.title("🏗️ ADVANCED CALCULATOR (WITH PRICES)")
    
    # Updated List with all Commercial & Residential Units
    selection = st.selectbox("Property Type:", [
        "3 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", 
        "1 Kanal", "2 Kanal", "4 Kanal",
        "4 Marla Commercial Building", "8 Marla Commercial Building", "16 Marla Commercial Building"
    ])
    
    # Rates (April 2026)
    r_bricks, r_cement, r_steel = 16, 1280, 268000
    
    # Simple Logic for heavy calculation
    m_map = {"3 Marla": 3, "5 Marla": 5, "1 Kanal": 20, "4 Marla Commercial Building": 8}
    m = m_map.get(selection, 10) # Default 10 if not in small map
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Bricks (Awal)", f"{4500*m:,}", f"Rs. {4500*m*r_bricks:,}")
    c2.metric("Cement (Bags)", f"{95*m:,}", f"Rs. {95*m*r_cement:,}")
    c3.metric("Steel (Tons)", f"{0.45*m}", f"Rs. {int(0.45*m*r_steel):,}")

elif menu == "Factory Products":
    st.title("🏭 BABAR FACTORY - PRODUCT AWARENESS")
    st.markdown("""
    ### 1. Awal Quality Bricks
    * *Detail:* Direct from kiln, water absorption < 15%.
    * *Awareness:* Hamesha 'Awal' brick use karein foundation ke liye.
    ### 2. Grade 60 Steel
    * *Detail:* Best for multi-story commercial buildings.
    """)

elif menu == "Client Database":
    st.title("👥 EXECUTIVE CLIENT LIST")
    st.table([
        {"Client": "Sheikh Nadeem Ahmad", "Project": "Crown City Gwadar", "Status": "VIP"},
        {"Client": "Chaudhary Mudasir", "Project": "Advocate Office", "Status": "Active"},
        {"Client": "Kiran Usman", "Project": "Express News Studio", "Status": "Completed"}
    ])
