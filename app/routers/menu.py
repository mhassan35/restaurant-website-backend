from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.MenuItemResponse])
def get_menu(db: Session = Depends(get_db)):
    return crud.get_menu_items(db)
