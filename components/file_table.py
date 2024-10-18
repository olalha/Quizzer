import streamlit as st
from utils.file_management import handle_file_deletion, handle_delete_all
from utils.alert import show_alert

def render_file_table():
    st.subheader("Uploaded Files")
    
    if st.button("Delete All Files"):
        st.session_state.files = handle_delete_all()
        st.session_state.alert = {
            'type': 'warning',
            'message': "All files have been removed from the database."
        }
        st.rerun()

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
                    st.session_state.files = handle_file_deletion(file.id)
                    st.session_state.alert = {
                        'type': 'warning',
                        'message': f"File '{file.filename}' removed from database."
                    }
                    st.rerun()
    else:
        st.session_state.alert = {
            'type': 'info',
            'message': "No files uploaded yet."
        }
        show_alert()
