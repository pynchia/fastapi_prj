from pydantic_settings import BaseSettings
from pydantic import Field


class ApiSettings(BaseSettings):
    secret_key: str = Field(..., env="API_SECRET_KEY")
    version: str = Field("unknown", env="API_VERSION")
