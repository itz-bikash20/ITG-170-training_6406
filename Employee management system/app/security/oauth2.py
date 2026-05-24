from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from jose import jwt
from jose import JWTError

from dotenv import load_dotenv

import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/hr/login"
)


def verify_token(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        hr_email = payload.get("sub")

        if hr_email is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return hr_email

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token Expired or Invalid"
        )