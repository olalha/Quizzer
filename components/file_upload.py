import streamlit as st
from utils.file_management import save_uploaded_file, load_files
from utils.alert import show_alert

def render_file_upload(allowed_types=['pdf', 'pptx', 'docx'], form_key="upload_form"):
    with st.form(form_key, clear_on_submit=True):
        uploaded_file = st.file_uploader("Upload a Lecture File", type=allowed_types)
        submit_button = st.form_submit_button("Upload")

    if submit_button:
        if uploaded_file is not None:
            save_uploaded_file(uploaded_file)
            st.session_state.files = load_files()
            st.session_state.alert = {
                'type': 'success',
                'message': f"File '{uploaded_file.name}' uploaded and saved to database."
            }
            st.rerun()
        else:
            st.session_state.alert = {
                'type': 'error',
                'message': "Please select a file before uploading."
            }
            show_alert()
