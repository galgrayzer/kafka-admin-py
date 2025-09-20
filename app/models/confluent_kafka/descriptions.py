from pydantic import BaseModel
from typing import Optional


class NodeDescription(BaseModel):
    id: int
    host: str
    port: int
    rack: Optional[str]


class PartitionDescription(BaseModel):
    id: int
    leader: NodeDescription
    replicas: list[NodeDescription]
    isr: list[NodeDescription]


class TopicDescription(BaseModel):
    name: str
    topic_id: str
    partitions: list[PartitionDescription]
    is_internal: bool
