from fastapi import FastAPI
from app.database import Base, engine
from app.routers.menu import router as menu_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant API")

app.include_router(menu_router)

@app.get("/")
def root():
    return {"status": "API is running"}
