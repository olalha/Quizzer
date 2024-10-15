import streamlit as st
from utils.database.db_setup import session
from utils.database.models import UploadedFile, Quiz
import os

UPLOAD_FOLDER = 'data/uploads'

# Streamlit file uploader
uploaded_file = st.file_uploader("Upload a Lecture File", type=['pdf', 'pptx', 'docx'])

if uploaded_file:
    
    # Save the uploaded file to the local 'uploads' folder
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    # Add file details to the database
    new_file = UploadedFile(filename=uploaded_file.name, filepath=file_path, title="Lecture material")
    session.add(new_file)
    session.commit()
    
    st.write(f"File '{uploaded_file.name}' uploaded and saved to database.")

# Display quizzes (as an example)
quizzes = session.query(Quiz).all()
if quizzes:
    for quiz in quizzes:
        st.write(f"Quiz ID: {quiz.id}")
        st.write(quiz.quiz_content)
