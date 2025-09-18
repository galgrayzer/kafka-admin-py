from fastapi import FastAPI
import uvicorn

from src.factory import AppFactory
from src.settings import fast_settings
from src.settings import app_settings
from src.logger import logger

fast_app: FastAPI = AppFactory.create_app()

if __name__ == "__main__":
    logger.info(
        f"Starting {fast_app.title} on {fast_settings.host}:{fast_settings.port}"
    )
    uvicorn.run(
        "main:fast_app",
        host=fast_settings.host,
        port=fast_settings.port,
        reload=fast_settings.reload,
        workers=app_settings.workers,
    )
