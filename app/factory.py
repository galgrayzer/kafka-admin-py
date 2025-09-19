from fastapi import FastAPI

from .settings import fast_settings


class AppFactory:
    @staticmethod
    def create_app() -> FastAPI:
        app = FastAPI(
            title=fast_settings.title,
            description=fast_settings.description,
            version=fast_settings.version,
        )
        AppFactory._include_routers(app)
        return app

    @staticmethod
    def _include_routers(app: FastAPI) -> None:
        from .api import api_router

        app.include_router(api_router)
