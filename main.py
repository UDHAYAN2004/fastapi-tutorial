from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
app=FastAPI()

#design the request body
class Blog(BaseModel):
    title:str
    description:str
    published:Optional[bool]

#adding blog
@app.post("/blog-create")
def create_blog(request:Blog):
    
    return {
        "message":"Blog is created",
        "data":request
    }

@app.get("/")
def index():
    return {"data":{
        "name":"FastAPI Application",
    }}

@app.get("/about")
def about():
    return {"data":{
        "About":"This is a sample FastAPI application."
    }}

#dynamic route
@app.get("/blog/{id}")
def blog(id:str):
    return {"Blog ID":int(id)}

#query parameters

@app.get("/blog")
# if pass a value as an argument it will give the output otherwise it will shows the error
def blog_list(limit=0,published:bool =True):
    if published:
        return {"data":f"{limit} published blogs from the database"}
    else:
        return {"data":f"{limit} blogs from the database"}

@app.get("blog/unpublished")
def unpublished():
    return {"data":"All unpublished blogs"}

#changing ports
if __name__=="__main__":
  uvicorn.run(app,port='9000')