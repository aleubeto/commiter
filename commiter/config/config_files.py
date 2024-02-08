import os

from commiter.config.env_vars import (
    CONFIG_FOLDER_PATH,
    initial_inputs_status,
    INPUT_FIELDS_PATH,
    SCOPES_PATH,
)


def config_file_exists(path: str) -> bool:
    """Check if a given configuration file already exists."""
    return os.path.exists(path)


def create_config_directory() -> None:
    """"""
    os.makedirs(CONFIG_FOLDER_PATH)


def create_inputs_file() -> None:
    """"""
    with open(INPUT_FIELDS_PATH, "a"):
        pass


def create_scopes_file() -> None:
    """"""
    with open(SCOPES_PATH, "a"):
        pass


def read_config_file(path: str) -> str:
    """"""
    with open(path, "r") as file_content:
        configfile_content = file_content.read()
    return configfile_content.rstrip("\n")
