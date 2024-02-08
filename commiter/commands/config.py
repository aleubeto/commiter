def print_config_list():
    """"""
    print("Configuration list")


def config_command(list_option: bool) -> None:
    """"""
    if list_option:
        print_config_list()
    else:
        print("Config command")
    
