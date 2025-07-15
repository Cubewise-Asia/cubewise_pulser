from enum import Enum

from fastapi import Path
from pydantic import BaseModel

content_param: str = Path(..., description="The content to use, either 'text' or 'subject'")


class Content(str, Enum):
    text = 'text'
    subject = 'subject'


class Notepad(BaseModel):
    text: str
