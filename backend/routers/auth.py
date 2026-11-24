from fastapi import APIRouter, HTTPException, status

from backend.models import LoginRequest, LoginResponse


router = APIRouter(prefix="/api", tags=["Administrator"])


# Authenticates an administrator and returns an access token.
@router.post(
    "/login",
    response_model=LoginResponse,
    summary="Administrator login",
    responses={501: {"description": "Not implemented"}},
)
def login(login_request: LoginRequest) -> LoginResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )


# Invalidates the current administrator session.
@router.post(
    "/logout",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Administrator logout",
    responses={501: {"description": "Not implemented"}},
)
def logout() -> None:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )
