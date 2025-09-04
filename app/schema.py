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




class Product(BaseModel):
 
    name:str
    price:int

    class config:
        orm_mode = True


class usercreate(BaseModel):
    name:str
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    name:str
    email:EmailStr
 

    class Config:
        orm_mode = True



class UserLogin(BaseModel):
    email:EmailStr
    password:str