from confluent_kafka.admin import AdminClient
from confluent_kafka.serializing_producer import SerializingProducer
from confluent_kafka.deserializing_consumer import DeserializingConsumer

from app.logger import logger


class KafkaClient:
    def __init__(self, config: dict[str, str]) -> None:
        self.config: dict[str, str] = config
        self._admin_client: AdminClient | None = None
        self._producer: SerializingProducer | None = None
        self._consumer: DeserializingConsumer | None = None

    def get_admin_client(self) -> AdminClient:
        if self._admin_client is None:
            self._admin_client = AdminClient(self.config)
            logger.debug(f"Initialized new AdminClient with config: {self.config}")
        return self._admin_client

    def get_producer(self) -> SerializingProducer:
        if self._producer is None:
            self._producer = SerializingProducer(self.config)
            logger.debug(
                f"Initialized new SerializingProducer with config: {self.config}"
            )
        return self._producer

    def get_consumer(self) -> DeserializingConsumer:
        if self._consumer is None:
            self._consumer = DeserializingConsumer(self.config)
            logger.debug(
                f"Initialized new DeserializingConsumer with config: {self.config}"
            )
        return self._consumer
