from .. import schema,model,utills
from fastapi import APIRouter,Depends,HTTPException,APIRouter
from sqlalchemy.orm import session
from ..database import get_db
from sqlalchemy.orm import Session
 

router=APIRouter(
    tags=["Users"]
)





@router.post("/signup")
def signup(user:schema.usercreate,dmb: session=Depends(get_db)):
    # Check if user already exists
    existing_user = dmb.query(model.Users).filter(model.Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #Hashing the password
    hashed_password=utills.hash(user.password)
    user.password=hashed_password
    new_user = model.Users(**user.dict())
    dmb.add(new_user)
    dmb.commit()
    dmb.refresh(new_user)
    return  new_user


 

  





@router.get("/user/{id}",response_model=schema.UserOut)
def user_details(id:int,dmb: session=Depends(get_db)):
    user = dmb.query(model.Users).filter(model.Users.id == id).first()
 
    return user



    