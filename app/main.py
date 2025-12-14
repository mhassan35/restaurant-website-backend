from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from app.routers import menu  # your router

app = FastAPI()

# Mount the static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include your router
app.include_router(menu.router)
