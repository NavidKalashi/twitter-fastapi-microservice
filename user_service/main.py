from fastapi import FastAPI
from app.db import models
from app.db.database import engine

app = FastAPI(title="Auth Service")
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "auth service running"}
