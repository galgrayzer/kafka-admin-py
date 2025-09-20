from confluent_kafka.admin import TopicDescription as ConfluentTopicDescription
from app.models.confluent_kafka.descriptions import (
    NodeDescription,
    PartitionDescription,
    TopicDescription,
)


def load_topic_description(
    topic_description: ConfluentTopicDescription,
) -> TopicDescription:
    return TopicDescription(
        name=topic_description.name,
        topic_id=str(topic_description.topic_id),
        partitions=[
            PartitionDescription(
                id=partition.id,
                leader=NodeDescription(
                    id=partition.leader.id,
                    host=partition.leader.host,
                    port=partition.leader.port,
                    rack=partition.leader.rack,
                ),
                replicas=[
                    NodeDescription(
                        id=replica.id,
                        host=replica.host,
                        port=replica.port,
                        rack=replica.rack,
                    )
                    for replica in partition.replicas
                ],
                isr=[
                    NodeDescription(
                        id=replica.id,
                        host=replica.host,
                        port=replica.port,
                        rack=replica.rack,
                    )
                    for replica in partition.isr
                ],
            )
            for partition in topic_description.partitions
        ],
        is_internal=topic_description.is_internal,
    )
