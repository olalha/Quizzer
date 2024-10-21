"""
File Table Component

This component can be added as part of a Streamlit page. It displays a table of files
stored in the database and allows for individual or bulk deletion of files.
"""

import streamlit as st

from .alert import show_alert
from utils.file_management import handle_file_deletion, handle_delete_all

def render_file_table():
    st.subheader("Uploaded Files")
    
    # Button to delete all files
    if st.button("Delete All Files"):
        st.session_state.files = handle_delete_all()
        st.session_state.alert = {
            'type': 'warning',
            'message': "All files have been removed from the database."
        }
        st.rerun()

    if st.session_state.files:
        # Display table of files
        for file in st.session_state.files:
            col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
            with col1:
                st.write(file.id)
            with col2:
                st.write(file.filename)
            with col3:
                st.write(file.upload_time)
            with col4:
                # Delete button for each file
                if st.button("Delete", key=f"delete_{file.id}"):
                    st.session_state.files = handle_file_deletion(file.id)
                    st.session_state.alert = {
                        'type': 'warning',
                        'message': f"File '{file.filename}' removed from database."
                    }
                    st.rerun()
    else:
        # Show message if no files are present
        st.session_state.alert = {
            'type': 'info',
            'message': "No files uploaded yet."
        }
        show_alert()
