import os

from commiter.config.config_files import (
    create_config_file,
    config_file_exists,
    get_current_fields_status,
    insert_initial_fields_values,
    read_config_file,
)
from commiter.config.env_vars import FIELDS_STATUS_PATH, input_fields_info


def print_input_fields_file() -> None:
    """"""
    print(read_config_file(FIELDS_STATUS_PATH))


def config_input_fields_file() -> None:
    """"""
    current_fields_status = get_current_fields_status()
    for field, field_info in input_fields_info.items():
        default_value = current_fields_status.get(field)
        field_description = field_info.get("description")
        print(f"{field} (default: {default_value})")
        print(f"description: {field_description}")


def reset_input_fields_file() -> None:
    """"""
    fields_file = FIELDS_STATUS_PATH
    if config_file_exists(fields_file):
        os.remove(fields_file)
    create_config_file(fields_file)
    insert_initial_fields_values(fields_file)


def config_command(list_option: bool, reset_option: bool) -> None:
    """"""
    if list_option:
        print_input_fields_file()
    elif reset_option:
        reset_input_fields_file()
    else:
        config_input_fields_file()
