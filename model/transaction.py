from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from datetime import datetime, timezone
from config.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="success")  # success / failed
    created_at = Column(DateTime, default= lambda: datetime.now(timezone.utc))