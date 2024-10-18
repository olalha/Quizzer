import streamlit as st
from utils.alert import show_alert
from utils.file_management import load_files
from components.file_upload import render_file_upload
from components.file_table import render_file_table

if st.session_state.alert:
    show_alert()

st.title("Files")

# Load files at the start of the page
if len(st.session_state.files) == 0:
    st.session_state.files = load_files()

render_file_upload()
render_file_table()
