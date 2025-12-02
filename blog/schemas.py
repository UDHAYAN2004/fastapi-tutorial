from pydantic import BaseModel,Field
from typing import Optional,List

class blog(BaseModel):
    title:str
    description:str
    published:Optional[bool]
class blog_list(BaseModel):
    blogs:List[blog]

class show_blog(blog):
    class Config():
        orm_mode=True
#orm_mode=True is used to tell Pydantic to read the data even if it is not a dict,


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