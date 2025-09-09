from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from ..config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(pw: str) -> str:
    return pwd.hash(pw)

def verify_password(pw: str, hash_pw: str) -> bool:
    return pwd.verify(pw, hash_pw)

def create_token(sub: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({"sub": sub, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES}

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except Exception:
        return None
