from .base import AppTomlSettings
from .api import ApiSettings
# from .database import DatabaseSettings
from .logging import LoggingSettings


class AppSettings(AppTomlSettings):
    api: ApiSettings
    # databases: DatabaseSettings
    logging: LoggingSettings


APP_CFG = AppSettings()
