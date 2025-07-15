import logging
import os
from configparser import NoSectionError
from logging.config import fileConfig

import uvicorn
from cubewise_pulser.config import cw_path
from cubewise_pulser.config.access_token import create_access_token
from cubewise_pulser.config.logging import generate_logging_config
from cubewise_pulser.utils.constants import Default
from cubewise_pulser.web_server import create_app

IS_DEV = os.environ.get('ENV') == 'development'
generate_logging_config(cw_path.logging_config, cw_path.log_path)
fileConfig(cw_path.logging_config)
create_access_token(cw_path.access_token_file)
app = create_app(debug=IS_DEV)


def main():
    try:
        try:
            port = app.cw_config.general.getint("server", "port")
        except NoSectionError:
            port = Default.port
        try:
            workers = app.cw_config.general.getint("server", "threads")
        except NoSectionError:
            workers = Default.threads
        if IS_DEV:
            uvicorn.run("run:app", host="0.0.0.0", port=port, reload=True)
        else:
            qw = uvicorn.Config(app=app, host="0.0.0.0", port=port, reload=False, log_config=None, workers=workers)
            server = uvicorn.Server(qw)
            server.install_signal_handlers = lambda: None
            server.run()
    except (Exception, SystemExit) as e:
        logging.exception(str(e))


if __name__ == '__main__':
    main()
