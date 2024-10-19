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

llm_testing_page = st.Page(
    page="views/llm_testing_view.py",
    title="LLM Testing",
)

nav = st.navigation(pages=[files_page, llm_testing_page])
nav.run()
