import os
import pathlib
from typing import Tuple, Type

import tomllib
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource
from pydantic import Field


APP_ROOT_PATH = pathlib.Path(__file__).parent.parent
CFG_TOML_NAME = pathlib.Path('cfg.toml')
CFG_PATH = pathlib.Path(os.getenv('APP_CFG_PATH', APP_ROOT_PATH/CFG_TOML_NAME))

if not CFG_PATH.exists():
    raise FileNotFoundError(f"config_file not found {CFG_PATH.absolute()}")


class AppTomlSettings(BaseSettings):
    class Config:
        extra = 'allow'

    @classmethod
    def settings_customise_sources(
        cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            lambda _: tomllib.loads(CFG_PATH.read_text()),
            file_secret_settings,
        )
