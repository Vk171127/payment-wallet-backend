from config.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.user import UserCreate, UserResponse, UserLogin
from services import user_service
from utils.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(userData: UserCreate, db: Session = Depends(get_db)):
    try:
        user = user_service.register_user(db, userData)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(userData: UserLogin, db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, userData.email, userData.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}