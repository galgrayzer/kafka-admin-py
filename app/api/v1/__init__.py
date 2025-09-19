from fastapi import APIRouter

from .endpoints import topic_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(topic_router)

__all__ = ["v1_router"]
