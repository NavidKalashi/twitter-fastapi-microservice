from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..repositories.user_repository import UserRepository
from ..schema.pydantic_schema import UsersCreate, UserUpdate
from ..db.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def create_user(self, db: Session, user_create: UsersCreate) -> User:
        hashed_password = self.hash_password(user_create.password)
        user = User(
            email=user_create.email,
            username=user_create.username,
            hashed_password=hashed_password,
            name=user_create.name,
            birthday=user_create.birthday
        )
        return self.repo.create_user(db, user)
    
    def update_user(self, db: Session, user: User, user_update: UserUpdate) -> User:
        if user_update.password:
            user.hashed_password = self.hash_password(user_update.password)
        if user_update.username:
            user.username = user_update.username
        if user_update.name:
            user.name = user_update.name
        if user_update.birthday:
            user.birthday = user_update.birthday
        return self.repo.update_user(db, user)