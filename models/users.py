from sqlalchemy import Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from config.sql_config import Base, SessionLocal


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)


def check_if_email_exsist(db ,email):
    user = db.query(User).filter(User.email == email).first()
    return user


def insert_user(db, data: dict):
    try:
        email = data.get('email')
        # בדיקה אם המשתמש קיים
        if check_if_email_exsist(db, email):
            return {'error': f'email: {email} already exists'}

        # יצירת משתמש חדש
        new_user = User(**data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {'success': 'User created', 'user_id': new_user.id}
    except SQLAlchemyError as e:
        db.rollback()
        return {"error": str(e)}