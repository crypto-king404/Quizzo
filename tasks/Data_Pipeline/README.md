# `data_pipeline.py`

## Overview

`data_pipeline.py` is a Python module designed to create and manage a Chroma collection for efficient document search and retrieval. The module leverages LangChain's document processing and embedding functionalities to store and query document embeddings. This script is primarily used for building a collection of documents that can be easily queried for similarity searches, making it ideal for applications like semantic search and recommendation systems.

### Table of Contents
1. [Installation](#installation)
2. [Classes and Methods](#classes-and-methods)
    - [ChromaCollectionCreator](#chromacollectioncreator)
        - [`__init__`](#__init__)
        - [`create_chroma_collection`](#create_chroma_collection)
        - [`query_chroma_collection`](#query_chroma_collection)
        - [`as_retriever`](#as_retriever)
3. [Usage](#usage)
4. [Example](#example)
5. [Dependencies](#dependencies)

## Installation

Ensure you have the following libraries installed before using the module:

```bash
pip install streamlit langchain chromadb langchain_community
```

Additionally, ensure that you have the supporting scripts `DocumentProcessor` and `EmbeddingClient` from the `tasks` module correctly set up in your project directory.

## Classes and Methods

### `ChromaCollectionCreator`

This class is responsible for creating a Chroma collection of document embeddings and querying them for similarity-based searches. 

#### `__init__(self, processor, embed_model)`

**Parameters:**
- `processor`: An instance of `DocumentProcessor` that handles the document ingestion process.
- `embed_model`: An instance of `EmbeddingClient` used for generating document embeddings.

**Description:**
Initializes the `ChromaCollectionCreator` class with a `DocumentProcessor` and `EmbeddingClient`. These two instances handle the ingestion and embedding of documents, respectively.

---

#### `create_chroma_collection(self)`

**Description:**
Creates a Chroma collection from documents processed by the `DocumentProcessor` instance. It splits the documents into manageable text chunks and generates embeddings using the provided embedding model. The resulting Chroma collection can be used for various downstream tasks like querying for similar documents.

**Output:**
- Displays success or error messages using Streamlit for document splitting and collection creation.

---

#### `query_chroma_collection(self, query) -> Document`

**Parameters:**
- `query`: A query string used to search the Chroma collection.

**Description:**
Queries the created Chroma collection for documents similar to the provided query. Returns the first matching document along with the similarity score.

**Returns:**
- A document with the highest similarity to the query.

---

#### `as_retriever(self)`

**Description:**
Returns the Chroma collection as a retriever object, making it easy to integrate with other applications like quiz generators or search systems.

---

## Usage

```python
from data_pipeline import ChromaCollectionCreator
from tasks.Document_Ingestion.Document_Ingestion import DocumentProcessor
from tasks.Embeddings.Embedding import EmbeddingClient

# Initialize document processor and embedding client
document_processor = DocumentProcessor()
embedding_client = EmbeddingClient()

# Initialize the ChromaCollectionCreator with processor and embedding model
collection_creator = ChromaCollectionCreator(document_processor, embedding_client)

# Create the Chroma collection
collection_creator.create_chroma_collection()

# Query the collection for a specific search term
result = collection_creator.query_chroma_collection("example query")
print(f"Found document: {result}")
```

## Example

To run this module, ensure that the `DocumentProcessor` and `EmbeddingClient` instances are correctly configured. Use the methods provided by the `ChromaCollectionCreator` class to create a document collection and perform similarity searches.

## Dependencies

- Python 3.x
- `streamlit`
- `langchain`
- `chromadb`
- `langchain_community`
- `tasks` module (Document Ingestion and Embedding)

---
