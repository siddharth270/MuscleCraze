"""Settings loaded from environment (pydantic-settings): DB URL, Supabase keys, Ollama host, etc."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "MuscleCraze API"
    version: str = "0.1.0"
    environment: str = "local"


settings = Settings()
