from sqlalchemy import Column, String, Float
from app.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    image = Column(String)
    category = Column(String)
    rating = Column(Float)
