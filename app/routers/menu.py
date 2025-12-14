from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter(prefix="/menu", tags=["menu"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.MenuItem])
def read_menu(db: Session = Depends(get_db)):
    return crud.get_menu(db)

@router.get("/{item_id}", response_model=schemas.MenuItem)
def read_menu_item(item_id: str, db: Session = Depends(get_db)):
    return crud.get_menu_by_id(db, item_id)

@router.get("/category/{category}", response_model=list[schemas.MenuItem])
def read_menu_by_category(category: str, db: Session = Depends(get_db)):
    return crud.get_menu_by_category(db, category)
