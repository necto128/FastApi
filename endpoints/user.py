from typing import List

from fastapi import APIRouter
from sqlalchemy.orm import Session

from dependencies.dependencies import get_depends
from models.models import User
from schema.user import UserOutputSchema

router = APIRouter()


@router.get("/users", response_model=List[UserOutputSchema])
def show_users(db: Session = get_depends()):
    return db.query(User).all()
