from fastapi import FastAPI
from config.database import engine, Base
from controllers import auth_controller, wallet_controller, transaction_controller

# This creates all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Payment Wallet")

app.include_router(auth_controller.router)
app.include_router(wallet_controller.router)
app.include_router(transaction_controller.router)

@app.get("/")
def root():
    return {"message": "Payment Wallet App Running!"}