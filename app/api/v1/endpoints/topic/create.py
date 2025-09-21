from fastapi import Request, HTTPException
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import KafkaException
from concurrent.futures import Future

from .topic_route import topic_router
from app.models.api.v1.requests.topic import CreateTopicRequest
from app.logger import logger


@topic_router.post("/{topic_name}", summary="Create a new topic")
def create_topic(
    request: Request, topic_name: str, create_topic_request: CreateTopicRequest
) -> dict[str, str]:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers
    logger.bind(bootstrap_servers=bootstrap_servers)

    logger.info(
        f"Creating topic '{topic_name}' with {create_topic_request.num_partitions} partitions "
        f"and replication factor {create_topic_request.replication_factor}"
    )

    future: Future[None] = admin_client.create_topics(
        [
            NewTopic(
                topic=topic_name,
                num_partitions=create_topic_request.num_partitions,
                replication_factor=create_topic_request.replication_factor,
                config=create_topic_request.config or {},
            )
        ]
    )[topic_name]

    try:
        future.result()
        logger.success(f"Topic '{topic_name}' created successfully")
    except KafkaException as e:
        logger.error(f"Error creating topic '{topic_name}': {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": f"Topic '{topic_name}' created successfully"}
