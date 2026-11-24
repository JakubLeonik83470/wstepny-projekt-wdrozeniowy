from pydantic import BaseModel, Field


# Response model for GET /health in routers/health.py.
class HealthResponse(BaseModel):
    status: str


# Request model for POST /api/login in routers/auth.py.
class LoginRequest(BaseModel):
    username: str = Field(description="Administrator username")
    password: str = Field(description="Administrator password")


# Response model for POST /api/login in routers/auth.py.
class LoginResponse(BaseModel):
    access_token: str = Field(description="Session token for subsequent requests")
    token_type: str = "bearer"


# Response model for user endpoints in routers/users.py.
class UserResponse(BaseModel):
    id: int
    full_name: str
    permission: str = Field(description="User permission")


# Response model for POST /api/users and POST /api/scan.
class OperationResponse(BaseModel):
    status: str
    message: str
