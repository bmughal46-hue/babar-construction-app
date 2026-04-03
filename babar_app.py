import streamlit as st

# --- CONSTRUCTION LOGIC DATA ---
# Average material required per marla (Standard Gray Structure)
material_data = {
    "Bricks": 4500,        # per marla
    "Cement Bags": 90,     # per marla
    "Sand (Cft)": 200,      # per marla
    "Crush/Bajri (Cft)": 90, # per marla
    "Steel (Tons)": 0.4     # per marla
}

with tab4: # Naya Tab: Babar Construction
    st.header("🏗️ Babar Construction | Cost & Material Estimator")
    st.info("Get precise estimates for your DHA Dream Home or Commercial Project.")

    # Selection Row
    col_a, col_b = st.columns(2)
    with col_a:
        p_type = st.selectbox("Project Type", ["Residential Home", "Commercial Building"])
    with col_b:
        p_size = st.selectbox("Plot Size", [
            "3 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", 
            "1 Kanal", "2 Kanal", "4 Kanal", "8 Marla Commercial", "4 Kanal Commercial"
        ])

    # Manual multiplier based on size
    size_num = float(p_size.split()[0])
    
    # Calculations
    total_bricks = int(size_num * material_data["Bricks"])
    total_cement = int(size_num * material_data["Cement Bags"])
    total_steel = round(size_num * material_data["Steel (Tons)"], 2)
    total_bajri = int(size_num * material_data["Crush/Bajri (Cft)"])

    # Display Results in Cards
    st.subheader(f"📊 Estimated Material for {p_size} {p_type}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bricks (Awal)", f"{total_bricks:,}")
    c2.metric("Cement Bags", f"{total_cement:,}")
    c3.metric("Steel (Sarya)", f"{total_steel} Tons")
    c4.metric("Crush (Bajri)", f"{total_bajri:,} Cft")

    st.markdown("---")
    
    # --- BRAND AWARENESS SECTION ---
    st.subheader("🛠️ Recommended Premium Brands (Quality Awareness)")
    st.write("Babar Construction recommends only the best for DHA structures:")
    
    brand_col1, brand_col2, brand_col3 = st.columns(3)
    with brand_col1:
        st.markdown("*Cement:*")
        st.write("- Maple Leaf Cement\n- Bestway Cement\n- Lucky Cement")
    with brand_col2:
        st.markdown("*Steel (Grade 60):*")
        st.write("- Ittehad Steel\n- Mughal Steel\n- Amreli Steels")
    with brand_col3:
        st.markdown("*Electric & Fittings:*")
        st.write("- Pakistan Cables\n- Fast Cables\n- GM Cables")

    # Call to Action
    st.success(f"📞 Want a detailed quote for your {p_size} project? Contact CEO Bilal Mughal: 0324-4000041")
