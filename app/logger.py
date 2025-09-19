from loguru import logger

from .settings import logger_settings

logger.add(
    sink=logger_settings.sink,
    level=logger_settings.level,
    rotation=logger_settings.rotation,
    retention=logger_settings.retention,
    compression=logger_settings.compression,
)

__all__ = ["logger"]
