from confluent_kafka.admin import AdminClient
from confluent_kafka.serializing_producer import SerializingProducer
from confluent_kafka.deserializing_consumer import DeserializingConsumer

from app.logger import logger
from app.settings import kafka_settings


class KafkaClient:
    def __init__(
        self, bootstrap_servers: str, scram_username: str, scram_password: str
    ) -> None:
        self._base_config: dict[str, str] = {
            "bootstrap.servers": bootstrap_servers,
            "security.protocol": kafka_settings.security_protocol,
            "sasl.mechanism": kafka_settings.scram_mechanism,
            "sasl.username": scram_username,
            "sasl.password": scram_password,
        }
        self._admin_client: AdminClient | None = None
        self._producer: SerializingProducer | None = None
        self._consumer: DeserializingConsumer | None = None

    def get_admin_client(self, config: dict[str, str]) -> AdminClient:
        if self._admin_client is None:
            config.update(self._base_config)
            self._admin_client = AdminClient(config)
            logger.debug(f"Initialized new AdminClient with config: {config}")
        return self._admin_client

    def get_producer(self, config: dict[str, str]) -> SerializingProducer:
        if self._producer is None:
            config.update(self._base_config)
            self._producer = SerializingProducer(config)
            logger.debug(f"Initialized new SerializingProducer with config: {config}")
        return self._producer

    def get_consumer(self, config: dict[str, str]) -> DeserializingConsumer:
        if self._consumer is None:
            config.update(self._base_config)
            self._consumer = DeserializingConsumer(config)
            logger.debug(f"Initialized new DeserializingConsumer with config: {config}")
        return self._consumer
