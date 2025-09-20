from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class KafkaSettings(BaseSettings):
    default_username: str = Field(default="admin", alias="KAFKA_DEFAULT_USERNAME")
    default_password: str = Field(
        default="admin-secret", alias="KAFKA_DEFAULT_PASSWORD"
    )
    scram_mechanism: str = Field(default="SCRAM-SHA-256", alias="KAFKA_SCRAM_MECHANISM")
    security_protocol: str = Field(
        default="SASL_PLAINTEXT", alias="KAFKA_SECURITY_PROTOCOL"
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
