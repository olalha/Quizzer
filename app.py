import streamlit as st
from utils.page_init import init_session_state

init_session_state()

files_page = st.Page(
    page="views/files_view.py",
    title="Files",
    default=True
)

nav = st.navigation(pages=[files_page])
nav.run()
