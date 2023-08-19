from typing import List

from fastapi import APIRouter, Request, status
from fastapi import Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from dependencies.dependencies import get_idea_service, get_depends
from models.models import Idea
from schema.idea import IdeaOutputSchema
from services.idea_service import IdeaServices, save_idea

router = APIRouter()


@router.put("/users/{id_user}/create")
def create_idea(id_user: int, request: Request,
                idea_services: IdeaServices = Depends(get_idea_service)) -> RedirectResponse:
    save_idea(user_id=id_user, db=idea_services)
    return RedirectResponse(
        request.url_for("get_idea_by_user", id_user=id_user),
        status_code=status.HTTP_200_OK)


@router.get("/users/{id_user}/ideas", response_model=List[IdeaOutputSchema])
def get_idea_by_user(id_user: int, db: Session = get_depends()):
    return db.query(Idea).filter_by(user_id=id_user).all()
