import os

from fastapi import HTTPException

from cubewise.config.cw_path import sample_file
from cubewise.schemas.sample import Content


def is_file_existing():
    if not os.path.exists(sample_file):
        raise HTTPException(status_code=404, detail=f"File '{sample_file}' not found")


class Notepad:

    @staticmethod
    def create(text: str):
        with open(sample_file, "w") as file:
            file.write(text)

    @staticmethod
    def update(text: str):
        is_file_existing()
        with open(sample_file, "a") as file:
            file.write(text)

    @staticmethod
    def get(content: str):
        is_file_existing()
        if content == Content.subject:
            return os.path.basename(sample_file)
        with open(sample_file, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    @staticmethod
    def delete():
        is_file_existing()
        os.remove(sample_file)
