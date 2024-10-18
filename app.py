import os
import streamlit as st
from utils.alert import show_alert
from utils.file_management import load_files, save_uploaded_file, handle_file_deletion, handle_delete_all

# Initialize session state
if 'files' not in st.session_state:
    st.session_state.files = []
    
if 'alert' not in st.session_state:
    st.session_state.alert = None

if st.session_state.alert:
    show_alert(st)

def handle_file_upload():
    with st.form("upload_form", clear_on_submit=True):
        uploaded_file = st.file_uploader("Upload a Lecture File", type=['pdf', 'pptx', 'docx'])
        submit_button = st.form_submit_button("Upload")

    if submit_button:
        if uploaded_file is not None:
            save_uploaded_file(uploaded_file)
            st.session_state.alert = {
                'type': 'success',
                'message': f"File '{uploaded_file.name}' uploaded and saved to database."
            }
            st.session_state.files = load_files()
            st.rerun()
        else:
            st.session_state.alert = {
                'type': 'error',
                'message': "Please select a file before uploading."
            }
            show_alert(st)

def display_file_table():
    st.subheader("Uploaded Files")
    if st.session_state.files:
        for file in st.session_state.files:
            col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
            with col1:
                st.write(file.id)
            with col2:
                st.write(file.filename)
            with col3:
                st.write(file.upload_time)
            with col4:
                if st.button("Delete", key=f"delete_{file.id}"):
                    st.session_state.alert = {
                        'type': 'warning',
                        'message': f"File '{file.filename}' removed from database."
                    }
                    st.session_state.files = handle_file_deletion(file.id)
                    st.rerun()
    else:
        st.session_state.alert = {
            'type': 'info',
            'message': "No files uploaded yet."
        }
        show_alert(st)
        
def main():
    st.title("File Upload and Management")

    # Load files at the start of the app
    if len(st.session_state.files) == 0:
        st.session_state.files = load_files()

    handle_file_upload()

    if st.button("Delete All Files"):
        st.session_state.files = handle_delete_all()
        st.session_state.alert = {
            'type': 'warning',
            'message': "All files have been removed from the database."
        }
        st.rerun()

    display_file_table()

if __name__ == "__main__":
    main()
