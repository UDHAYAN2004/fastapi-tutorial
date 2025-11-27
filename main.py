from fastapi import FastAPI

app=FastAPI()

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