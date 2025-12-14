from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import menu 

app = FastAPI(title="Restaurant Backend")

origins = [
    "http://localhost:3000",
    "https://restaurant-website-delta-neon.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# Mount the static folder to serve images
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include the menu router
app.include_router(menu.router, prefix="/menu", tags=["menu"])
