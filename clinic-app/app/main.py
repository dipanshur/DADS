from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user, doctor, appointment

app = FastAPI(title="Clinic App")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(doctor.router)
app.include_router(appointment.router)  

@app.get("/")
def root():
    return {"message": "Clinic API is running"}