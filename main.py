from fastapi import FastAPI
from todo import tasks, save_file
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form
from fastapi.responses import RedirectResponse

templates = Jinja2Templates(directory="templates")

app = FastAPI()

class Task(BaseModel):
    name:str


@app.get("/tasks")
def get_tasks() -> list[str]:
    return tasks

@app.post("/tasks")
def add_task(task: Task) -> dict:
    tasks.append(task.name)
    save_file()
    return {"message": "Task added!"}

@app.delete("/tasks/{item_id}")
def delete_item(item_id: int) -> dict:
    if item_id >= 1 and item_id <= len(tasks):
        del tasks[item_id - 1]
        save_file()
    else:
        return {"message" : "Enter a valid number!"}
    return {"message" : "Item deleted"}

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/")
def add_task_form(task: str = Form(...)):
    tasks.append(task)
    save_file()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{item_id}")
def delete_task_form(item_id: int):
    if item_id >= 1 and item_id <= len(tasks):
        del tasks[item_id - 1]
        save_file()
    return RedirectResponse(url="/", status_code=303)