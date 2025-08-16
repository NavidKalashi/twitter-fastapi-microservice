from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class UsersCreate(BaseModel):
    email: EmailStr
    username: str
    password: str
    name: Optional[str] = None
    birthday: Optional[datetime] = None

class UserUpdate(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    birthday: Optional[datetime] = None
    password: Optional[str] = None

class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    name: Optional[str]
    birthday: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True