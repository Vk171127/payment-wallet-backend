from sqlalchemy.orm import Session
from repositories import wallet_repository

def get_wallet(db: Session, user_id: int):
    wallet = wallet_repository.get_wallet_by_user_id(db, user_id)
    if not wallet:
        raise ValueError("Wallet not found for user")
    return wallet