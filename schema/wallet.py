from pydantic import BaseModel
from datetime import datetime

class WalletResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: datetime

    class Config:
        from_attributes = True
