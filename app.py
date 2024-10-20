import streamlit as st

if 'files' not in st.session_state:
    st.session_state.files = []
if 'alert' not in st.session_state:
    st.session_state.alert = None

files_page = st.Page(
    page="views/files_view.py",
    title="Files",
    default=True
)

generate_page = st.Page(
    page="views/generate_view.py",
    title="Generate",
)

nav = st.navigation(pages=[files_page, generate_page])
nav.run()
