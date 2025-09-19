from ._app_settings import AppSettings
from ._fast_settings import FastSettings
from ._logger_settings import LoggerSettings

app_settings = AppSettings()
fast_settings = FastSettings()
logger_settings = LoggerSettings()

__all__ = ["app_settings", "fast_settings", "logger_settings"]
