from .app_settings import AppSettings
from .fast_settings import FastSettings
from .logger_settings import LoggerSettings

app_settings = AppSettings()
fast_settings = FastSettings()
logger_settings = LoggerSettings()

__all__ = ["app_settings", "fast_settings", "logger_settings"]
