from fastapi import Query, Header
from app.settings import kafka_settings


def docs_bootstrap_servers(
    bootstrap_servers: str = Query(
        "localhost:9092", description="Kafka bootstrap servers list"
    ),
) -> str:
    return bootstrap_servers


def docs_kafka_username(
    kafka_username: str = Header(
        kafka_settings.default_username,
        description="Kafka username",
        alias="Kafka-Username",
    ),
) -> str:
    return kafka_username


def docs_kafka_password(
    kafka_password: str = Header(
        kafka_settings.default_password,
        description="Kafka password",
        alias="Kafka-Password",
    ),
) -> str:
    return kafka_password
