from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.user import UserResponse
from schema.wallet import WalletResponse
from services import wallet_service
from config.database import get_db
from controllers.deps import get_current_user

router = APIRouter(prefix="/wallet", tags=["wallet"])

@router.get("/", response_model=WalletResponse)
def get_wallet(db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    try:
        wallet = wallet_service.get_wallet(db, current_user.id)
        return wallet
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
