from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

from app.models.enums import LoggerLevel


class LoggerSettings(BaseSettings):
    level: LoggerLevel = Field(default=LoggerLevel.INFO, alias="LOGGER_LEVEL")
    sink: str = Field(default="logs/kafka-admin-py.log", alias="LOGGER_SINK")
    rotation: str = Field(default="10 MB", alias="LOGGER_ROTATION")
    retention: str = Field(default="10 days", alias="LOGGER_RETENTION")
    compression: str = Field(default="zip", alias="LOGGER_COMPRESSION")

    model_config = SettingsConfigDict(env_file=".env")
