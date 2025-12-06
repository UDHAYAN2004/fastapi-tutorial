from fastapi import APIRouter,status,Depends
from ..import(schemas,database)
from sqlalchemy.orm import Session
from .. import schemas
from ..repository.authenticate import LoginAuthenticate
from ..OAuth import get_current_user

router=APIRouter(tags=['Authentication'])

@router.post('/login',status_code=status.HTTP_200_OK,response_model=schemas.Token)
def login(data:schemas.login_data,db:Session=Depends(database.get_db)):
    return LoginAuthenticate.login(data,db)