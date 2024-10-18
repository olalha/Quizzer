import os
import streamlit as st

from utils.database.db_setup import session
from utils.database.models import UploadedFile, LearningMaterial
from utils.database.db_utils import delete_uploaded_file, cleanup_all_uploaded_files
from config.settings import UPLOAD_FOLDER

# Initialize session state
if 'files' not in st.session_state:
    st.session_state.files = []

def load_files():
    return session.query(UploadedFile).all()

def save_uploaded_file(uploaded_file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    new_file = UploadedFile(filename=uploaded_file.name, filepath=file_path, title="Lecture material")
    session.add(new_file)
    session.commit()

def handle_file_upload():
    with st.form("upload_form"):
        uploaded_file = st.file_uploader("Upload a Lecture File", type=['pdf', 'pptx', 'docx'])
        submit_button = st.form_submit_button("Upload")

    if submit_button and uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.success(f"File '{uploaded_file.name}' uploaded and saved to database.")
        st.session_state.files = load_files()
        st.rerun()

def handle_file_deletion(file_id):
    delete_uploaded_file(session, file_id)
    st.session_state.files = load_files()
    st.rerun()

def handle_delete_all():
    cleanup_all_uploaded_files(session)
    st.session_state.files = load_files()
    st.rerun()

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
                    handle_file_deletion(file.id)
    else:
        st.info("No files uploaded yet.")

def main():
    st.title("File Upload and Management")

    # Load files at the start of the app
    if len(st.session_state.files) == 0:
        st.session_state.files = load_files()

    handle_file_upload()

    if st.button("Delete All Files"):
        handle_delete_all()

    display_file_table()

if __name__ == "__main__":
    main()
