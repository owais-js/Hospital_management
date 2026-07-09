from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends,APIRouter

from app.core.database import get_db

from app.crud.staff import(
    create_staff
)

from app.schemas.staff import(
    StaffCreate,
    StaffResponse
)

router = APIRouter(
    prefix="/staff",
    tags=["Staff"]
)

@router.post("/",response_model=StaffResponse)
def create(
    staff : StaffCreate,
    db : Session = Depends(get_db)
):
    return create_staff(db,staff)