from ._app_settings import AppSettings
from ._fast_settings import FastSettings

app_settings = AppSettings()
fast_settings = FastSettings()

__all__ = ["app_settings", "fast_settings"]
