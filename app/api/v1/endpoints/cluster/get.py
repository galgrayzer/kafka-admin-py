from fastapi import Request, HTTPException
from confluent_kafka.admin import AdminClient
from confluent_kafka import KafkaException

from .cluster_route import cluster_router
from app.logger import logger


@cluster_router.get("/list-topics", summary="List all topics in Kafka cluster")
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
