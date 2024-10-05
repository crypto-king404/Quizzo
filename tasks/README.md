# `tasks`

## Overview

The `tasks` directory contains a collection of modules designed to facilitate document ingestion, text embedding, quiz generation, and management for an interactive quiz application called **Quizzo**. This directory serves as the core functionality for the application, integrating various components to allow users to upload documents, generate quizzes, and manage quiz interactions.

### Directory Structure

```
tasks/
│
├── Document_Ingestion/
│   ├── __init__.py
│   └── Document_Ingestion.py
│
├── Embeddings/
│   ├── __init__.py
│   └── Embedding.py
│
├── Data_Pipeline/
│   ├── __init__.py
│   └── data_pipeline.py
│
├── Quiz_Generator/
│   ├── __init__.py
│   └── quiz_generator.py
│
├── Quiz_Manager/
│   ├── __init__.py
│   └── quiz_manager.py
│
└── app.py
```

### Contents

1. **Document_Ingestion**: 
   - Contains functionality for processing and ingesting PDF documents using `PyPDFLoader`. The `DocumentProcessor` class provides methods to upload and extract pages from the PDF files.

2. **Embeddings**: 
   - Manages the connection to Google Cloud's Vertex AI for generating text embeddings. The `EmbeddingClient` class encapsulates methods for embedding queries and documents, allowing for semantic understanding of text.

3. **Data_Pipeline**: 
   - Implements the `ChromaCollectionCreator` class, which creates a Chroma collection of document embeddings from the processed documents. This class enables efficient storage and retrieval of document vectors for querying.

4. **Quiz_Generator**: 
   - Contains the `QuizGenerator` class that generates quiz questions based on a specified topic and document content. It uses a large language model (LLM) to create questions in a structured JSON format, ensuring they are unique and relevant.

5. **Quiz_Manager**: 
   - Handles the navigation and management of quiz questions. The `QuizManager` class allows users to retrieve questions, check answers, and manage quiz state effectively.

6. **app.py**: 
   - The main entry point for the Quizzo application. This script integrates all the components from the `tasks` directory, facilitating user interaction through a Streamlit interface. It orchestrates the document ingestion, quiz generation, and quiz management processes.

### Installation

Before running the application, ensure you have the following dependencies installed:

```bash
pip install streamlit langchain google-auth google-auth-oauthlib google-auth-httplib2 langchain_google_vertexai reportlab
```

### Usage

To run the application, navigate to the `tasks` directory and execute:

```bash
streamlit run app.py
```
