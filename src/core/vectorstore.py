# src/core/vectorstore.py

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

# TODO: Load ChromaDB persistence path from config/settings.py
CHROMA_DB_PATH = "./chroma_db"

def get_vector_store(embeddings: Embeddings):
    """Initializes and returns the ChromaDB vector store."""
    print(f"Initializing ChromaDB vector store at: {CHROMA_DB_PATH}")
    vector_store = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
    return vector_store

