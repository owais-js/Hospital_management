from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate

def create_doctor(db:Session,doctor:DoctorCreate):
    db_doctor = Doctor(
        name = doctor.name,
        gender = doctor.gender,
        specialization = doctor.specialization,
        qualification = doctor.qualification,
        phone = doctor.phone,
        experience = doctor.experience
    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor

