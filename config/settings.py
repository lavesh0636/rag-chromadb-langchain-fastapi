# src/config/settings.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # LangChain settings
    llm_model: str = "llama3" # Default LLM model name
    embedding_model: str = "llama3" # Default embedding model name

    # ChromaDB settings
    chroma_db_path: str = "./chroma_db" # Path to store ChromaDB data

    # API settings
    api_prefix: str = "/api/v1"

    # You can add more settings here, e.g., for API keys, search engines, etc.

    class Config:
        # Load environment variables from a .env file if it exists
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() # Global instance of settings
