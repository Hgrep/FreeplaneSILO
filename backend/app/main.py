from fastapi import FastAPI
from app.api.v1 import health, mindmaps, tags

app = FastAPI(title="FreeplaneSILO API")

app.include_router(health.router, prefix="/api/v1")
app.include_router(mindmaps.router, prefix="/api/v1")
app.include_router(tags.router, prefix="/api/v1")
