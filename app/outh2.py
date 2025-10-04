from jose import JWTError, jwt
from datetime import datetime, timedelta

from pydantic.networks import HttpUrl
from . import schema
from fastapi import Depends,status,HTTPException

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')

SECRECT_KEY="hello@world"
ALGORITHM="HS256"
EXPIRE_MINUTES=100


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRECT_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRECT_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=schema.TokenData(id=id)
    except JWTError:
        raise credentials_exception

 