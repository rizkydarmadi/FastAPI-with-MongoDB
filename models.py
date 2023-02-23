import uuid
from pydantic import BaseModel, Field
from datetime import datetime


class TodoModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str
    description: str
    date: str
