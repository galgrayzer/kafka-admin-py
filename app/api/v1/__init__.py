from fastapi import APIRouter, Depends


from app.api.v1.middlewares import (
    extract_bootstrap_servers,
    extract_kafka_credentials,
    create_kafka_client,
)

from app.api.v1.swagger_docs import (
    docs_bootstrap_servers,
    docs_kafka_password,
    docs_kafka_username,
)

from .endpoints import topic_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(
    topic_router,
    dependencies=[
        Depends(docs_bootstrap_servers),
        Depends(docs_kafka_username),
        Depends(docs_kafka_password),
        Depends(extract_bootstrap_servers),
        Depends(extract_kafka_credentials),
        Depends(create_kafka_client),
    ],
)

__all__ = ["v1_router"]
