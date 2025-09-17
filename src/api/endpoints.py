from fastapi import APIRouter

router = APIRouter()

@router.get("/health", summary="Health Check")
def health_check():
    """Checks if the API is running."""
    return {"status": "ok"}
