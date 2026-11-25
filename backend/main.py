from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.database import initialize_database
from backend.routers import auth, health, scanning, users


# Initializes the database before the API starts handling requests.
@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncGenerator[None, None]:
    initialize_database()
    yield


app = FastAPI(title="Access Control System API", lifespan=lifespan)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(scanning.router)