"""
Streamlit main application.
"""

import streamlit as st
import yaml

settings = {}

# Initialize session state variables
if 'files' not in st.session_state:
    st.session_state.files = []
if 'alert' not in st.session_state:
    st.session_state.alert = None

# Load settings
try:
    with open('_config/settings.yaml', 'r') as file:
        settings = yaml.safe_load(file)
except Exception as e:
    st.error(f"Error: Could not load settings file: {e}")
    settings = {}

# Define pages

files_page = st.Page(
    page="views/files_view.py",
    title="Files",
    default=True
)

generate_page = st.Page(
    page="views/generate_view.py",
    title="Generate",
)

# Setup navigation
nav = st.navigation(pages=[files_page, generate_page])
nav.run()
