"""
Streamlit main application.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Check if environment variables are set
required_env_vars = ['OPENROUTER_API_KEY', 'DATABASE_URL']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    raise ValueError(f"Error: Missing required environment variables: {', '.join(missing_vars)}")

import streamlit as st

# Initialize session state variables
if 'files' not in st.session_state:
    st.session_state.files = []
if 'alert' not in st.session_state:
    st.session_state.alert = None

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
