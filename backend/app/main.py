from fastapi import FastAPI
from app.api.v1 import health, mindmaps, tags
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(title="FreeplaneSILO API")

app.include_router(health.router, prefix="/api/v1")
app.include_router(mindmaps.router, prefix="/api/v1")
app.include_router(tags.router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)