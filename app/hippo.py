from multiprocessing import synchronize
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import model 
from sqlalchemy.orm import Session, session
from fastapi import Depends
from .database import engine,  get_db
from random import randrange
from . import schema , utills
from passlib.context import CryptContext
from .router import product,user 

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

model.Base.metadata.create_all(bind=engine)

app = FastAPI()




# for database connection

while True:
    try:
        conn=psycopg2.connect(host='localhost',database='hippodb',user='postgres',password='kali',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Error in connection to the database" , error )
        time.sleep(2)
        

    # my_name=[{"name":"nikku","housenumber":123},{"name":"hikku","housenumber":123}]

    # @app.get("/nikku")
    # def hello():
    #     return  my_name 


    # @app.post("/")
    # def post(payload:create_product):
    #     my_name.append(payload)
    #     return {"message": my_name}

app.include_router(product.router)
app.include_router(user.router)
 