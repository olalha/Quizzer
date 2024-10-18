import streamlit as st

def init_session_state():
    if 'files' not in st.session_state:
        st.session_state.files = []
    if 'alert' not in st.session_state:
        st.session_state.alert = None
