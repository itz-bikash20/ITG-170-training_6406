from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.hr_model import HR

from app.schemas.hr_schema import HRCreate
from app.schemas.hr_schema import HRLogin

from app.security.hashing import hash_password
from app.security.hashing import verify_password

from app.security.jwt_handler import create_access_token

router = APIRouter()


# ADD HR
@router.post("/add-hr")
def add_hr(
    hr: HRCreate,
    db: Session = Depends(get_db)
):

    existing_hr = db.query(HR).filter(
        HR.hr_email == hr.hr_email
    ).first()

    if existing_hr:

        raise HTTPException(
            status_code=400,
            detail="HR already exists"
        )

    hashed_password = hash_password(
        hr.hr_password
    )

    new_hr = HR(

        hr_name=hr.hr_name,

        hr_email=hr.hr_email,

        hr_password=hashed_password
    )

    db.add(new_hr)

    db.commit()

    db.refresh(new_hr)

    return {
        "message": "HR Added Successfully"
    }


# LOGIN
@router.post("/login")
def hr_login(

    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)

):

    hr = db.query(HR).filter(
        HR.hr_email == form_data.username
    ).first()

    if not hr:

        raise HTTPException(
            status_code=404,
            detail="HR Not Found"
        )

    password_check = verify_password(
        form_data.password,
        hr.hr_password
    )

    if not password_check:

        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    access_token = create_access_token(
        data={"sub": hr.hr_email}
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"
    }