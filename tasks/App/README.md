# `app.py`

## Overview

`app.py` is the main application script for `Quizzo`, a Streamlit-based interactive quiz builder and manager. It integrates document ingestion, embeddings, quiz generation, and quiz management functionalities to create, display, and manage quizzes based on user-uploaded PDF documents. The app leverages Google Cloud Vertex AI for generating text embeddings, LangChain for document processing, and ChromaDB for efficient storage and retrieval of document embeddings.

### Table of Contents
1. [Installation](#installation)
2. [Features](#features)
3. [Application Flow](#application-flow)
4. [Usage](#usage)
5. [Example](#example)
6. [Dependencies](#dependencies)

## Installation

Make sure you have the following dependencies installed before running the application:

```bash
pip install streamlit langchain google-auth google-auth-oauthlib google-auth-httplib2 langchain_google_vertexai reportlab
```

You will also need a Google Cloud service account key file for authentication, which should be provided in the configuration.

## Features

- **Document Ingestion**: Upload multiple PDF files and extract their content using the `DocumentProcessor` class.
- **Embedding Creation**: Generate embeddings for the uploaded documents using Google Cloud's Vertex AI with the `EmbeddingClient` class.
- **Quiz Generation**: Automatically create quiz questions based on a selected topic using the `QuizGenerator` class and ChromaDB.
- **Quiz Management**: Navigate through questions, validate answers, and track scores using the `QuizManager` class.
- **Report Generation**: Generate and download a PDF report summarizing quiz results, including total questions, correct answers, incorrect answers, and overall score.

## Application Flow

1. **Data Ingestion and Embedding**:
   - The application begins with a form that allows users to upload PDF files for ingestion.
   - Once the documents are uploaded, they are processed using `DocumentProcessor` and the resulting pages are stored.
   - The application then uses `EmbeddingClient` to create embeddings for the documents, which are stored in a Chroma collection using `ChromaCollectionCreator`.

2. **Quiz Generation**:
   - The user specifies the topic of the quiz and the number of questions to generate (up to 10).
   - The `QuizGenerator` class creates quiz questions based on the specified topic and the content from the ingested documents.
   - Generated questions are stored in the session state (`st.session_state["question_bank"]`).

3. **Quiz Display and Navigation**:
   - The quiz questions are displayed one by one with multiple-choice options.
   - Users can navigate through the questions, and the `QuizManager` class handles question indexing and navigation logic.
   - User responses are validated, and feedback is provided for each answer.

4. **Result Summary and Report Generation**:
   - Once all questions are answered, the user can generate a PDF report with the results.
   - The report includes total questions, correct and incorrect answers, and the overall score.
   - The PDF report is available for download directly from the Streamlit interface.

## Usage

```bash
# Run the application using Streamlit
streamlit run app.py
```

### Important Notes:
- **Google Cloud Configuration**: Ensure that `embed_config` is correctly set up with your Google Cloud `project`, `location`, `model_name`, and the path to your service account key file.
- **Session State Management**: `st.session_state` is used to manage quiz state, question indices, and score tracking.

## Example

```python
# Sample Configuration for Google Cloud Vertex AI Embeddings
embed_config = {
    "model_name": "textembedding-gecko@003",
    "project": "PROJECT-123",
    "key_file_path": "C:/path/to/the/json/authentication.json",
    "location": "us-central1"
}

# Initialize and run the application
python app.py
```

## Dependencies

- Python 3.x
- `streamlit`
- `langchain`
- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `langchain_google_vertexai`
- `reportlab`

