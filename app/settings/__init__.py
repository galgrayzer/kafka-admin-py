from .app_settings import AppSettings
from .fast_settings import FastSettings
from .kafka_settings import KafkaSettings
from .logger_settings import LoggerSettings

app_settings = AppSettings()
fast_settings = FastSettings()
kafka_settings = KafkaSettings()
logger_settings = LoggerSettings()

__all__ = ["app_settings", "fast_settings", "kafka_settings", "logger_settings"]
