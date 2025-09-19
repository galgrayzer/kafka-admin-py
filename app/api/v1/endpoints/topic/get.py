from .topic_route import topic_router


@topic_router.get("")
def get_topics() -> dict[str, str]:
    return {"message": "List of topics"}
