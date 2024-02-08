import os


home_path = os.path.expanduser("~")
CONFIG_FOLDER_PATH = f"{home_path}/.commiter"
INPUT_FIELDS_PATH = f"{CONFIG_FOLDER_PATH}/inputs"
SCOPES_PATH = f"{CONFIG_FOLDER_PATH}/scopes"

inputs_info = {
    "prefix": {"initial_value": "", "description": ""},
    "ticket": {"initial_value": False, "description": ""},
    "type": {"initial_value": True, "description": ""},
    "scope": {"initial_value": True, "description": ""},
    "emoji": {"initial_value": True, "description": ""},
    "message": {"initial_value": True, "description": ""},
    "description": {"initial_value": True, "description": ""},
}
