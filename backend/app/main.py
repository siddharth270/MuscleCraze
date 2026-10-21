"""FastAPI app factory: create app, mount routers, register middleware/startup hooks."""
from fastapi import FastAPI

from app.api.v1 import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version=settings.version)
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()
