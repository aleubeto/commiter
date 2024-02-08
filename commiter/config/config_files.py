import os

from commiter.config.env_vars import (
    CONFIG_FOLDER_PATH,
    inputs_info,
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
    for key, input_data in inputs_info.items():
        command = f"echo {key}={input_data.get('initial_value')} >> {INPUT_FIELDS_PATH}"
        os.system(command)


def create_scopes_file() -> None:
    """"""
    with open(SCOPES_PATH, "a"):
        pass


def read_config_file(path: str) -> str:
    """"""
    with open(path, "r") as file_content:
        configfile_content = file_content.read()
    return configfile_content.rstrip("\n")
