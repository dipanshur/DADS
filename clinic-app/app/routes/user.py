from fastapi import APIRouter, FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, clinic, schemas
from app.database import Sessionlocal

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return clinic.create_user(db, user)