from configparser import ConfigParser

from cubewise_pulser.config.cw_path import general_config_path

config_ini = ConfigParser()
config_ini.read(general_config_path)
