"""
File Upload Component

This component can be added as part of a Streamlit page. It provides a file uploader
for files and handles the upload process, including saving to the database
and updating the session state.
"""

import streamlit as st
from text_processing.text_extractor import SUPPORTED_FILE_TYPES

from .alert import show_alert
from utils.file_management import handle_file_upload

def render_file_upload(allowed_types=SUPPORTED_FILE_TYPES, form_key="upload_form"):
    # Create a form for file upload
    with st.form(form_key, clear_on_submit=True):
        uploaded_file = st.file_uploader("Upload a Lecture File", type=allowed_types)
        submit_button = st.form_submit_button("Upload")

    if submit_button:
        if uploaded_file is not None:
            # Handle the file upload process
            st.session_state.files = handle_file_upload(uploaded_file)
            # Set a success alert
            st.session_state.alert = {
                'type': 'success',
                'message': f"File '{uploaded_file.name}' uploaded and saved to database."
            }
            # Rerun the app to reflect changes
            st.rerun()
        else:
            # Show an error alert if no file was selected
            st.session_state.alert = {
                'type': 'error',
                'message': "Please select a file before uploading."
            }
            show_alert()
