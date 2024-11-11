# דוגמה למודל
from sqlalchemy import Column, Integer, String
from config.sql_config import Base, engine

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String)
    price = Column(Integer)


# יצירת הטבלאות בבסיס הנתונים
Base.metadata.create_all(bind=engine)