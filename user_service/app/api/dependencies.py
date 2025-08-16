from fastapi import Depends
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..repositories.user_repository import UserRepository
from ..services.user_service import UserService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repo():
    return UserRepository()

def get_user_service(repo: UserRepository = Depends(get_user_repo)):
    return UserService(repo)