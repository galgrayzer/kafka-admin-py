from asyncio import Future
from fastapi import Request, HTTPException
from confluent_kafka.admin import (
    AdminClient,
    TopicDescription as ConfluentTopicMetadata,
)
from confluent_kafka import KafkaException, TopicCollection


from .topic_route import topic_router
from app.logger import logger
from app.models.confluent_kafka import TopicDescription
from app.utils.confluent_kafka import load_topic_description


@topic_router.get("/list", summary="List all topics")
def get_topics(request: Request) -> list[str]:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers

    logger.bind(bootstrap_servers=bootstrap_servers).info(
        "Fetching all topics from Kafka Cluster"
    )
    try:
        topic_list = admin_client.list_topics().topics
        logger.bind(bootstrap_servers=bootstrap_servers).success(
            "Fetched all topics successfully"
        )
    except KafkaException as e:
        logger.bind(bootstrap_servers=bootstrap_servers).error(
            f"Error fetching topics: {e}"
        )
        raise HTTPException(status_code=500, detail=str(e))

    return list(topic_list)


@topic_router.get("/{topic_name}", summary="Get topic metadata")
def get_topic_metadata(request: Request, topic_name: str) -> TopicDescription:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers

    logger.bind(bootstrap_servers=bootstrap_servers).info(
        f"Fetching topic {topic_name} metadata"
    )
    try:
        future: Future[ConfluentTopicMetadata] = admin_client.describe_topics(
            TopicCollection([topic_name])
        )[topic_name]
        topic_metadata: ConfluentTopicMetadata = future.result()
        logger.bind(bootstrap_servers=bootstrap_servers).success(
            f"Successfully fetched topic {topic_name} metadata"
        )
    except KafkaException as e:
        logger.bind(bootstrap_servers=bootstrap_servers).error(
            f"Error fetching topic {topic_name} metadata: {e}"
        )
        raise HTTPException(status_code=500, detail=str(e))

    return load_topic_description(topic_metadata)
