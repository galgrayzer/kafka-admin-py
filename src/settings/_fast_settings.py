from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict
from os import getenv

from src.models.enums import AppEnvironment


class FastSettings(BaseSettings):
    host: str = Field(default="0.0.0.0", alias="FAST_HOST")
    port: PositiveInt = Field(default=3000, alias="FAST_PORT")
    reload: bool = Field(
        default=(
            getenv("APP_ENVIRONMENT", AppEnvironment.DEVELOPMENT)
            is AppEnvironment.DEVELOPMENT
        ),
        alias="FAST_RELOAD",
    )
    title: str = Field(default="Kafka Admin PY", alias="FAST_TITLE")
    description: str = Field(
        default="A REST API that does Kafka operations on clusters",
        alias="FAST_DESCRIPTION",
    )
    version: str = Field(default="1.0.0", alias="FAST_VERSION")

    model_config = SettingsConfigDict(env_file=".env")
