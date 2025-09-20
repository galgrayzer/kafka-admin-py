from fastapi import APIRouter, Depends, Query


from app.api.v1.middlewares import extract_bootstrap_servers


def docs_bootstrap_servers(
    bootstrap_servers: str = Query(..., description="Kafka bootstrap servers list"),
) -> str:
    return bootstrap_servers


topic_router = APIRouter(
    prefix="/topic",
    tags=["topic"],
    dependencies=[Depends(docs_bootstrap_servers), Depends(extract_bootstrap_servers)],
)
