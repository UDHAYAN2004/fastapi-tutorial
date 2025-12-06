from pydantic import BaseModel,Field
from typing import Optional,List




class blog(BaseModel):
    title:str
    description:str
    published:Optional[bool]
class blog_list(BaseModel):
    blogs:List[blog]



#creating user
class User(BaseModel):
    name:str
    email:str
    password:str=Field(...,max_length=72)

class show_user(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True
class show_blog(BaseModel):
    title:str
    description:str
    published:bool
    createdBy:show_user
   
    class Config():
        orm_mode=True
#orm_mode=True is used to tell Pydantic to read the data even if it is not a dict,


class login_data(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:Optional[str]=None