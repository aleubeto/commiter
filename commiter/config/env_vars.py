import os

from commiter.config.fields_data.gitmojis import gitmojis_options
from commiter.config.fields_data.types import commit_types_options


home_path = os.path.expanduser("~")
CONFIG_FOLDER_PATH = f"{home_path}/.commiter"
FIELDS_STATUS_PATH = f"{CONFIG_FOLDER_PATH}/fields"
SCOPES_PATH = f"{CONFIG_FOLDER_PATH}/scopes"
PREFIXES_PATH = f"{CONFIG_FOLDER_PATH}/prefixes"

input_fields_info = {
    "prefix": {
        "initial_status": False,
        "description": "",
        "optional": True,
    },
    "ticket": {
        "initial_status": False,
        "description": "Specify the ticket/issue related to this commit",
    },
    "type": {
        "initial_status": True,
        "description": "Select the type of change you are committing",
        "optional": False,
        "options": commit_types_options,
    },
    "scope": {
        "initial_status": True,
        "description": "Select the scope of this change",
        "optional": True,
    },
    "gitmoji": {
        "initial_status": True,
        "description": "Choose a gitmoji",
        "optional": True,
        "options": gitmojis_options,
    },
    "message": {
        "initial_status": True,
        "description": "Write a short imperative tense description of the change",
    },
    "description": {
        "initial_status": True,
        "description": "Provide a longer description of the change",
    },
}
