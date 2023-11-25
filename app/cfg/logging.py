from enum import StrEnum

from pydantic_settings import BaseSettings


class LogLevels(StrEnum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"


class LoggingSettings(BaseSettings):
    level: LogLevels = LogLevels.INFO
    color_system: str = 'standard'
    width: int = 160
    rich_tracebacks: bool = False
    traceback_show_locals: bool = False
