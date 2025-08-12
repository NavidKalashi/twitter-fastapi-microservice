from fastapi import FastAPI
from app.db.session import engine, Base

app = FastAPI(title="Auth Service")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"msg": "auth service running"}