import streamlit as st

# ----------------------------
# 1. PAGE CONFIG & BRANDING
# ----------------------------
st.set_page_config(page_title="Babar Real Estate | Super App", layout="wide", page_icon="🏠")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); border-top: 4px solid #C5A059; }
    .stButton>button { background-color: #C5A059; color: white; width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# ----------------------------
# 2. SIDEBAR NAVIGATION
# ----------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/609/609803.png", width=80)
    st.title("Babar Real Estate")
    st.caption("CEO: Bilal Mughal")
    st.divider()
    menu = st.radio("Main Menu", ["📊 Dashboard", "🧮 Construction Calculator", "🤖 AI Advisor", "📈 Market Insights"])
    st.divider()
    st.info("Direct WhatsApp: +92 3XX XXXXXXX")

# ----------------------------
# 3. DASHBOARD
# ----------------------------
if menu == "📊 Dashboard":
    st.title("🏠 Babar Real Estate Super App")
    st.markdown("#### Buy | Sell | Invest | Construct")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("5 Marla Avg Price", "1.2 – 1.8 Cr", delta="DHA Ph 9")
    with col2:
        st.metric("10 Marla Avg Price", "2.8 – 4.5 Cr", delta="DHA Ph 6")
    with col3:
        st.metric("1 Kanal Avg Price", "5.5 – 9.0 Cr", delta="DHA Ph 7")
    
    st.write("---")
    st.subheader("Latest Listings")
    st.write("📍 *DHA Phase 6:* 1 Kanal Plot - Hot Location (Demand 6.5 Cr)")
    st.write("📍 *DHA Phase 9 Prism:* 5 Marla Plot - Near Possession (Demand 1.4 Cr)")

# ----------------------------
# 4. CONSTRUCTION CALCULATOR
# ----------------------------
elif menu == "🧮 Construction Calculator":
    st.title("🧮 Smart Construction Estimator (2026)")
    
    c1, c2 = st.columns(2)
    with c1:
        plot_size = st.selectbox("Select Plot Size", ["3 Marla", "5 Marla", "7 Marla", "8 Marla", "10 Marla", "1 Kanal", "2 Kanal"])
        floors = st.selectbox("Construction Type", ["Double Story (G+1)", "Single Story", "Basement + G + 1"])
    
    with c2:
        # Standard sqft mapping
        sqft_defaults = {"3 Marla": 1350, "5 Marla": 2100, "7 Marla": 2700, "8 Marla": 3100, "10 Marla": 3500, "1 Kanal": 6500, "2 Kanal": 11500}
        covered_area = st.number_input("Total Covered Area (sqft)", value=sqft_defaults[plot_size])

    # 2026 Actual Rates
    rate = st.slider("Grey Structure Rate (PKR/sqft)", 3300, 3800, 3450)
    total_cost = covered_area * rate

    st.divider()
    col_a, col_b = st.columns(2)
    col_a.success(f"*Total Covered Area:* {covered_area:,} sqft")
    col_b.success(f"*Estimated Grey Cost:* PKR {total_cost/1000000:.2f} Million")

    # MATERIAL ESTIMATION Logic
    st.subheader("🧱 Required Material (Grey Structure)")
    m1, m2, m3 = st.columns(3)
    m1.metric("Cement Bags", f"{int(covered_area * 0.45):,}")
    m2.metric("Bricks (Awwal)", f"{int(covered_area * 26):,}")
    m3.metric("Steel (Tons)", f"{round(covered_area * 0.0038, 2)}")
    
    st.caption("Recommendations: Lucky/Bestway Cement | Mughal/Ittehad Grade-60 Steel")

# ----------------------------
# 5. AI ADVISOR
# ----------------------------
elif menu == "🤖 AI Advisor":
    st.title("🤖 Babar AI Property Advisor")
    user_query = st.text_input("Ask about investment, phases, or rates (e.g., 'Where to invest in DHA?')")

    if user_query:
        q = user_query.lower()
        if "phase 6" in q:
            st.success("Phase 6 is the gold standard. High rental yield and 100% secure.")
        elif "prism" in q or "phase 9" in q:
            st.success("9 Prism is best for investment. Possession is coming, prices will jump 20%.")
        elif "commercial" in q:
            st.success("Commercial in Phase 7 & 8 Broadway is hot right now. High ROI.")
        else:
            st.info("General Advice: 2026 is the year of 'Construct & Sell'. Buy 5 Marla, build A+ quality, and sell for 30% profit.")

# ----------------------------
# 6. MARKET INSIGHTS
# ----------------------------
elif menu == "📈 Market Insights":
    st.title("📊 Market Trends (DHA Lahore)")
    st.markdown("### 🔥 Hot Sectors This Month")
    st.write("✅ *Phase 9 Prism:* Sector Q & R (High demand)")
    st.write("✅ *Phase 7:* Sector Y (Construction hub)")
    st.write("✅ *Phase 6:* Sector M (Premium Living)")
    
    st.divider()
    st.success("""
    *Investment Strategy by Bilal Mughal:*
    1. Buy plot in 'Developing' phase.
    2. Start construction immediately (Beat inflation).
    3. Use premium materials (Increases resale value).
    4. Resale profit margin: *25% - 40%* in current market.
    """)

st.markdown("<br><hr><center>Powered by Bilal Mughal | Babar Real Estate © 2026</center>", unsafe_allow_html=True)
