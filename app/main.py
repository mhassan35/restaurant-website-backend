from fastapi import FastAPI
from app.routers import menu
from app.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant API")

# Include routers
app.include_router(menu.router)
