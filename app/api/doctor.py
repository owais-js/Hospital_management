from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.doctor import(
    DoctorCreate,
    DoctorResponse
)

from app.crud.doctor import(
    create_doctor,
    get_doctor,
    get_doctors,
    update_doctor,
    delete_doctor
)

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/",response_model=DoctorResponse)
def create(
    doctor : DoctorCreate,
    db : Session = Depends(get_db)
):
    return create_doctor(db,doctor)


@router.get("/",response_model=list[DoctorResponse])
def read_all(
    db: Session = Depends(get_db)
):
    return get_doctors(db)


@router.get("/{doctor_id}",response_model=DoctorResponse)
def read_one(
    doctor_id : int,
    db: Session = Depends(get_db)
):
    doctor = get_doctor(db,doctor_id)

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )
    return doctor
