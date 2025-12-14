from fastapi import FastAPI
from app.database import Base, engine
from app.routers import menu
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Restaurant Menu API")

# Include your routers
app.include_router(menu.router)
