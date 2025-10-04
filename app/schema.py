from pydantic import BaseModel, EmailStr

class productBase(BaseModel):
    name:str
    price:int
    inventory:int


# class create_product(BaseModel):
#     name:str
#     price:int
#     inventory:int


# class update_product(BaseModel):
#     name:str
#     price:int
#     inventory:int

 
class productCreate(productBase):
    pass



# for getting the product(response model)
class Product(BaseModel):
 
    name:str
 
    class config:
        orm_mode = True




#for USERS

class usercreate(BaseModel):
    name:str
    email:EmailStr
    password:str


#response for the user 
class UserOut(BaseModel):
    id:int
    name:str
    email:EmailStr
 

    class Config:
        orm_mode = True



class UserLogin(BaseModel):
    email:EmailStr
    password:str



class userlogin_credentials(BaseModel):
    email:EmailStr
    password:str