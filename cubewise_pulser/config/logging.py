import os


def generate_logging_config(config_file, log_file):
    if os.path.isfile(config_file):
        return
    template = \
        """
[loggers]
keys=root

[handlers]
keys=stream_handler, file_handler

[formatters]
keys=formatter

[logger_root]
level=DEBUG
handlers=stream_handler, file_handler

[handler_stream_handler]
class=StreamHandler
level=ERROR
formatter=formatter
args=(sys.stderr,)

[handler_file_handler]
class=handlers.RotatingFileHandler
level=INFO
formatter=formatter
args=(r'{}', 'a', 5*1024*1024, 10, 'utf-8')

[formatter_formatter]
format=%(asctime)s - Cubewise - %(levelname)s - %(message)s
        """

    with open(config_file, 'w', encoding="utf8") as file:
        file.write(template.format(log_file))
