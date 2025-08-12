from sqlalchemy.orm import Session
from collections.abc import Generator
from db.session import SessionLocal

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()