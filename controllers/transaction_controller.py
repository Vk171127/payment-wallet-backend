from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schema.transaction import TransactionResponse, TransactionCreate
from schema.user import UserResponse
from services import transaction_service
from controllers.deps import get_current_user

router = APIRouter(prefix="/transaction", tags=["transaction"])

@router.post("/send", response_model=TransactionResponse)
def transfer_funds(payload: TransactionCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    try:
        transaction = transaction_service.send_money(db, current_user.id, payload.receiver_id, payload.amount)
        return transaction
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/history", response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    transactions = transaction_service.get_user_transactions(db, current_user.id)
    return transactions