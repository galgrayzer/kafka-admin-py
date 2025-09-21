from fastapi import HTTPException, Request
from confluent_kafka.admin import AdminClient
from confluent_kafka import KafkaException
from asyncio import Future

from .topic_route import topic_router
from app.logger import logger


@topic_router.delete("/{topic_name}", summary="Delete a topic")
def delete_topic(request: Request, topic_name: str) -> dict[str, str]:
    admin_client: AdminClient = request.state.kafka_client.get_admin_client()
    bootstrap_servers: str = request.state.bootstrap_servers
    logger.bind(bootstrap_servers=bootstrap_servers)

    logger.info(f"Deleting topic {topic_name}")

    future: Future[None] = admin_client.delete_topics([topic_name])[topic_name]

    try:
        future.result()
        logger.success(f"Topic {topic_name} has been deleted")
    except KafkaException as e:
        logger.error(f"Error deleting topic {topic_name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": f"Topic {topic_name} has been deleted"}
