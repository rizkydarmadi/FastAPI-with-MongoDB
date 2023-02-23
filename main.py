from fastapi import FastAPI
from pymongo import MongoClient
from routes import router as todos_router

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb://admin:password123@localhost:6000")
    app.database = app.mongodb_client["todo"]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


app.include_router(todos_router, tags=["Todo List"])
