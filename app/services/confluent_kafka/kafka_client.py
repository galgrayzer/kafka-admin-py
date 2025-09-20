from confluent_kafka.admin import AdminClient
from confluent_kafka import Producer, Consumer


class KafkaClient:
    def __init__(self, config: dict[str, str]) -> None:
        self.config: dict[str, str] = config
        self._admin_client: AdminClient | None = None
        self._producer: Producer | None = None
        self._consumer: Consumer | None = None

    def get_admin_client(self) -> AdminClient:
        if self._admin_client is None:
            self._admin_client = AdminClient(self.config)
        return self._admin_client

    def get_producer(self) -> Producer:
        if self._producer is None:
            self._producer = Producer(self.config)
        return self._producer

    def get_consumer(self) -> Consumer:
        if self._consumer is None:
            self._consumer = Consumer(self.config)
        return self._consumer
