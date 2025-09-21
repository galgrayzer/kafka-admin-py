from asyncio import Future
from fastapi import Request, HTTPException
from confluent_kafka.admin import (
    AdminClient,
    TopicDescription as ConfluentTopicMetadata,
    ConfigResource,
    ConfigEntry,
)
from confluent_kafka import KafkaException, TopicCollection


from .topic_route import topic_router
from app.logger import logger
from app.models.confluent_kafka import TopicDescription
from app.utils.confluent_kafka import load_topic_description


@topic_router.get("/{topic_name}/metadata", summary="Get topic metadata")
def get_topic_metadata(request: Request, topic_name: str) -> TopicDescription:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers
    logger.bind(bootstrap_servers=bootstrap_servers)

    logger.info(f"Fetching topic {topic_name} metadata")

    future: Future[ConfluentTopicMetadata] = admin_client.describe_topics(
        TopicCollection([topic_name])
    )[topic_name]

    try:
        topic_metadata: ConfluentTopicMetadata = future.result()
        logger.success(f"Successfully fetched topic {topic_name} metadata")
    except KafkaException as e:
        logger.error(f"Error fetching topic {topic_name} metadata: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return load_topic_description(topic_metadata)


@topic_router.get("/{topic_name}/configs", summary="Get topic configs")
def get_topic_configs(request: Request, topic_name: str) -> dict[str, str]:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers
    logger.bind(bootstrap_servers=bootstrap_servers)

    logger.info(f"Fetching topic {topic_name} configs")

    topic_config_resource = ConfigResource(
        name=topic_name, restype=ConfigResource.Type.TOPIC
    )
    future: Future[dict[str, ConfigEntry]] = admin_client.describe_configs(
        [topic_config_resource]
    )[topic_config_resource]

    try:
        topic_configs: dict[str, ConfigEntry] = future.result()
        logger.success(f"Successfully fetched topic {topic_name} configs")
    except KafkaException as e:
        logger.error(f"Error fetching topic {topic_name} configs: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {k: v.value for k, v in topic_configs.items()}
