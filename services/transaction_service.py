from repositories import transaction_repository, wallet_repository
from sqlalchemy.orm import Session

def get_user_transactions(db: Session, user_id: int):
    return transaction_repository.get_transactions_by_user_id(db, user_id)

def send_money(db: Session, sender_id: int, receiver_id: int, amount: float):
    
    if amount <= 0:
        raise ValueError("Amount must be greater than zero")
    
    sender_wallet = wallet_repository.get_wallet_by_user_id(db, sender_id)
    receiver_wallet = wallet_repository.get_wallet_by_user_id(db, receiver_id)

    if sender_id == receiver_id:
        raise ValueError("Cannot send money to yourself")
    
    if not sender_wallet:
        raise ValueError("Sender wallet not found")
    if not receiver_wallet:
        raise ValueError("Receiver wallet not found")
    
    if sender_wallet.balance < amount:
        raise ValueError("Insufficient funds in sender's wallet")
    
    # Deduct from sender and add to receiver
    wallet_repository.update_wallet_balance(db, sender_wallet, -amount)
    wallet_repository.update_wallet_balance(db, receiver_wallet, amount)

    # Create transaction record
    transaction = transaction_repository.create_transaction(db, sender_id, receiver_id, amount)

    return transaction