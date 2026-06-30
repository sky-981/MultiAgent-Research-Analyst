"""FastAPI entrypoint. Run: uvicorn app.main:app --reload"""

from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title="MultiAgent Research Analyst",
    version="0.1.0",
    description="Autonomous multi-agent research system (LangGraph + FastAPI).",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness check — server zinda hai ya nahi."""
    return {"status": "ok", "env": settings.app_env}
