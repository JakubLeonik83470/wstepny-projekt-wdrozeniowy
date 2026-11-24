from fastapi import APIRouter

from backend.models import HealthResponse


router = APIRouter(tags=["System"])


# Reports whether the API process is responding.
@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok")
