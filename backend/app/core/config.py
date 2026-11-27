from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration lue depuis les variables d'environnement / le fichier .env."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "ESSIVIVI API"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://essivi:essivi@localhost:5432/essivi"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 15
    otp_expire_minutes: int = 5
    cors_origins: list[str] = []


@lru_cache
def get_settings() -> Settings:
    return Settings()
