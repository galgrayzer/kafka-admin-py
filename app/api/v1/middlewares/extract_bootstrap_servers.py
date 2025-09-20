from fastapi import Request

from app.logger import logger
from fastapi import HTTPException


def extract_bootstrap_servers(request: Request) -> None:
    bootstrap_servers = request.query_params.get("bootstrap_servers")
    if bootstrap_servers:
        request.state.bootstrap_servers = bootstrap_servers
        logger.debug(f"Extracted bootstrap servers: {bootstrap_servers}")
    else:
        raise HTTPException(
            status_code=400, detail="Missing 'bootstrap_server' query parameter."
        )
