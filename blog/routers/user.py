from fastapi import APIRouter,Response,status,HTTPException,Depends
from ..import(schemas,model)
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..repository.user import UserRepository
from ..OAuth import get_current_user

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

router=APIRouter(
)

#creating user

@router.post('/user-create',status_code=status.HTTP_201_CREATED,response_model=schemas.show_user,tags=['user'])
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    h_password = hash_password(user.password)
    return UserRepository.create_user(db,user,h_password)

@router.get('/user/{id}',response_model= schemas.show_user,tags=['user'])
def get_user(id,db:Session=Depends(get_db)):
   return UserRepository.get_user_by_id(db,id)
