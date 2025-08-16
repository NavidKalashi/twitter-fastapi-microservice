from sqlalchemy.orm import Session
from uuid import UUID
from ..db.models import User

class UserRepository:

    def get_user_by_id(self, db: Session, user_id: UUID):
        return db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
    
    def create_user(self, db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def update_user(self, db: Session, user: User):
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user: User):
        db.delete(user)
        db.commit()