from fastapi import APIRouter

from endpoints import utils, idea, user

api_router = APIRouter()
api_router.include_router(idea.router, tags=["Idea"])
api_router.include_router(user.router, tags=["User"])
api_router.include_router(utils.router, prefix="/utils", tags=["Utilities"])
