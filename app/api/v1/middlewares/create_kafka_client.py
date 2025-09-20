from fastapi import Request
from fastapi import HTTPException

from app.logger import logger
from app.services.confluent_kafka import KafkaClient


def create_kafka_client(request: Request) -> None:
    bootstrap_servers: str = request.state.bootstrap_servers
    