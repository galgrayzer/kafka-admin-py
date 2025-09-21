from fastapi import HTTPException, Request
from confluent_kafka.admin import (
    AdminClient,
    NewPartitions,
    ConfigResource,
    ConfigEntry,
    AlterConfigOpType,
)
from confluent_kafka import KafkaException
from asyncio import Future

from .topic_route import topic_router
from app.logger import logger
from app.models.api.v1.requests.topic import (
    IncreaseNumberOfPartitionsRequest,
    AlterTopicConfigsRequest,
)


@topic_router.put(
    "/{topic_name}/partitions", summary="Increase the number of topic partitions"
)
def increase_topic_partitions(
    request: Request,
    topic_name: str,
    increase_partitions_request: IncreaseNumberOfPartitionsRequest,
) -> dict[str, str]:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers
    logger.bind(bootstrap_servers=bootstrap_servers)

    logger.info(
        f"Increasing topic {topic_name} number of partitions to {increase_partitions_request.num_partitions}"
    )
    new_topic_partitions: NewPartitions = NewPartitions(
        topic_name, increase_partitions_request.num_partitions
    )
    future: Future[None] = admin_client.create_partitions([new_topic_partitions])[
        topic_name
    ]
    try:
        future.result()
        logger.success(
            f"Number of partitions for topic {topic_name} has been increased"
        )
    except KafkaException as e:
        logger.error(
            f"Error when trying to increase topic {topic_name} number of partitions: {e}"
        )
        raise HTTPException(status_code=500, detail=str(e))

    return {"detail": f"Number of partitions for topic {topic_name} has been increased"}


@topic_router.put("/{topic_name}/configs", summary="Alter topic config")
def alter_topic_config(
    request: Request,
    topic_name: str,
    alter_topic_config_request: AlterTopicConfigsRequest,
) -> dict[str, str]:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers
    logger.bind(bootstrap_servers=bootstrap_servers)

    logger.info(f"Altering topic {topic_name} configs")
    topic_new_configs: list[ConfigEntry] = [
        ConfigEntry(name, value, incremental_operation=AlterConfigOpType.SET)
        for name, value in alter_topic_config_request.config.items()
    ]
    topic_config_resource: ConfigResource = ConfigResource(
        restype=ConfigResource.Type.TOPIC,
        name=topic_name,
        incremental_configs=topic_new_configs,
    )
    future: Future[None] = admin_client.incremental_alter_configs(
        [topic_config_resource]
    )[topic_config_resource]
    try:
        future.result()
        logger.success(f"Successfully updated topic {topic_name} configs")
    except KafkaException as e:
        logger.error(f"Error when trying to alter topic {topic_name} configs: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": f"Successfully updated topic {topic_name} configs"}
