import streamlit as st

st.title("Lecture Material Quiz Generator")

uploaded_file = st.file_uploader("Upload a Lecture File", type=['pdf', 'pptx', 'docx'])

if uploaded_file:
    st.write(f"File uploaded: {uploaded_file.name}")
