from confluent_kafka.admin import AclOperation, AclPermissionType, ResourceType
from pydantic import BaseModel, Field


class CreateACLRequest(BaseModel):
    resource_type: ResourceType = Field(
        description="The resource type.",
        examples=[ResourceType.TOPIC, ResourceType.BROKER, ResourceType.ANY],
    )
    resource_name: str = Field(
        description="The resource name, which depends on the resource type. For ResourceType.BROKER, the resource name is the broker id.",
        examples=["test-topic", "broker1"],
    )
    principal: str = Field(
        description="The principal this AclBinding refers to.", examples=["user1"]
    )
    host: str = Field(
        default="*", description="The host that the call is allowed to come from."
    )
    operation: AclOperation = Field(
        description="The operation/s specified by this binding."
    )
    permission_type: AclPermissionType = Field(
        description="The permission type for the specified operation."
    )
