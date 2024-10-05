# `quiz_generator.py`

## Overview

`quiz_generator.py` is a Python module that facilitates automated quiz generation using advanced AI techniques. It leverages LangChain, Google Cloud Vertex AI, and document embeddings to create quiz questions based on a specific topic. This module can generate multiple-choice questions with explanations and validate the uniqueness of each question to ensure high-quality quiz content.

### Table of Contents
1. [Installation](#installation)
2. [Classes and Methods](#classes-and-methods)
    - [QuizGenerator](#quizgenerator)
        - [`__init__`](#__init__)
        - [`init_llm`](#init_llm)
        - [`generate_question_with_vectorstore`](#generate_question_with_vectorstore)
        - [`generate_quiz`](#generate_quiz)
        - [`validate_question`](#validate_question)
3. [Usage](#usage)
4. [Example](#example)
5. [Dependencies](#dependencies)

## Installation

Ensure you have the following libraries installed before using the module:

```bash
pip install streamlit langchain langchain_google_vertexai nltk
```

Additionally, ensure that `DocumentProcessor`, `EmbeddingClient`, and `ChromaCollectionCreator` classes from the `tasks` module are correctly set up in your project directory.

## Classes and Methods

### `QuizGenerator`

This class handles the generation of quiz questions using a specified topic, a language model (LLM), and an optional vectorstore (e.g., ChromaDB). It ensures each question is relevant and unique by validating the generated questions before adding them to the quiz.

#### `__init__(self, topic=None, num_questions=1, vectorstore=None)`

**Parameters:**
- `topic`: A string representing the topic of the quiz (e.g., "Machine Learning"). Defaults to "General Knowledge" if not provided.
- `num_questions`: The number of questions to generate, capped at a maximum of 10. Raises a `ValueError` if the number exceeds 10.
- `vectorstore`: An optional instance of a vectorstore (e.g., ChromaDB) for retrieving relevant information related to the quiz topic.

**Description:**
Initializes the `QuizGenerator` with a specified topic, number of questions, and a vectorstore instance for querying related information. If a vectorstore is not provided, it will rely solely on the language model for content generation.

---

#### `init_llm(self)`

**Description:**
Initializes and configures the Large Language Model (LLM) using Google Cloud Vertex AI for generating quiz questions. It sets up parameters like `model_name`, `temperature`, and `max_output_tokens` to control the LLM's output behavior.

---

#### `generate_question_with_vectorstore(self)`

**Description:**
Generates a quiz question using the specified topic and vectorstore. It utilizes a `PromptTemplate` and retrieves relevant information from the vectorstore before feeding it into the LLM to generate the question.

**Returns:**
- A JSON-formatted string representing the generated quiz question.

---

#### `generate_quiz(self) -> list`

**Description:**
Orchestrates the entire quiz generation process by calling `generate_question_with_vectorstore()` to create each question. Ensures each question is unique by using the `validate_question` method before adding it to the final quiz.

**Returns:**
- A list of unique, validated quiz questions.

---

#### `validate_question(self, question: dict) -> bool`

**Description:**
Validates the uniqueness of the provided question by comparing it to existing questions in the `question_bank`. It uses Jaccard distance on n-grams of the question text to determine if the question is sufficiently distinct from others.

**Returns:**
- `True` if the question is unique; otherwise, `False`.

---

## Usage

```python
from tasks.Data_Pipeline.data_pipeline import ChromaCollectionCreator
from tasks.Document_Ingestion.Document_Ingestion import DocumentProcessor
from tasks.Embeddings.Embedding import EmbeddingClient
from quiz_generator import QuizGenerator

# Initialize necessary components
document_processor = DocumentProcessor()
embedding_client = EmbeddingClient(
    model_name="textembedding-gecko", 
    project="your-google-cloud-project", 
    location="us-central1", 
    key_file_path="/path/to/service-account-key.json"
)
collection_creator = ChromaCollectionCreator(document_processor, embedding_client)

# Create a Chroma collection with processed documents
collection_creator.create_chroma_collection()

# Initialize the QuizGenerator with topic, number of questions, and the created vectorstore
quiz_generator = QuizGenerator(topic="Machine Learning", num_questions=5, vectorstore=collection_creator.db)

# Generate the quiz
quiz = quiz_generator.generate_quiz()
print(f"Generated Quiz: {quiz}")
```

## Example

To run this module, ensure that you have a Google Cloud Vertex AI model configured and a Chroma collection created with your documents. Use the `generate_quiz()` method to generate a quiz on the specified topic with the desired number of questions. This module integrates seamlessly with Streamlit for interactive application development.

## Dependencies

- Python 3.x
- `streamlit`
- `langchain`
- `langchain_google_vertexai`
- `nltk`
