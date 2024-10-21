
# **Quiz and Notes Generator from Lecture Materials**

## **Purpose of the Application**

The goal of this project is to create a simple application that allows users to upload lecture materials (in PDF, PPTX, or DOCX format) and automatically generate quizzes from the content using large language models (LLMs). This tool is designed for personal use by students to test their knowledge of lecture materials.

### **Key Features**:
1. **File Upload**: Users can upload lecture files (PDF, PPTX, or DOCX).
2. **Text Extraction**: The application extracts text from the uploaded files.
3. **Content Generation**: The extracted text is processed by an multiple LLMs.
4. **Simple Interface**: Users can interact with the generated content in a simple web interface.

## **Setup**
1. Clone the repository.
    ```bash
    git clone https://github.com/olalha/Quizzer.git
    ```
2. Set up a python venv and install the dependencies.
    ```bash
    python -m venv _quizzer_venv
    source _quizzer_venv/scripts/activate
    pip install -r requirements.txt
    ```
3. Configure the .env file.
    ```
    OPENROUTER_API_KEY = 'your_openrouter_api_key'
    DATABASE_URL = 'your_database_url'
    ```
4. Run the application.
    ```bash
    streamlit run app.py
    ```
