from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from .jwtToken import verify_token
oauth2scheme=OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token:str=Depends(oauth2scheme)):
    credentail_exception=HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detial="You are Unauthorized access",
        headers={"WWW-Authenticate":"Bearer"}
    )
    return verify_token(token,credentail_exception)
