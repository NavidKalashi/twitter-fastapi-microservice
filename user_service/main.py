from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from app.api.endpoints import router as user_router

app = FastAPI(title="Auth Service")
models.Base.metadata.create_all(bind=engine)

app.include_router(user_router)