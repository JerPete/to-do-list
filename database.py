from sqlmodel import create_engine, SQLModel
from models import Task  # noqa: F401

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL)

def create_tables():
    SQLModel.metadata.create_all(engine)