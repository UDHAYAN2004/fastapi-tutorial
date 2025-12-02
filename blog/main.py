from fastapi import FastAPI,Depends,Response,status,HTTPException
from . import schemas,model
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
app=FastAPI()
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

model.Base.metadata.create_all(bind=engine)

def hash_password(password:str):
    return pwd_context.hash(password)

#desing the request body

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#adding new blogs
@app.post('/blog-create',status_code=status.HTTP_201_CREATED)
def blog_create(response:Response,blog_list: schemas.blog_list, db: Session = Depends(get_db)):
    if not blog_list.blogs:
        response=response.status_code=status.HTTP_400_BAD_REQUEST
        return{
            "Response":response,
            "message":"No data is entered"
        }
    db_blogs = [
        model.Blog(
            title=blog.title,
            description=blog.description,
            published=blog.published if blog.published is not None else False
        )
        for blog in blog_list.blogs
    ]
    db.add_all(db_blogs)
    db.commit()
    for blog in db_blogs:
        db.refresh(blog)
    return {
        "message": "Blogs created successfully",
        "data": blog_list
    }
@app.get("/get-blogs", response_model=List[schemas.show_blog])
def get_blogs(db:Session=Depends(get_db)):
    blogs=db.query(model.Blog).all()
    return blogs

@app.get("/blogs/{id}",response_model=schemas.show_blog)
def getby_id(id:int,db:Session=Depends(get_db)):
    blog=db.query(model.Blog).filter(model.Blog.id==id).first()
    if not blog:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail=f"Blog with the id {id} is not available")

    return blog
#delete blog
@app.delete("/blogs-delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session=Depends(get_db) ):
    db.query(model.Blog).filter(model.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return{
        "message":"Blog is Deleted"
    }

#update blog

@app.put('/blog-update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, blog: schemas.blog, db: Session = Depends(get_db)):

    blog_obj = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not blog_obj:
        raise HTTPException(status_code=404, detail="Blog not found")

    blog_obj.title = blog.title
    blog_obj.description = blog.description
    blog_obj.published = blog.published

    db.commit()
    db.refresh(blog_obj)

    return {
        "message": "Blog updated successfully",
        "updated_blog": blog_obj
    }


#creating user

@app.post('/user-create',status_code=status.HTTP_201_CREATED,response_model=schemas.show_user)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    h_password = hash_password(user.password)

    new_user = model.User(
        name=user.name,
        email=user.email,
        password=h_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
