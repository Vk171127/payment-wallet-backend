from sqlalchemy.orm import Session
from model.transaction import Transaction

def get_transactions_by_user_id(db: Session, user_id: int):
    return db.query(Transaction).filter(
        (Transaction.sender_id == user_id) | (Transaction.receiver_id == user_id)
    ).order_by(Transaction.created_at.desc()).all()

def create_transaction(db: Session, sender_id: int, receiver_id: int, amount: float, status: str = "success"):
    new_transaction = Transaction(
        sender_id=sender_id,
        receiver_id=receiver_id,
        amount=amount,
        status=status
    )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction