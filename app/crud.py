from sqlalchemy.orm import Session
from app import models, schemas

def get_menu_items(db: Session):
    return db.query(models.MenuItem).all()

def get_menu_by_category(db: Session, category: str):
    return db.query(models.MenuItem).filter(models.MenuItem.category == category).all()

def create_menu_item(db: Session, item: schemas.MenuItemCreate):
    db_item = models.MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
