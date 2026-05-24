from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime


class EmployeeCreate(BaseModel):

    fname: str

    lname: str

    personal_mail: EmailStr

    department: str

    role_id: str

    joining_date: datetime

    salary: float

    status_id: str