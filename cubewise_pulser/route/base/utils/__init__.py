import json


def configparser_to_json(cw_config):
    config_dict = {}
    for section in cw_config.general.sections():
        config_dict[section] = {}
        for option in cw_config.general.options(section):
            config_dict[section][option] = cw_config.general.get(section, option)
    return config_dict
