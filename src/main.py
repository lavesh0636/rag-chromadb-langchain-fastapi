from fastapi import FastAPI

app = FastAPI(
    title="RAG Application API",
    description="API for the RAG system using ChromaDB, LangChain, and FastAPI.",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
