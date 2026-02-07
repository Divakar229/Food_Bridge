from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.models.model import Base
from backend.app.api.database import engine
from backend.app.routes.user import router as user_router
from backend.app.routes.food import router as food_router
from backend.app.utils.logger import setup_logging   # ✅ Correct import

setup_logging()   # ✅ Now works


PRODUCTION=False
app=FastAPI(
    docs_url=None if PRODUCTION else "/docs",
    redoc_url=None if PRODUCTION else "/redocs",
    openapi_url=None if PRODUCTION else "/openapi.json.", 
)
# Base.metadata.create_all(bind=engine)  #SQLAlchemy looks inside Base Finds all classes that inherit from it and create all the tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5432"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

app.include_router(user_router)
app.include_router(food_router)





