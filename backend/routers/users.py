from fastapi import APIRouter, HTTPException, Path, Response, status

from backend.models import (
    OperationResponse,
    UserResponse,
)

router = APIRouter(prefix="/api/users", tags=["Users"])


# Returns the collection of registered users.
@router.get(
    "",
    response_model=list[UserResponse],
    summary="Get the user list",
    responses={501: {"description": "Not implemented"}},
)
def get_users() -> list[UserResponse]:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )


# Returns one user selected by their ID.
@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get a user",
    responses={
        404: {"description": "User not found"},
        501: {"description": "Not implemented"},
    },
)
def get_user(user_id: int = Path(ge=1)) -> UserResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )


# Starts the user registration script and returns its operation status.
@router.post(
    "",
    response_model=OperationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
    responses={501: {"description": "Not implemented"}},
)
def create_user() -> OperationResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )


# Deletes the user selected by their ID.
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a user",
    responses={
        404: {"description": "User not found"},
        501: {"description": "Not implemented"},
    },
)
def delete_user(user_id: int = Path(ge=1)) -> Response:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented",
    )