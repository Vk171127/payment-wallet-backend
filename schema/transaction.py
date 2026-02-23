from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    receiver_id: int
    amount: float

class TransactionResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True