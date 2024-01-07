from typing import Optional

from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class PostgresSettings(BaseModel):
    user: str = 'postgres'
    password: str = 'password'
    db: str = 'fastapi_shop'
    host: str = 'localhost'
    port: str = 5432
    url: str = 'postgresql://postgres:password@localhost/fastapi_shop'

# postgresql+asyncpg://postgres:password@localhost:5432/fastapi_shop
class ProjectSettings(BaseSettings):
    api_key: Optional[str] = None
    debug: Optional[bool] = True
    api_logger_format: Optional[str] = '%(levelname)s: %(asctime)s - %(message)s'

    postgres: PostgresSettings = PostgresSettings()

    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        frozen=True,
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


base_settings = ProjectSettings()
