from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings using pydantic to load from environment variables."""
    
    # App settings
    app_name: str = "sentiment-analyzer"
    app_version: str = "0.1.0"
    environment: str = "development"
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "info"
    
    # Optional Redis cache - not used in basic implementation but follows 12-Factor App
    # for future extensibility
    redis_host: Optional[str] = None
    redis_port: Optional[int] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()