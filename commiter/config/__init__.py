from commiter.config.config_files import (
    config_file_exists,
    create_config_directory,
    create_config_file,
    insert_initial_fields_values,
)
from commiter.config.env_vars import (
    CONFIG_FOLDER_PATH,
    FIELDS_STATUS_PATH,
    SCOPES_PATH,
    PREFIXES_PATH,
)


fields_path = FIELDS_STATUS_PATH
scopes_path = SCOPES_PATH
prefixes_path = PREFIXES_PATH


if not config_file_exists(CONFIG_FOLDER_PATH):
    create_config_directory()


if not config_file_exists(fields_path):
    create_config_file(fields_path)
    insert_initial_fields_values(fields_path)


if not config_file_exists(scopes_path):
    create_config_file(scopes_path)


if not config_file_exists(prefixes_path):
    create_config_file(prefixes_path)
