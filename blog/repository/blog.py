from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import model, schemas


class BlogRepository:

    @staticmethod
    def create_blog(blog_list: schemas.blog_list, db: Session):
        db_blogs = [
            model.Blog(
                title=blog.title,
                description=blog.description,
                published=blog.published if blog.published is not None else False,
                user_id=1
            )
            for blog in blog_list.blogs
        ]
        db.add_all(db_blogs)
        db.commit()

        for blog in db_blogs:
            db.refresh(blog)

        return db_blogs

    @staticmethod
    def get_all_blogs(db: Session):
        return db.query(model.Blog).all()

    @staticmethod
    def get_blog_by_id(id: int, db: Session):
        blog = db.query(model.Blog).filter(model.Blog.id == id).first()
        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id {id} not found"
            )
        return blog

    @staticmethod
    def delete_blog(id: int, db: Session):
        blog = db.query(model.Blog).filter(model.Blog.id == id)
        if not blog.first():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Blog with id {id} not found"
            )

        blog.delete(synchronize_session=False)
        db.commit()
        return {"message": "Blog deleted successfully"}

    @staticmethod
    def update_blog(id: int, blog: schemas.blog, db: Session):
        blog_obj = db.query(model.Blog).filter(model.Blog.id == id).first()

        if not blog_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Blog not found"
            )

        blog_obj.title = blog.title
        blog_obj.description = blog.description
        blog_obj.published = blog.published

        db.commit()
        db.refresh(blog_obj)

        return blog_obj
