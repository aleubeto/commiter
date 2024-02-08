import os
from typing import Dict

from commiter.config.env_vars import (
    CONFIG_FOLDER_PATH,
    FIELDS_STATUS_PATH,
    input_fields_info,
)


def config_file_exists(path: str) -> bool:
    """Check if a given configuration file already exists."""
    return os.path.exists(path)


def create_config_directory() -> None:
    """"""
    os.makedirs(CONFIG_FOLDER_PATH)


def create_config_file(path: str) -> None:
    """"""
    with open(path, "a"):
        pass


def insert_fields_values(path: str, inputs_status: Dict) -> None:
    """"""
    for field, status in inputs_status.items():
        command = f"echo {field}={status} >> {path}"
        os.system(command)


def insert_initial_fields_values(path: str) -> None:
    """"""
    initial_field_status = {
        field: info["initial_status"] for field, info in input_fields_info.items()
    }
    insert_fields_values(path=path, inputs_status=initial_field_status)


def read_config_file(path: str) -> str:
    """"""
    with open(path, "r") as file_content:
        configfile_content = file_content.read()
    return configfile_content.rstrip("\n")


def get_current_fields_status() -> Dict:
    """Retrieve configuration variables from a given configuration file."""
    inputs_status = {}
    with open(FIELDS_STATUS_PATH, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            inputs_status[key] = value
    return inputs_status
