from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.models.enums import AppEnvironment
from . import app_settings


class FastSettings(BaseSettings):
    host: str = Field(default="0.0.0.0", alias="FAST_HOST")
    port: int = Field(default=8000, alias="FAST_PORT")
    reload: bool = Field(
        default=(app_settings.environment is AppEnvironment.DEVELOPMENT),
        alias="FAST_RELOAD",
    )

    model_config = SettingsConfigDict(env_file=".env")
