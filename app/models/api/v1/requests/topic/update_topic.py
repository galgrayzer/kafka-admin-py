from pydantic import BaseModel, Field, PositiveInt


class IncreaseNumberOfPartitionsRequest(BaseModel):
    num_partitions: PositiveInt = Field(
        description="New number of partitions for the topic",
    )
