from pydantic import BaseModel


class IdeaSchema(BaseModel):
    id: int
    type: str
    activity: str
    accessibility: float
    price: float


class IdeaOutputSchema(BaseModel):
    id: int
    type: str
    activity: str
    accessibility: float
    price: float
    user_id: int


class IdeaCreateSchema(BaseModel):
    type: str
    activity: str
    accessibility: float
    price: float
