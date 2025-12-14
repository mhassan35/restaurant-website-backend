from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import menu

app = FastAPI()
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
app.mount("/static", StaticFiles(directory="app/static/images"), name="static")
app.include_router(menu.router)
