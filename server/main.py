import logging

from fastapi import FastAPI

from server.api.slack_events import router as slack_router
from server.api.chat import router as chat_router
from server.config import settings
from server.models.database import engine, Base

logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)

app = FastAPI(title="AI HR Chatbot", version="0.1.0")

app.include_router(slack_router, prefix="/api/slack")
app.include_router(chat_router, prefix="/api")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/health/db")
async def health_db():
    from sqlalchemy import text
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
