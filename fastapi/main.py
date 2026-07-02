from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db:5432/{os.environ['POSTGRES_DB']}"

engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "Hello Docker!"}

@app.get("/db-test")
def db_test():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    return {"db": "connected"}