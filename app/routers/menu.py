from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/menu", tags=["menu"])

@router.get("/", response_model=list[schemas.MenuItem])
def read_menu(db: Session = Depends(get_db)):
    return crud.get_menu_items(db)
