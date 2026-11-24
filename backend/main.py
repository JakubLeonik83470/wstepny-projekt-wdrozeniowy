from fastapi import FastAPI

from backend.routers import auth, health, scanning, users

app = FastAPI(title="Access Control System API")

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(scanning.router)