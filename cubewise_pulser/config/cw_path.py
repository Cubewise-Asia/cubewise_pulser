import os
import sys

from cubewise.utils.constants import APP_NAME

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    general_config_path = os.path.join(application_path, 'config', 'config.ini')
    logging_config = os.path.join(application_path, 'bin', 'logging_config.ini')
    log_path = os.path.join(application_path, 'bin', APP_NAME + '.log')
    access_token_file = os.path.join(application_path, 'bin', 'access_token.txt')
    sample_file = os.path.join(application_path, 'bin', 'sample.txt')
elif __file__:
    CURRENT_DIRECTORY = os.path.dirname(__file__)
    general_config_path = os.path.join(CURRENT_DIRECTORY, '../..', 'config', 'config.ini')
    logging_config = os.path.join(CURRENT_DIRECTORY, '../..', 'bin', 'logging_config.ini')
    log_path = os.path.join(CURRENT_DIRECTORY, '../..', 'bin', APP_NAME + '.log')
    access_token_file = os.path.join(CURRENT_DIRECTORY, '../..', 'bin', 'access_token.txt')
    sample_file = os.path.join(CURRENT_DIRECTORY, '../..', 'bin', 'sample.txt')
