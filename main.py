from fastapi import FastAPI
import uvicorn

from src.factory import AppFactory
from src.settings import fast_settings
from src.settings import app_settings

fast_app: FastAPI = AppFactory.create_app()

if __name__ == "__main__":
    uvicorn.run(
        fast_app,
        host=fast_settings.host,
        port=fast_settings.port,
        reload=fast_settings.reload,
        workers=app_settings.workers,
    )
    
