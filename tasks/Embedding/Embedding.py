# embedding_client.py

import streamlit as st
from google.auth import credentials, default
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from langchain_google_vertexai import VertexAIEmbeddings

class EmbeddingClient:
    """
    Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings.

    """
    
    def __init__(self, model_name, project, location, key_file_path):
        # Initialize the VertexAIEmbeddings client with the given parameters
        self.client = self._initialize_client(model_name, project, location, key_file_path)


    def _initialize_client(self, model_name, project, location, key_file_path):
        # Load the service account key file
        credentials = service_account.Credentials.from_service_account_file(key_file_path)

        # Initialize the VertexAIEmbeddings client with the provided parameters and credentials
        client = VertexAIEmbeddings(model_name=model_name, project=project, location=location, credentials=credentials)
        return client
        

    def embed_query(self, query):
        """
        Uses the embedding client to retrieve embeddings for the given query.

        :param query: The text query to embed.
        :return: The embeddings for the query or None if the operation fails.
        """
        vectors = self.client.embed_query(query)
        return vectors
    
    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.

        :param documents: A list of text documents to embed.
        :return: A list of embeddings for the given documents.
        """
        try:
            return self.client.embed_documents(documents)
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None

if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "PROJECT-123"
    location = "us-central1"
    key_file_path = "C:/path/to/the/json/authentication.json"

    embedding_client = EmbeddingClient(model_name, project, location, key_file_path)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        st.write(vectors)
        print("Successfully used the embedding client!")
