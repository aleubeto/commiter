from commiter.config.config_files import (
    config_file_exists,
    create_config_directory,
    create_inputs_file,
    create_scopes_file,
)
from commiter.config.env_vars import CONFIG_FOLDER_PATH, INPUT_FIELDS_PATH, SCOPES_PATH


if not config_file_exists(CONFIG_FOLDER_PATH):
    create_config_directory()


if not config_file_exists(INPUT_FIELDS_PATH):
    create_inputs_file()


if not config_file_exists(SCOPES_PATH):
    create_scopes_file()
