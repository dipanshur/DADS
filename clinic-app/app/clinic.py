## Business Logic

from sqlalchemy.orm import Session
from app import models

## create a user
def create_user(db: Session, user):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

## Create a doctor

def create_doctor(db: Session, doctor):
    db_doc = models.Doctor(name=doctor.name, specialization=doctor.specialization)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)

    return db_doc

def get_doctors(db: Session):
    return db.query(models.Doctor).all()

def get_doctor_by_specialization(db: Session):
    doctors = db.query(models.Doctors).all()

    results = []
    for doctor in doctors:
        if doctor.specialization == specialization:
            results.append(doctor)

    return results

def create_appointment(db: Session, appointment):
    if appointment.user_id <=0:
        return {"error": "Invalid User_id"}
    
    db_app = models.Appointment(**appointment.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)

    return db_app

def get_appointments(db: Session):
    return db.query(models.Appointment).all()



