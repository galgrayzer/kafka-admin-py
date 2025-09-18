from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from src.models.enums import AppEnvironment


class AppSettings(BaseSettings):
    environment: AppEnvironment = Field(
        default=AppEnvironment.DEVELOPMENT, alias="APP_ENVIRONMENT"
    )

    model_config = SettingsConfigDict(env_file=".env")
