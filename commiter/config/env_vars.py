import os


home_path = os.path.expanduser("~")
CONFIG_FOLDER_PATH = f"{home_path}/.commiter"
INPUT_FIELDS_PATH = f"{CONFIG_FOLDER_PATH}/inputs"
SCOPES_PATH = f"{CONFIG_FOLDER_PATH}/scopes"

initial_inputs_status = {
    "prefix": {"description": "", "value": ""},
    "ticket": {"description": "", "value": False},
    "type": {"description": "", "value": True},
    "scope": {"description": "", "value": True},
    "emoji": {"description": "", "value": True},
    "message": {"description": "", "value": True},
    "description": {"description": "", "value": True},
}
