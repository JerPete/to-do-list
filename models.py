from sqlmodel import Field, SQLModel
from datetime import datetime

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user: str | None = Field(default=None)
    title: str 
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory= datetime.now)
    