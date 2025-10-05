from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import session
from pydantic.networks import HttpUrl
from . import schema , database,model
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
        id:int=payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=schema.TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token:str=Depends(oauth2_scheme),db:session=Depends(database.get_db)):
    credentials_exception=HTTPException(status_code=401,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    
    token_data=verify_token(token,credentials_exception)
    user=db.query(model.Users).filter(model.Users.id==token_data.id).first()
    return user
