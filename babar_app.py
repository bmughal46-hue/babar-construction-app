import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- 1. CONFIG & BRANDING ---
st.set_page_config(page_title="Babar Real Estate | SaaS", layout="wide", page_icon="🏠")

# Custom CSS for Premium SaaS UI
st.markdown("""
    <style>
    .main { background-color: #f1f5f9; }
    .stMetric { background-color: white; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); border-left: 5px solid #C5A059; }
    .sidebar .sidebar-content { background-image: linear-gradient(#1e293b,#0f172a); }
    .brand-title { color: #C5A059; font-size: 32px; font-weight: 800; letter-spacing: -1px; }
    .footer { text-align: center; padding: 20px; color: #64748b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA ENGINE (Built-in for Stability) ---
# In a real SaaS, this would come from a Database (PostgreSQL/MySQL)
raw_data = {
    'PlotNumber': ['102-J', '45-A', '205-M', '12-Q', '88-CCA'],
    'Phase': ['Phase 6', 'Phase 7', 'Phase 8', 'Phase 9 Prism', 'Phase 6 Commercial'],
    'PlotSize': ['1 Kanal', '10 Marla', '5 Marla', '5 Marla', '4 Marla'],
    'Price': ['7.5 Cr', '3.8 Cr', '1.9 Cr', '1.3 Cr', '12.0 Cr'],
    'Lat': [31.4697, 31.4395, 31.4900, 31.4100, 31.4720],
    'Lon': [74.4500, 74.4700, 74.5100, 74.4900, 74.4550]
}
df = pd.DataFrame(raw_data)

# --- 3. HEADER (CEO + LOGO) ---
h_col1, h_col2 = st.columns([4, 1])
with h_col1:
    st.markdown("<div class='brand-title'>BABAR REAL ESTATE & BUILDERS</div>", unsafe_allow_html=True)
    st.caption("The Most Advanced Real Estate SaaS Platform in Pakistan")
with h_col2:
    # Generic Avatar for CEO (Replace URL with your hosted photo later)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.caption("Bilal Mughal (CEO)")

st.divider()

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### 🛠️ SaaS Control Center")
    choice = st.radio("Navigation", [
        "Dashboard", 
        "Interactive Maps", 
        "AI Property Advisor", 
        "Smarter Calculator", 
        "Saved Plots", 
        "Admin Panel", 
        "Ads Management"
    ])
    st.divider()
    st.info("System Status: Online 🟢")

# --- 5. FEATURE LOGIC ---

# --- DASHBOARD ---
if choice == "Dashboard":
    st.subheader("🚀 Real-Time Market Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Active Listings", "1,240", "+12")
    m2.metric("Avg 1 Kanal (Ph 6)", "7.2 Cr", "Stable")
    m3.metric("ROI Potential", "18.5%", "High")
    m4.metric("New Leads", "48", "+5")
    
    st.write("### Recent Hot Listings")
    st.dataframe(df, use_container_width=True)

# --- MAPS ---
elif choice == "Interactive Maps":
    st.title("🗺️ DHA Smart Map Interface")
    st.write("Visualizing inventory across DHA Lahore Phases.")
    
    m = folium.Map(location=[31.4500, 74.4600], zoom_start=12, tiles="CartoDB positron")
    for _, row in df.iterrows():
        folium.Marker(
            [row['Lat'], row['Lon']], 
            popup=f"<b>{row['PlotNumber']}</b><br>{row['Phase']}<br>Price: {row['Price']}",
            tooltip=row['Phase'],
            icon=folium.Icon(color='orange', icon='info-sign')
        ).add_to(m)
    
    st_folium(m, width=1100, height=550)

# --- AI ADVISOR ---
elif choice == "AI Property Advisor":
    st.title("🤖 Babar AI Advisor (GPT-4 Powered)")
    st.write("Ask anything about DHA investment strategies.")
    user_input = st.text_input("Example: Is Phase 9 Prism good for 1-year investment?")
    
    if user_input:
        with st.spinner("AI is analyzing market trends..."):
            # Simulation of AI Response (Integrate OpenAI API here)
            st.chat_message("assistant").write(f"Based on 2026 data, '{user_input}' suggests a high ROI strategy. Bilal Mughal recommends focusing on 'Construct & Sell' in developing sectors.")

# --- CALCULATOR ---
elif choice == "Smarter Calculator":
    st.title("🧮 Advanced Construction & Investment Calc")
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        size = st.selectbox("Plot Size", ["5 Marla", "10 Marla", "1 Kanal"])
        target = st.radio("Target", ["Grey Structure", "Full Finishing"])
    with col_c2:
        rate = st.number_input("Market Rate (PKR/sqft)", value=3450)
        area = {"5 Marla": 2100, "10 Marla": 3500, "1 Kanal": 6500}[size]
    
    total = area * rate
    st.success(f"### Estimated Total: PKR {total:,.0f}")
    
# --- SAVED PLOTS ---
elif choice == "Saved Plots":
    st.title("💾 User Favorites")
    st.warning("User Authentication Required. Login to see your saved plots.")
    st.button("Login / Sign Up")

# --- ADMIN PANEL ---
elif choice == "Admin Panel":
    st.title("🛠️ Global Admin Panel")
    st.subheader("Data & File Management")
    uploaded = st.file_uploader("Upload Daily Plot Inventory (CSV)", type="csv")
    if uploaded:
        st.success("Database Updated Successfully!")
    st.button("Clear Cache")

# --- ADS MANAGEMENT ---
elif choice == "Ads Management":
    st.title("📢 SaaS Ads Manager")
    st.write("Promote your listings or partners.")
    ad_img = st.file_uploader("Upload Ad Banner (1200x200)", type=["jpg", "png"])
    ad_link = st.text_input("Enter Destination URL")
    if st.button("Deploy Ad"):
        st.info("Ad queued for review by Bilal Mughal.")

# --- FOOTER ---
st.markdown("""
    <div class='footer'>
    <hr>
    © 2026 Babar Real Estate | Developed by Bilal Mughal | All Rights Reserved
    </div>
    """, unsafe_allow_html=True)
