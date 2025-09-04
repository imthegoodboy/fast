from jose import JWTError, jwt
from datetime import datetime, timedelta


SECRET_KEY = "nikkuies"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def acces_token(data:dict):
    to_incode=data.copy()
    expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_incode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_incode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt