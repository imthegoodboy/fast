from fastapi import APIRouter,Depends,HTTPException,APIRouter

from .. import schema,model,utills
from sqlalchemy.orm import session
from ..database import get_db

router=APIRouter(
    tags=["Auth"]
    )

#for user login page

@router.post("/login" )
def login_user(user_credentials:schema.userlogin_credentials,dmb: session=Depends(get_db)):
    
    user=dmb.query(model.Users).filter(model.Users.email == user_credentials.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not utills.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=404, detail="Invalid password")
    
    return {"message": "Login successful"}