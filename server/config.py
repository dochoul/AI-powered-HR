from pathlib import Path

from pydantic_settings import BaseSettings

_ENV_FILE = Path(__file__).parent / ".env"


class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://hrbot:hrbot_password@localhost:5433/hr_chatbot"

    # Gemini API
    gemini_api_key: str = ""

    # Slack
    slack_bot_token: str = ""
    slack_signing_secret: str = ""
    slack_app_token: str = ""

    # App
    app_env: str = "development"
    log_level: str = "INFO"

    model_config = {"env_file": str(_ENV_FILE), "env_file_encoding": "utf-8"}


settings = Settings()
