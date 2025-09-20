from fastapi import Request
from .topic_route import topic_router


@topic_router.get("")
def get_topics(request: Request) -> dict[str, str]:
    return {"bootstrap.servers": request.state.bootstrap_servers}
