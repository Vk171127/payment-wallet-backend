from datetime import datetime, timedelta, timezone
from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

def create_access_token(data: dict):
    jwt_payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    jwt_payload.update({"exp": expire})
    encoded_jwt = jwt.encode(jwt_payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt