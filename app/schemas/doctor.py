from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name : str
    gender : str
    specialization : str
    qualification : str
    phone : str
    experience : str

class DoctorResponse(BaseModel):
    id : int
    name : str
    gender : str
    specialization : str
    qualification : str
    phone : str
    experience : str

    class Config:
        from_attributes = True