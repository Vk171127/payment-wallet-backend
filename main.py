from fastapi import FastAPI
from config.database import engine, Base

# This creates all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Payment Wallet")

@app.get("/")
def root():
    return {"message": "Payment Wallet App Running!"}