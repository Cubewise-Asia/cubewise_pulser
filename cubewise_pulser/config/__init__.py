import configparser

from cubewise_pulser.config import cw_path


class cw_config():

    def __init__(self, general_config) -> None:
        self.general = general_config

    def reload_general(self):
        self.general = configparser.ConfigParser()
        self.general.read(cw_path.general_config_path)


def init_config() -> cw_config:
    assert cw_path.general_config_path, 'config path is not found at {}'.format(cw_path.general_config_path)
    general_config = configparser.ConfigParser()
    general_config.read(cw_path.general_config_path)

    return cw_config(general_config)
