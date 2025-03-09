import streamlit as st
import streamlit.components.v1 as components

# Set page configuration for full-screen layout
st.set_page_config(
    page_title="About Project", layout="wide", initial_sidebar_state="collapsed",
    page_icon="📃")

# Read the HTML file
with open("about.html", "r") as file:
    html_content = file.read()

# Hide the Streamlit menu and footer to make the page look more like fullscreen
hide_streamlit_style = """
    <style>
        font-size: 20px
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0; margin: 0;}
    </style>
"""



st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Display the HTML content as fullscreen
components.html(html_content, height=1000, scrolling=True)