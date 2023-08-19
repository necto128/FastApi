import os

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from services.idea_service import IdeaServices

load_dotenv()

engine = create_engine(os.environ.get('SQLALCHEMY_DATABASE_URI'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_depends() -> Depends:
    return Depends(get_db)


def get_idea_service(db: Session = Depends(get_db)) -> IdeaServices:
    return IdeaServices(db=db)
