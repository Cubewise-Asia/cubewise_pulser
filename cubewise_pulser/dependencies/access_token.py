from fastapi import Header, HTTPException, status
from cubewise.config import cw_path
from cubewise.utils.constants import API_KEY_HEADER


def verify_api_key(x_api_key: str = Header(None, alias=API_KEY_HEADER)):
    if not x_api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Access token is missing")

    with open(cw_path.access_token_file, 'r') as file:
        token_in_record = file.readline().strip()

    if token_in_record != x_api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid access token")