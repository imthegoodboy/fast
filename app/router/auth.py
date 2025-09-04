from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schema, model, utills,oauth
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=["Authentication"]
)


@router.post("/authenticate")
def authenticate_user(user_cred=OAuth2PasswordRequestForm,db:Session=Depends(get_db)):
    user =db.query(model.Users).filter(model.Users.email==user_cred.email).first()
    access_token=oauth.create_access_token(data={"user_id":user.id})
    utills.verify(user_cred.password,user.password)
    return {"access_token":access_token,"token_type":"bearer"}
    