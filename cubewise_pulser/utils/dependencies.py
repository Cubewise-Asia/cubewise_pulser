from cubewise_pulser.config import cw_config
from fastapi import Request


def get_cw_config(request: Request) -> cw_config:
    return request.app.cw_config
