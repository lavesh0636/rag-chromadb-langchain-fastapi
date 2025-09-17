# src/core/langchain_setup.py

from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

# TODO: Load model names and parameters from config/settings.py
LLM_MODEL = "llama3"
EMBEDDING_MODEL = "llama3"

def initialize_llm():
    """Initializes the LLM model."""
    print(f"Initializing LLM with model: {LLM_MODEL}")
    # Replace with your preferred LLM initialization
    llm = Ollama(model=LLM_MODEL)
    return llm

def initialize_embeddings():
    """Initializes the embedding model."""
    print(f"Initializing embeddings with model: {EMBEDDING_MODEL}")
    # Replace with your preferred embedding model initialization
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    return embeddings

