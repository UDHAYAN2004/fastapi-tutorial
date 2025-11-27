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