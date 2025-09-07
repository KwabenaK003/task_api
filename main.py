from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from bson.objectid import ObjectId

app = FastAPI()

class AddTask(BaseModel):
    task_id: int
    title: str
    description: str

class UpdateTask(BaseModel):
    task_id: int
    title: str
    description: str


tasks = []

@app.get("/")
def get_home():
    return {"message" : "Welcome to my TO-DO manager."}


@app.post("/tasks")
def add_task(task:AddTask):
    task = tasks.append(task)
    return tasks


@app.get("/tasks", summary="Get all tasks")
def get_all_tasks():
    return tasks


@app.get("/tasks/{task_id}", summary="Get task by ID")
def get_task(task_id: int):
    for task in tasks:
        return task
    return {"error": "Task not found"}


@app.put("/tasks/{task_id}", summary="Update a user's task")
def update_task(task:UpdateTask):
    for task in tasks:
        new_task = tasks.pop(task)
        return new_task
    return {"error": "Task not found"}


@app.delete("/tasks/{task_id}", summary="Delete a user's task", status_code=204)
def delete_task(task_id: int):
    for task in tasks:
        tasks.remove(task)
        return {"message": "Task deleted successfully"}
    return {"message": "Task not found"}

