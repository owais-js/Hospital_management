from sqlalchemy.orm import Session

from app.models.staff import Staff
from app.schemas.staff import StaffCreate

def create_staff(db:Session,staff:StaffCreate):
    db_staff = Staff(
        name = staff.name,
        gender = staff.gender,
        designation = staff.designation,
        department = staff.department,
        phone = staff.phone,
        salary = staff.salary
    )
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)

    return db_staff