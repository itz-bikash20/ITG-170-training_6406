from pydantic import BaseModel
from pydantic import EmailStr


class HRCreate(BaseModel):

    hr_name: str

    hr_email: EmailStr

    hr_password: str


class HRLogin(BaseModel):

    hr_email: EmailStr

    hr_password: str