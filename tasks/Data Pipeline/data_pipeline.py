import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.Document_Ingestion.Document_Ingestion import DocumentProcessor
from tasks.Embeddings.Embedding import EmbeddingClient


# Import Task libraries
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

class ChromaCollectionCreator:
    def __init__(self, processor, embed_model):
        """
        Initializes the ChromaCollectionCreator with a DocumentProcessor instance and embeddings configuration.
        :param processor: An instance of DocumentProcessor that has processed documents.
        :param embeddings_config: An embedding client for embedding documents.
        """
        self.processor = processor      # This will hold the DocumentProcessor from Task 3
        self.embed_model = embed_model  # This will hold the EmbeddingClient from Task 4
        self.db = None                  # This will hold the Chroma collection
    
    def create_chroma_collection(self):
        """
        Create a Chroma collection from the documents processed by the DocumentProcessor instance.
        """
        
        # Check for processed documents
        if len(self.processor.pages) == 0:
            st.error("No documents found!", icon="🚨")
            return

        # Split documents into text chunks
        
        texts = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=100).split_documents(self.processor.pages)
        
        if texts is not None:
            st.success(f"Successfully split pages to {len(texts)} documents!", icon="✅")

        #  Create the Chroma Collection
        self.db = Chroma.from_documents(texts, self.embed_model)
        
        if self.db:
            st.success("Successfully created Chroma Collection!", icon="✅")
        else:
            st.error("Failed to create Chroma Collection!", icon="🚨")
    
    def query_chroma_collection(self, query) -> Document:
        """
        Queries the created Chroma collection for documents similar to the query.
        :param query: The query string to search for in the Chroma collection.
        
        Returns the first matching document from the collection with similarity score.
        """
        if self.db:
            docs = self.db.similarity_search_with_relevance_scores(query)
            if docs:
                return docs[0]
            else:
                st.error("No matching documents found!", icon="🚨")
        else:
            st.error("Chroma Collection has not been created!", icon="🚨")

    def as_retriever(self):
        """
        Returns the Chroma collection as a retriever for use in quiz generator
        """
        return self.query_chroma_collection

#Test if the app is working
# if __name__ == "__main__":
#     processor = DocumentProcessor() # Initialize from Task 3
#     processor.ingest_documents()
    
#     embed_config = {
#         "model_name": "textembedding-gecko@003",
#         "project": "PROJECT-123",
#         "key_file_path": "C:/path/to/the/json/authentication.json",
#         "location": "us-central1"
#     }
    
#     embed_client = EmbeddingClient(**embed_config) # Initialize from Task 4
    
#     chroma_creator = ChromaCollectionCreator(processor, embed_client)
    
#     with st.form("Load Data to Chroma"):
#         st.write("Select PDFs for Ingestion, then click Submit")
        
#         submitted = st.form_submit_button("Submit")
#         if submitted:
#             chroma_creator.create_chroma_collection()
