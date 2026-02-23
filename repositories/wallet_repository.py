from sqlalchemy.orm import Session
from model.wallet import Wallet

def get_wallet_by_user_id(db: Session, user_id: int):
    return db.query(Wallet).filter(Wallet.user_id == user_id).first()

def create_wallet(db: Session, user_id: int):
    new_wallet = Wallet(user_id=user_id)
    db.add(new_wallet)
    db.commit()
    db.refresh(new_wallet)
    return new_wallet

def update_wallet_balance(db: Session, wallet: Wallet, amount: float):
    wallet.balance += amount
    db.commit()
    db.refresh(wallet)
    return wallet