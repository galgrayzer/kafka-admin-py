from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.models.enums import AppEnvironment
from . import app_settings


class FastSettings(BaseSettings):
    host: str = Field(default="0.0.0.0", alias="FAST_HOST")
    port: PositiveInt = Field(default=8000, alias="FAST_PORT")
    reload: bool = Field(
        default=(app_settings.environment is AppEnvironment.DEVELOPMENT),
        alias="FAST_RELOAD",
    )
    title: str = Field(default="My API", alias="FAST_TITLE")
    description: str = Field(default="This is a sample API", alias="FAST_DESCRIPTION")
    version: str = Field(default="1.0.0", alias="FAST_VERSION")

    model_config = SettingsConfigDict(env_file=".env")
