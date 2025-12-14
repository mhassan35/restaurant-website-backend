from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: str
    price: float
    image: str
    category: str
    rating: float

class MenuItemCreate(MenuItemBase):
    id: str

class MenuItemResponse(MenuItemCreate):
    class Config:
        from_attributes = True
