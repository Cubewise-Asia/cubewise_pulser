import os
from configparser import ConfigParser

from cubewise_pulser.config.cw_path import general_config_path

config_ini = ConfigParser()
assert os.path.exists(general_config_path), 'config path not found : {} '.format(general_config_path)
config_ini.read(general_config_path)
