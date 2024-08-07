from src.helper import load_pdf, create_text_chunks, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf("data/")
text_chunks = create_text_chunks(extracted_data)
embeddings = download_hugging_face_embeddings()

# Initilising Pinecone (knowledge base)
pc = Pinecone()

# Pinecone index
index_name = 'chatbot-index'


# Create embeddings for each text chunk and store
doc_search = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)