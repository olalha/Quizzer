"""
Streamlit page for managing uploaded files.
"""

import streamlit as st

from utils.file_management import load_files
from components.alert import show_alert
from components.file_upload import render_file_upload
from components.file_table import render_file_table

# Display alert if it exists in session state
if st.session_state.alert:
    show_alert()

st.title("Files")

# Load files at the start of the page
if len(st.session_state.files) == 0:
    st.session_state.files = load_files()

# Load components
render_file_upload()
render_file_table()
