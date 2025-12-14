from sqlalchemy import Column, String, Float, Integer
from app.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image = Column(String)
    category = Column(String, index=True)
    rating = Column(Float)
