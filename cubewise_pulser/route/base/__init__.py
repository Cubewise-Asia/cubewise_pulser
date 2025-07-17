from cubewise_pulser.dependencies.access_token import verify_api_key
from cubewise_pulser.route.base.utils import configparser_to_json
from cubewise_pulser.utils.dependencies import get_cw_config
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix='/api/function', tags=['BASE'], dependencies=[Depends(verify_api_key)])


@router.api_route('/get_config/', methods=['GET'], status_code=status.HTTP_200_OK)
def get_config(cw_config: dict = Depends(get_cw_config)):
    return configparser_to_json(cw_config=cw_config)
