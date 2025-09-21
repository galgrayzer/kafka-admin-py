from .topic_route import topic_router
from .get import get_topic_metadata
from .create import create_topic
from .delete import delete_topic
from .update import increase_topic_partitions

__all__ = [
    "topic_router",
    "get_topic_metadata",
    "create_topic",
    "delete_topic",
    "increase_topic_partitions",
]
