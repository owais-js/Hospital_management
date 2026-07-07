from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.patient import (
    PatientCreate,
    PatientResponse
)

from app.crud.patient import (
    create_patient,
    get_patients,
    get_patient,
    update_patient,
    delete_patient
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/", response_model=PatientResponse)
def create(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    return create_patient(db, patient)


