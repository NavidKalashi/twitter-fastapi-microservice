from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from ..schema.pydantic_schema import UserOut, UsersCreate, UserUpdate
from ..api.dependencies import get_db, get_user_service
from ..services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UsersCreate, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    db_user = service.repo.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db, user)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: UUID, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    user = service.repo.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: UUID, user_update: UserUpdate, db: Session = Depends(get_db), service: UserService = Depends(get_user_service)):
    user = service.repo.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return service.update_user(db, user, user_update)