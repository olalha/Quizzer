import streamlit as st

from components.alert import show_alert
from utils.file_management import load_files, get_file_name, get_file_id
from text_processing.material_generator import generate_summary_json

# Display alert if it exists in session state
if st.session_state.alert:
    show_alert()
    
"""
TESTING CODE (WIP)

Allows user to select a file and send a request to the LLM for a summary.
"""

st.title("Prompt Builder")

# Load files at the start of the page
if len(st.session_state.files) == 0:
    st.session_state.files = load_files()

file_options = [get_file_name(file.id) for file in st.session_state.files]
selected_file = st.selectbox("Select a file", options=file_options)

# Add a submit button
if st.button("Submit"):
    if selected_file:
        selected_file_id = get_file_id(selected_file)
        summary_json = generate_summary_json(selected_file_id)
        st.write(summary_json)
    else:
        st.session_state.alert = {
            'type': 'warning',
            'message': "Please select a file before submitting."
        }
        show_alert()