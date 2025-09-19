from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .settings import fast_settings


class AppFactory:
    @staticmethod
    def create_app() -> FastAPI:
        app = FastAPI(
            title=fast_settings.title,
            description=fast_settings.description,
            version=fast_settings.version,
        )

        # Add CORS middleware
        app.add_middleware(
            middleware_class=CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        return app
