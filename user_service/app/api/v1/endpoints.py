from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .dependencies import get_db

router = APIRouter()

@router.get("/items")
async def list_items(db: Session = Depends(get_db)):
    return {"msg": "conncted to db"}