import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.Document_Ingestion.Document_Ingestion import DocumentProcessor
from tasks.Embeddings.Embedding import EmbeddingClient
from tasks.Data_Pipeline.data_pipeline import ChromaCollectionCreator

f"""
To Build a Quiz Builder with Streamlit and LangChain
"""

#Test if the app is working
# if __name__ == "__main__":
#     st.header("Quizzo")

#     # Configuration for EmbeddingClient
#     embed_config = {
#         "model_name": "textembedding-gecko@003",
#         "project": "PROJECT-123",
#         "location": "us-central1"
#     }
    
#     screen = st.empty() # Screen 1, ingest documents
#     with screen.container():
#         st.header("Quizzify")
#         ####### YOUR CODE HERE #######
#         # 1) Initalize DocumentProcessor and Ingest Documents from Task 3
#         processor = DocumentProcessor()
#         processor.ingest_documents()

#         embed_config = {
#         "model_name": "textembedding-gecko@003",
#         "project": "PROJECT-123",
#         "key_file_path": "C:/path/to/the/json/authentication.json",
#         "location": "us-central1"
#         }


#         embed_client = EmbeddingClient(**embed_config)

# 
#         chroma_creator = ChromaCollectionCreator(processor, embed_client)

#         with st.form("Load Data to Chroma"):
#             st.subheader("Quiz Builder")
#             st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
#        
#             #Use streamlit widgets to capture the user's input
#             topic = st.text_input("Enter the quiz topic:")

#             # for the quiz topic and the desired number of questions
#        
#             num_questions = st.slider("Select the number of questions", min_value=1, max_value= 10, value = 5)

#             document = None
            
#             submitted = st.form_submit_button("Generate a Quiz!")
#             if submitted:
#          
#                 # 5) Use the create_chroma_collection() method to create a Chroma collection from the processed documents
#           

#                 chroma_collection = chroma_creator.create_chroma_collection()
                    
#                 # Uncomment the following lines to test the query_chroma_collection() method
#                 document = chroma_creator.query_chroma_collection(topic) 
                
#     if document:
#         screen.empty() # Screen 2
#         with st.container():
#             st.header("Query Chroma for Topic, top Document: ")
#             st.write(document)
