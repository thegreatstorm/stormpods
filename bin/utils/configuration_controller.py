import os
import configparser


def config_controller(script_dir, default, local):

    config = configparser.RawConfigParser()
    prefix_dir = os.path.abspath(os.path.join(script_dir))
    default_config_path = os.path.abspath(os.path.join(prefix_dir, default))
    local_config_path = os.path.abspath(os.path.join(prefix_dir, local))

    config.read(default_config_path)
    if os.path.isfile(local_config_path):
        config.read(local_config_path)

    return config


def get_game_config(prefix_dir, game_name):
    # Game Configuration
    game_config = {}
    game_config_settings = config_controller(prefix_dir, "server/conf/{}.conf".format(game_name), "local.conf")
    for each_section in game_config_settings.sections():
        for (key, value) in game_config_settings.items(each_section):
            game_config[key] = value

    return game_config