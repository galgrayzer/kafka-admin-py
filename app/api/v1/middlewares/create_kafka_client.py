from fastapi import Request

from app.services.confluent_kafka import KafkaClient
from app.logger import logger


def create_kafka_client(request: Request) -> None:
    bootstrap_servers: str = request.state.bootstrap_servers
    scram_username: str = request.state.kafka_username
    scram_password: str = request.state.kafka_password

    kafka_client = KafkaClient(
        bootstrap_servers=bootstrap_servers,
        scram_username=scram_username,
        scram_password=scram_password,
    )

    request.state.kafka_client = kafka_client

    logger.debug("Kafka client created and attached to request")
