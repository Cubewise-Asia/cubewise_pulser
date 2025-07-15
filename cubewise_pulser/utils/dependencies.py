from fastapi import Request
from cubewise.config import cw_config


def get_cw_config(request: Request) -> cw_config:
    return request.app.cw_config
