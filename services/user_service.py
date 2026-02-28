from sqlalchemy.orm import Session
from repositories import user_repository, wallet_repository
from schema.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated ='auto')

def hashpassword(password: str):
    return pwd_context.hash(password)

def verifypassword(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def register_user(db: Session, user_data: UserCreate):
    existing_user = user_repository.get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("Email already registered")
    hashed_password = hashpassword(user_data.password)
    new_user = user_repository.create_user(db, user_data.name, user_data.email, hashed_password)
    wallet_repository.create_wallet(db, new_user.id)
    return new_user