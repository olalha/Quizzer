
!!!
THIS NEEDS TO BE CONVERTED TO MARKDOWN AND TURNED INTO A README.MD FILE
!!!

# **Quiz Generator from Lecture Materials - Outline**

## **Purpose of the Application**

The goal of this project is to create a simple application that allows users to upload lecture materials (in PDF, PPTX, or DOCX format) and automatically generate quizzes from the content using large language models (LLMs). This tool is designed for personal use by students to test their knowledge of lecture materials.

### **Key Features**:
1. **File Upload**: Users can upload lecture files (PDF, PPTX, or DOCX).
2. **Text Extraction**: The application extracts text from the uploaded files.
3. **Quiz Generation**: The extracted text is sent to an multiple LLMs (via OpenRouter's API), which generates quiz questions.
4. **Quiz Display**: Users can answer the quiz and get feedback.


### **Tools and Libraries**

1. **Streamlit**: Simplifies web app creation, allowing interaction through a Python-only interface.
2. **OpenRouter API**: Provides LLM-based quiz generation from the lecture content.
3. **pdfminer.six, python-pptx, python-docx**: Used to extract text from PDF, PPTX, and DOCX files.
4. **requests**: For sending HTTP requests to the OpenRouter API.
5. **Python Virtual Environment (venv)**: Manages dependencies and isolates project libraries.
