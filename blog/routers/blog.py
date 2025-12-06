from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import schemas
from ..repository.blog import BlogRepository
from ..OAuth import get_current_user

router = APIRouter(
    tags=["blogs"],
    dependencies=[Depends(get_current_user)]
                )


@router.post("/blog-create", status_code=status.HTTP_201_CREATED)
def create_blog(blog_list: schemas.blog_list, db: Session = Depends(get_db)):
    blogs = BlogRepository.create_blog(blog_list, db)
    return {
        "message": "Blogs created successfully",
        "data": blogs
    }


@router.get("/get-blogs", response_model=List[schemas.show_blog])
def get_blogs(db: Session = Depends(get_db)):
    return BlogRepository.get_all_blogs(db)


@router.get("/blogs/{id}", response_model=schemas.show_blog)
def get_blog(id: int, db: Session = Depends(get_db)):
    return BlogRepository.get_blog_by_id(id, db)


@router.delete("/blogs-delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    return BlogRepository.delete_blog(id, db)


@router.put("/blog-update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, blog: schemas.blog, db: Session = Depends(get_db)):
    updated_blog = BlogRepository.update_blog(id, blog, db)
    return {
        "message": "Blog updated successfully",
        "updated_blog": updated_blog
    }
