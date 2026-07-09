from pydantic import BaseModel

class StaffCreate(BaseModel):
    name : str
    gender : str
    designation : str
    department : str
    phone : str
    salary : int

class StaffResponse(BaseModel):
    id : int
    name : str
    gender : str
    designation : str
    department : str
    phone : str
    salary : int

    class Config:
        from_attributes = True