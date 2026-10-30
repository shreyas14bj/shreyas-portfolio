import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Configure Streamlit page metadata and layout
st.set_page_config(
    page_title="Shreyas B J • AI/ML Engineer & Observational Draughtsman",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS to hide default Streamlit chrome (header, hamburger menu, footer, status widget)
# and stretch the embedded portfolio iframe across 100% of the viewport seamlessly
st.markdown("""
<style>
    /* Hide Streamlit Header, Menu, Footer, and Status Indicators */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    footer {
        display: none !important;
    }
    #MainMenu {
        display: none !important;
    }
    div[data-testid="stToolbar"] {
        display: none !important;
    }
    div[data-testid="stDecoration"] {
        display: none !important;
    }
    div[data-testid="stStatusWidget"] {
        display: none !important;
    }
    
    /* Remove default container padding so the layout extends edge-to-edge */
    .main .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow: hidden !important;
    }
    
    /* Fixed full-screen iframe styling */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 99999 !important;
    }
</style>
""", unsafe_allow_html=True)

# Locate index.html and assets
current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "index.html")
photo_path = os.path.join(current_dir, "assets", "shreyas-photo.png")

if not os.path.exists(html_path):
    st.error("Portfolio build file (index.html) was not found in the root directory.")
    st.stop()

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Inline profile photo as Base64 Data URL to guarantee zero 404s inside the iframe
if os.path.exists(photo_path):
    with open(photo_path, "rb") as img_file:
        photo_b64 = base64.b64encode(img_file.read()).decode("utf-8")
        photo_data_url = f"data:image/png;base64,{photo_b64}"
        html_content = html_content.replace("./assets/shreyas-photo.png", photo_data_url)

# Render the self-contained cinematic portfolio with scrolling enabled
components.html(html_content, height=1200, scrolling=True)
