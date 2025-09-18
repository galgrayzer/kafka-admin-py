from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, PositiveInt
from src.models.enums import AppEnvironment


class AppSettings(BaseSettings):
    environment: AppEnvironment = Field(
        default=AppEnvironment.DEVELOPMENT, alias="APP_ENVIRONMENT"
    )
    workers: PositiveInt = Field(default=1, alias="APP_WORKERS")

    model_config = SettingsConfigDict(env_file=".env")
