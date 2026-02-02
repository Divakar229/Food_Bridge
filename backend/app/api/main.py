from fastapi import FastAPI,Depends,HTTPException
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from backend.app.models.model import Base,Product
from backend.app.api.database import engine,db_dependency
from sqlalchemy.orm import Session
from backend.app.schemas.schema import ProductCreate
PRODUCTION=False
app=FastAPI(
    docs_url=None if PRODUCTION else "/docs",
    redoc_url=None if PRODUCTION else "/redocs",
    openapi_url=None if PRODUCTION else "/openapi.json.", 
)
# Base.metadata.create_all(bind=engine)  #SQLAlchemy looks inside Base Finds all classes that inherit from it and create all the tables

Base.metadata.create_all(bind=engine)

db_depen=Annotated[Session,Depends(db_dependency)]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5432"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
def greet():
    return {"message":"hello world"}

@app.get('/product')
def all(db:db_depen):
    return db.query(Product).all()

@app.post('/practice')
def create(P:ProductCreate,db:Session=Depends(db_dependency)):
    data = Product(**P.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data



@app.get("/practise/{id}")
def find(roll:int,db:Session=Depends(db_dependency)):
    id=db.query(Product).filter(Product.roll==roll).first()
    if not id:
        raise HTTPException(status_code=404,detail="not found")
    return id


