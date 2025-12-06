from ..import(schemas,model)
from fastapi import HTTPException,status

class UserRepository:
    @staticmethod
    def create_user(db, user, hashed_password):
        db_user = model.User(
            name=user.name,
            email=user.email,
            password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    @staticmethod
    def get_user_by_id(db,id):
         user=db.query(model.User).filter(model.User.id==id).first()
         if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
         return user