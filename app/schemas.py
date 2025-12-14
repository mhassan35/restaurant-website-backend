from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    image: str | None = None
    category: str | None = None
    rating: float | None = None

class MenuItemCreate(MenuItemBase):
    id: str

class MenuItem(MenuItemBase):
    id: str

    class Config:
        form_mode = True
