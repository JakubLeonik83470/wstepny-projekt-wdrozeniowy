from fastapi import APIRouter, HTTPException, status

from backend.models import OperationResponse


router = APIRouter(prefix="/api", tags=["Scanning"])


# Starts the face scanning script and returns its operation status.
@router.post(
    "/scan",
    response_model=OperationResponse,
    summary="Face scan and access verification",
    responses={501: {"description": "Not implemented"}},
)
def scan() -> OperationResponse:
    # TODO: Run the face scanning script and return its result.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )
