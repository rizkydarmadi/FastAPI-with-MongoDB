from fastapi import APIRouter, Request, Body
from models import TodoModel
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()


@router.post("/", response_description="create a todo list", response_model=TodoModel)
def create(request: Request, list: TodoModel = Body(...)):
    list = jsonable_encoder(list)
    new_list = request.app.database["todos"].insert_one(list)
    created_list = request.app.database["todos"].find_one({"_id": new_list.inserted_id})

    return created_list


@router.get(
    "/", response_description="list all the todos", response_model=List[TodoModel]
)
def show_list(request: Request):
    todos = list(request.app.database["todos"].find(limit=50))
    return todos
