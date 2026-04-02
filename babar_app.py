import streamlit as st

# --- 1. SETTINGS & SYNTAX FIX ---
st.set_page_config(page_title="Babar Real Estate | Zameen Edition", layout="wide")

# --- 2. ZAMEEN.COM STYLE CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stApp { max-width: 550px; margin: 0 auto; background: white; border: 1px solid #e1e4e7; }
    .property-card {
        background: white; border-radius: 12px; padding: 16px; margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); border-left: 6px solid #28a745;
    }
    .price-tag { color: #28a745; font-size: 22px; font-weight: 800; margin-bottom: 5px; }
    .loc-text { color: #666; font-size: 14px; margin-bottom: 10px; }
    .badge { background: #e8f5e9; color: #2e7d32; padding: 3px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; }
    .contact-btn { width: 100%; background: #28a745; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DYNAMIC INVENTORY ---
if 'ads' not in st.session_state:
    st.session_state.ads = [
        {"price": "3.40 Crore", "loc": "Phase 9 Prism, Sector C", "size": "1 Kanal", "type": "Residential"},
        {"price": "1.85 Crore", "loc": "Phase 7, Sector Z", "size": "10 Marla", "type": "Residential"}
    ]

# --- 4. NAVIGATION (DHA PLUS STYLE) ---
st.markdown("<h2 style='color:#003366; text-align:center;'>BABAR <span style='color:#28a745;'>GROUP</span></h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:12px;'>Elite SaaS Portal by Bilal Mughal</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏠 Buy", "🤖 AI Advisor", "🧮 Construction", "⚙️ Admin"])

# --- TAB 1: ZAMEEN STYLE LISTINGS ---
with tabs[0]:
    st.markdown("### Featured Properties 🔥")
    for ad in st.session_state.ads:
        st.markdown(f"""
        <div class="property-card">
            <div class="price-tag">PKR {ad['price']}</div>
            <div class="loc-text">📍 {ad['loc']}</div>
            <div style="margin-bottom:15px;">
                <span class="badge">{ad['size']}</span>
                <span class="badge">{ad['type']}</span>
                <span class="badge">Verified</span>
            </div>
            <button class="contact-btn">WhatsApp Bilal Mughal</button>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: AI AGENT ---
with tabs[1]:
    st.markdown("### 🤖 Babar AI Advisor")
    query = st.text_input("Investement ke bare mein pochein:")
    if query:
        st.info(f"Market Analysis: Based on Zameen trends, {query} suggests a high ROI in DHA Lahore Phase 6.")

# --- TAB 3: CONSTRUCTION CALCULATOR ---
with tabs[2]:
    st.markdown("### 🧮 Elite Estimator 2026")
    p_size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
    rate = 3450 # Current Lahore Rate
    area = {"5 Marla": 2100, "10 Marla": 3500, "1 Kanal": 6500}[p_size]
    total = (area * rate) / 1000000
    st.metric("Total Investment", f"PKR {total:.2f} Million")
    st.caption("Rate: 3,450/sqft (Grey Structure)")

# --- TAB 4: ADMIN PANEL (ADS MANAGEMENT) ---
with tabs[3]:
    st.markdown("### ⚙️ Inventory Control")
    with st.form("admin_form"):
        p = st.text_input("Price (e.g. 2.10 Crore)")
        l = st.text_input("Full Location")
        s = st.selectbox("Size", ["5 Marla", "10 Marla", "1 Kanal"])
        if st.form_submit_button("Post Ad Globally"):
            st.session_state.ads.insert(0, {"price": p, "loc": l, "size": s, "type": "Residential"})
            st.success("Ad Live ho chuki hai!")

st.markdown("<br><center><p style='color:#999; font-size:10px;'>Babar Real Estate v17.0 | April 2026</p></center>", unsafe_allow_html=True)
