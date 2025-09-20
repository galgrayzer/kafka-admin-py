from pydantic import BaseModel, Field, PositiveInt
from typing import Optional


class CreateTopicRequest(BaseModel):
    num_partitions: PositiveInt = Field(
        default=1,
        description="Number of partitions for the new topic",
        examples=[3],
        ge=1,
    )
    replication_factor: PositiveInt = Field(
        default=1,
        description="Replication factor for the new topic",
        examples=[1, 2, 3],
        ge=1,
    )
    config: Optional[dict[str, str]] = Field(
        description="Configuration settings for the new topic",
        examples=[{"cleanup.policy": "delete", "retention.ms": "604800000"}],
    )
