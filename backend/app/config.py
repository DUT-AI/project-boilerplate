from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

API_DIR = Path(__file__).resolve().parent
ROOT_DIR = API_DIR.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Database
    database_url: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/boilerplate_db"
    )

    # Security & JWT
    jwt_secret_key: str = "change-this-to-a-very-secure-secret-key-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 1440

    # Server configs
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: str = "http://localhost:3000"

    # S3 / MinIO Storage
    s3_endpoint: str = ""
    s3_secure: bool = False
    s3_access_key: str = ""
    s3_secret_key: str = ""
    s3_bucket_name: str = "boilerplate-uploads"

    @property
    def cors_origin_list(self) -> list[str]:
        """Parses comma-separated CORS origins into a list of strings."""
        return [
            origin.strip() for origin in self.cors_origins.split(",") if origin.strip()
        ]


settings = Settings()
