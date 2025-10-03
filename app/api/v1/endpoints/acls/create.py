from concurrent.futures import Future
from fastapi import Request, HTTPException
from confluent_kafka.admin import (
    AclBinding,
    AdminClient,
    ResourcePatternType,
)
from confluent_kafka import KafkaException

from app.models.api.v1.requests.acls import CreateACLRequest

from .acls_route import acls_router
from app.logger import logger


@acls_router.post("", summary="Create new ACL on the Kafka cluster")
def create_acl(requst: Request, create_acl_request: CreateACLRequest) -> dict[str, str]:
    admin_client: AdminClient = requst.state.kafka_client.get_admin_client()
    bootstrap_servers: str = requst.state.bootstrap_servers

    logger.bind(
        bootstrap_servers=bootstrap_servers,
        restype=create_acl_request.resource_type,
        name=create_acl_request.resource_name,
        principal=create_acl_request.principal,
        host=create_acl_request.host,
        operation=create_acl_request.operation,
        permission_type=create_acl_request.permission_type,
        resource_pattern_type=ResourcePatternType.LITERAL,
    ).info("Creating new ACL on the Kafka cluster")

    acl_binding: AclBinding = AclBinding(
        restype=create_acl_request.resource_type,
        name=create_acl_request.resource_name,
        principal=create_acl_request.principal,
        host=create_acl_request.host,
        operation=create_acl_request.operation,
        permission_type=create_acl_request.permission_type,
        resource_pattern_type=ResourcePatternType.LITERAL,
    )
    future: Future[None] = admin_client.create_acls([acl_binding])[acl_binding]

    try:
        future.result()
        logger.bind(
            bootstrap_servers=bootstrap_servers,
            restype=create_acl_request.resource_type,
            name=create_acl_request.resource_name,
            principal=create_acl_request.principal,
            host=create_acl_request.host,
            operation=create_acl_request.operation,
            permission_type=create_acl_request.permission_type,
            resource_pattern_type=ResourcePatternType.LITERAL,
        ).success("ACL created successfuly")
    except KafkaException as e:
        logger.bind(
            bootstrap_servers=bootstrap_servers,
            restype=create_acl_request.resource_type,
            name=create_acl_request.resource_name,
            principal=create_acl_request.principal,
            host=create_acl_request.host,
            operation=create_acl_request.operation,
            permission_type=create_acl_request.permission_type,
            resource_pattern_type=ResourcePatternType.LITERAL,
        ).error(f"Failed to create new ACL: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "ACL created"}
