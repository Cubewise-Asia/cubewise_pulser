import os
import time
import logging
from pathlib import Path
from jose import jwt, JWTError

SECRET_KEY = os.getenv("SECRET_KEY", "cubewise_verify")
ALGORITHM = "HS256"


def create_access_token(access_token_file: str):
    """
    Creates an access token and saves it to the specified file if it doesn't already exist.
    """
    access_token_path = Path(access_token_file)

    if access_token_path.exists():
        return

    try:
        data = {"id": int(time.time())}
        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        access_token_path.write_text(encoded_jwt)
    except JWTError as e:
        logging.error(f"Error encoding JWT: {e}")
    except OSError as e:
        logging.error(f"Error writing to file {access_token_file}: {e}")
