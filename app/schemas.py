from pydantic import BaseModel

class MenuItemBase(BaseModel):
    id: str
    name: str
    description: str
    price: float
    image: str
    category: str
    rating: float

class MenuItemCreate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    class Config:
        from_attributes = True
