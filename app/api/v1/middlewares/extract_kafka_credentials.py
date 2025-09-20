from fastapi import Request

from app.logger import logger
from app.settings import kafka_settings


def extract_kafka_credentials(request: Request) -> None:
    kafka_username: str | None = request.headers.get(
        "Kafka-Username", kafka_settings.default_username
    )
    kafka_password: str | None = request.headers.get(
        "Kafka-Password", kafka_settings.default_password
    )

    request.state.kafka_username = kafka_username
    request.state.kafka_password = kafka_password

    logger.debug("Extracted Kafka credentials from headers")
