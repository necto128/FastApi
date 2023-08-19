import os
from typing import Union

import requests
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from models.models import Idea
from schema.idea import IdeaCreateSchema

load_dotenv()


class IdeaServices:
    def __init__(self, db):
        self.__db = db

    def create_group(self, idea: Idea):
        idea_db = idea
        self.__db.add(idea_db)
        self.__db.commit()
        self.__db.refresh(idea_db)
        return idea_db


def generate_idea() -> Union[IdeaCreateSchema, dict]:
    try:
        response = requests.get(os.environ.get('URL_IDEA'))
    except Exception:
        return {"Error": "Source is not exist"}
    return IdeaCreateSchema(**response.json())


def save_idea(user_id: int, db: IdeaServices) -> None:
    db.create_group(
        Idea(
            **generate_idea().model_dump(),
            user_id=user_id)
    )
