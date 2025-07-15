from fastapi import APIRouter, Depends, status

from cubewise.dependencies.access_token import verify_api_key
from cubewise.route.sample.utils import Notepad as _Notepad
from cubewise.schemas.sample import Content, Notepad, content_param

router = APIRouter(prefix='/api/sample', tags=['SAMPLE'], dependencies=[Depends(verify_api_key)])


@router.api_route('/{content}/', methods=['GET'], status_code=status.HTTP_200_OK)
def get(content: Content = content_param):
    return _Notepad.get(content)


@router.api_route('/', methods=['POST'], status_code=status.HTTP_201_CREATED, response_model=str)
def post(body: Notepad):
    _Notepad.create(text=body.text)
    return body.text


@router.api_route('/', methods=['PUT'], status_code=status.HTTP_204_NO_CONTENT)
def put(body: Notepad):
    _Notepad.update(text=body.text)


@router.api_route('/', methods=['DELETE'], status_code=status.HTTP_204_NO_CONTENT)
def delete():
    _Notepad.delete()
