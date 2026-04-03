import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# 2. Construction Material Calculation Logic
def get_material_estimates(size_label):
    # Base rates per Marla
    base_bricks = 4500
    base_cement = 90
    base_steel = 0.4
    base_bajri = 90

    multipliers = {
        "3 Marla": 3,
        "4 Marla": 4,
        "4 Marla Building": 5.5,
        "5 Marla": 5,
        "7 Marla": 7,
        "8 Marla": 8,
        "8 Marla Building": 10.5,
        "10 Marla": 10,
        "16 Marla Building": 20,
        "1 Kanal": 20,
        "2 Kanal": 40,
        "4 Kanal": 80,
        "4 Kanal Commercial": 100
    }

    m = multipliers.get(size_label, 0)
    
    return {
        "Bricks": int(base_bricks * m),
        "Cement": int(base_cement * m),
        "Steel": round(base_steel * m, 2),
        "Bajri": int(base_bajri * m)
    }

# 3. User Interface
st.title("BABAR REAL ESTATE & CONSTRUCTION")

options = [
    "3 Marla", "4 Marla", "4 Marla Building", "5 Marla", 
    "7 Marla", "8 Marla", "8 Marla Building", "10 Marla", 
    "16 Marla Building", "1 Kanal", "2 Kanal", 
    "4 Kanal", "4 Kanal Commercial"
]

selected_size = st.selectbox("Select Property Size:", options)

if selected_size:
    res = get_material_estimates(selected_size)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Bricks (Awal)", f"{res['Bricks']:,}")
    col2.metric("Cement Bags", f"{res['Cement']:,}")
    col3.metric("Steel (Tons)", f"{res['Steel']}")
    col4.metric("Bajri (Cft)", f"{res['Bajri']:,}")
