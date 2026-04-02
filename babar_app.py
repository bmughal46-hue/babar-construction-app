import streamlit as st

# --- 1. CONFIG ---
st.set_page_config(page_title="Babar Real Estate", layout="wide")

# Session States
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- 2. PREMIUM UI ---
st.markdown("""
    <style>
    .stApp { max-width: 500px; margin: 0 auto; background: white; border: 1px solid #ddd; }
    .welcome-banner { background: #e8f5e9; color: #2e7d32; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; margin-bottom: 20px; border: 1px solid #a5d6a7; }
    .header-style { background: #003366; color: white; padding: 20px; text-align: center; border-radius: 0 0 15px 15px; }
    .whatsapp-footer { position: fixed; bottom: 0; width: 100%; max-width: 500px; background: #25D366; color: white; text-align: center; padding: 10px; font-weight: bold; z-index: 100; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<div class='header-style'><h2>BABAR REAL ESTATE</h2><p style='font-size:12px;'>DHA Phase 8 Broadway, Lahore</p></div>", unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["🏡 Home", "🤖 AI", "🧮 Calc", "⚙️ Admin"])

# --- ADMIN TAB (Yahan Welcome Message aayega) ---
with tab4:
    if not st.session_state.logged_in:
        st.subheader("Admin Login")
        u = st.text_input("User ID")
        p = st.text_input("Password", type="password")
        if st.button("Login"):
            if u == "admin" and p == "babar123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Login")
    else:
        # --- YE RAHI AAPKI REQUESTED TABDEELI ---
        st.markdown("<div class='welcome-banner'>🌟 Welcome to Babar Mughal (CEO)</div>", unsafe_allow_html=True)
        st.success("Admin Access Granted. You can now manage all listings.")
        
        with st.form("post_ad"):
            st.write("📢 *Post New Property Ad*")
            price = st.text_input("Price (e.g. 3.30 Crore)")
            loc = st.text_input("Location")
            if st.form_submit_button("Publish Now"):
                st.info(f"Ad for {loc} has been queued for publishing.")
        
        if st.button("Secure Logout"):
            st.session_state.logged_in = False
            st.rerun()

# --- OTHER TABS (Sari App) ---
with tab1:
    st.write("### Featured Listings")
    st.info("Listings will appear here once published from Admin.")

with tab2:
    st.write("### AI Property Advisor")
    st.caption("Ask Bilal Mughal's AI anything about DHA market.")

with tab3:
    st.write("### Construction Bill Generator")
    st.caption("Generate official estimates for your clients.")

# --- FOOTER ---
st.markdown("<div class='whatsapp-footer'>WhatsApp: Babar Mughal (+92 324 4000041)</div>", unsafe_allow_html=True)
