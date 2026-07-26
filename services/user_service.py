from sqlalchemy.orm import Session
from repositories import user_repository, wallet_repository
from schema.user import UserCreate
from passlib.context import CryptContext
from utils.email import normalize_email

pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='auto', bcrypt__rounds=12)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, email: str, password: str):
    normalized_email = normalize_email(email)
    user = user_repository.get_user_by_email(db, normalized_email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def register_user(db: Session, user_data: UserCreate):
    normalized_email = normalize_email(user_data.email)
    existing_user = user_repository.get_user_by_email(db, normalized_email)
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password = hash_password(user_data.password)
    new_user = user_repository.create_user(db, user_data.name, normalized_email, hashed_password)
    wallet_repository.create_wallet(db, new_user.id)
    return new_user