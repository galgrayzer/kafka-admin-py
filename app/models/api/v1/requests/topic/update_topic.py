from pydantic import BaseModel, Field, PositiveInt


class IncreaseNumberOfPartitionsRequest(BaseModel):
    num_partitions: PositiveInt = Field(
        description="New number of partitions for the topic",
    )


class AlterTopicConfigsRequest(BaseModel):
    config: dict[str, str] = Field(
        description="Configuration settings for the new topic",
        examples=[{"cleanup.policy": "delete", "retention.ms": "604800000"}],
    )
