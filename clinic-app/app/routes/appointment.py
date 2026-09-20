from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app import models, clinic, schemas
from app.database import Sessionlocal

router = APIRouter(prefix="/appointments", tags=["appointments"])

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return clinic.create_appointment(db, appointment) 

@router.get("/")
def get_appointments(db: Session = Depends(get_db)):
    return clinic.get_appointments(db)