from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from database import create_tables, engine
from sqlmodel import Session, select
from models import Task


create_tables()

templates = Jinja2Templates(directory="templates")

app = FastAPI()

def get_db():
    with Session(engine) as session:
        yield session

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.exec(select(Task)).all()
    return tasks

@app.post("/tasks")
def add_task(task: Task, db: Session = Depends(get_db)):
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    return {"message": "Task added!"}

@app.delete("/tasks/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    task = db.get(Task, id)
    if not task:
        return {"message" : "Enter a valid number!"}  
    db.delete(task)
    db.commit()
    return {"message" : "Item deleted"}

@app.get("/")
def home(request: Request, db: Session= Depends(get_db)):
    tasks = db.exec(select(Task)).all()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/")
def add_task_form(task: str = Form(...), db: Session= Depends(get_db)):
    db_task = Task(title=task)
    db.add(db_task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete/{id}")
def delete_task_form(id: int, db: Session= Depends(get_db)):
    task = db.get(Task, id)
    if not task:
        return
    db.delete(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)