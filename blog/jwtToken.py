from datetime import datetime,timedelta,timezone
from fastapi import status,HTTPException
from typing import Optional
from jose import JWTError,jwt
from .schemas import TokenData

SECRET_KEY="jwtsecretkey1234567890"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30


def create_token(data:dict,secret_key:str=SECRET_KEY,algorithm:str=ALGORITHM):
    to_encode=data.copy()
    expires_delta=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expires_delta})

    jwt_encoder=jwt.encode(to_encode,secret_key,algorithm=algorithm)

    return jwt_encoder

def verify_token(token:str,credential_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str=payload.get("sub")
        if email is None:
            raise credential_exception
        token_data= TokenData(email=email)
    except JWTError:
        raise credential_exception
    return token_data
    