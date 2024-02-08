from commiter.config.config_files import read_config_file
from commiter.config.env_vars import INPUT_FIELDS_PATH


def print_config_list() -> None:
    """"""
    print(read_config_file(INPUT_FIELDS_PATH))


def config_command(list_option: bool) -> None:
    """"""
    if list_option:
        print_config_list()
    else:
        print("Config command")
