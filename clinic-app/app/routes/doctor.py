from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, clinic, schemas
from app.database import Sessionlocal

router = APIRouter(prefix="/doctors", tags=["doctors"])

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return clinic.create_doctor(db, doctor)

