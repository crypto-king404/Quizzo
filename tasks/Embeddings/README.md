# `Embedding.py`

## Overview

`Embedding.py` is a Python module designed to interface with Google Cloud's Vertex AI for generating text embeddings. It provides an easy-to-use client class, `EmbeddingClient`, that can connect to Vertex AI using service account credentials and generate embeddings for text queries and documents. The module is particularly useful for applications that require text similarity calculations, document clustering, or any other natural language processing tasks that benefit from vector representations.

### Table of Contents
1. [Installation](#installation)
2. [Classes and Methods](#classes-and-methods)
    - [EmbeddingClient](#embeddingclient)
        - [`__init__`](#__init__)
        - [`embed_query`](#embed_query)
        - [`embed_documents`](#embed_documents)
3. [Usage](#usage)
4. [Example](#example)
5. [Dependencies](#dependencies)

## Installation

Make sure to have the following libraries installed before using the module:

```bash
pip install streamlit google-auth google-auth-oauthlib google-auth-httplib2 langchain_google_vertexai
```

## Classes and Methods

### `EmbeddingClient`

This class provides an interface for interacting with the Vertex AI embedding services using `VertexAIEmbeddings`. It allows you to generate embeddings for both individual queries and multiple documents.

#### `__init__(self, model_name, project, location, key_file_path)`

**Parameters:**
- `model_name`: The name of the Vertex AI model to use for generating embeddings.
- `project`: The Google Cloud project ID where the Vertex AI resources are deployed.
- `location`: The location/region of the Vertex AI resources.
- `key_file_path`: The path to the service account key file used for authentication.

**Description:**
Initializes the `EmbeddingClient` by connecting to Google Cloud Vertex AI using the provided credentials and configuration.

---

#### `embed_query(self, query)`

**Parameters:**
- `query`: A text string for which embeddings need to be generated.

**Description:**
Generates embeddings for the given query text using the connected Vertex AI embedding model.

**Returns:**
- A list representing the vector embeddings of the input query.

---

#### `embed_documents(self, documents)`

**Parameters:**
- `documents`: A list of text documents for which embeddings need to be generated.

**Description:**
Generates embeddings for a batch of documents. This is useful when working with large sets of documents that need to be represented as vectors for further analysis.

**Returns:**
- A list of vectors representing the embeddings of the input documents.

---

## Usage

```python
from Embedding import EmbeddingClient

# Define parameters for the embedding client
model_name = "textembedding-gecko"
project = "your-google-cloud-project"
location = "us-central1"
key_file_path = "/path/to/your/service-account-key.json"

# Initialize the EmbeddingClient
embedding_client = EmbeddingClient(model_name=model_name, project=project, location=location, key_file_path=key_file_path)

# Generate embeddings for a single query
query_embedding = embedding_client.embed_query("What is the capital of France?")
print(f"Query Embedding: {query_embedding}")

# Generate embeddings for multiple documents
documents = ["Document 1 content", "Document 2 content"]
document_embeddings = embedding_client.embed_documents(documents)
print(f"Document Embeddings: {document_embeddings}")
```

## Example

To run this module, ensure that you have a Google Cloud project set up with Vertex AI enabled. Create a service account with appropriate permissions and download its key file. Update the `key_file_path` parameter in the script to point to the location of this key file. Once set up, use the methods `embed_query` and `embed_documents` to generate embeddings for your text data.

## Dependencies

- Python 3.x
- `streamlit`
- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `langchain_google_vertexai`
