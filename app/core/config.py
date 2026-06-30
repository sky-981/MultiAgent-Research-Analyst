"""App configuration — .env se type-safe load (pydantic-settings)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # .env me extra keys ho to crash na ho
    )

    app_env: str = "local"

    # LLM (LiteLLM model string se provider decide hota)
    llm_model: str = "gemini/gemini-1.5-flash"
    gemini_api_key: str = ""
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    # Web search
    tavily_api_key: str = ""

    # Observability (Langfuse)
    langfuse_public_key: str = ""
    langfuse_secret_key: str = ""
    langfuse_host: str = "http://localhost:3000"


# Ek hi instance poore app me import hota
settings = Settings()
