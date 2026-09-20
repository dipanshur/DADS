## Validation Layer using Pydantic
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str


class DoctorCreate(BaseModel):
    name: str
    specialization: str

class AppointmentCreate(BaseModel):
    user_id: int
    doctor_id: int
    date: str