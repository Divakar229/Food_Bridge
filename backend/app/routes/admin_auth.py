from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
#OAuth2 → Standard way of doing login + token generation
from backend.app.schemas.admin_auth import AdminCreate, AdminResponse, Token
from backend.app.api.database import db_dependency
from ..curd.curd_admin import get_admin_by_email, create_admin
from backend.app.core.security import (
    hash_password,
    verify_pass,
    create_access_token
)
from backend.app.core.config import settings
from backend.app.core.dependencies import get_current_admin

router = APIRouter(prefix="/admin", tags=["Admin Auth"])

@router.post("/", response_model=AdminResponse)
def register_admin(admin: AdminCreate, db: Session = Depends(db_dependency)):
    if get_admin_by_email(db, admin.email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(admin.password)
    return create_admin(db, admin.email, hashed)

@router.post("/token", response_model=Token)
def login_admin(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(db_dependency)
):
    admin = get_admin_by_email(db, form.username)

    if not admin or not verify_pass(form.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": admin.email, "id": admin.id},
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=AdminResponse)
def get_me(current_admin=Depends(get_current_admin)):
    return current_admin
