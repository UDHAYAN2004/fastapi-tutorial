from fastapi import HTTPException,status
from ..import model
from ..routers.user import verify_password
from ..jwtToken import create_token


class LoginAuthenticate:
    @staticmethod
    def login (login_data,db):
       user=db.query(model.User).filter(login_data.email==model.User.email).first()
       
       if not user:
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not Found")
       if not verify_password(login_data.password,user.password):
           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect Password")
       access_token=create_token(data={"sub":user.email})
       return {"access_token":access_token,
               "token_type":"bearer"}
       