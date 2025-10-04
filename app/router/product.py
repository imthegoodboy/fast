from .. import schema,model,utills
from fastapi import APIRouter,Depends,HTTPException,APIRouter
from sqlalchemy.orm import session
from ..database import get_db
 

router=APIRouter(
    prefix="/product",
    tags=["Products"]
)



@router.get("/",response_model=list[schema.Product])
def get_products(dmb: session=Depends(get_db)):
    # cursor.execute(""" SELECT * FROM public."Products" """)
    # product=cursor.fetchall()
    product = dmb.query(model.Products).all()
    print(product)
    return   product 


# for create product
@router.post("/",response_model=schema.Product)
def create_product(product:schema.productCreate,dmb: session=Depends(get_db)):
    # cursor.execute(""" INSERT INTO public."Products" (name, price, inventory) VALUES (%s, %s, %s) RETURNING * """,(product.name, product.price, product.inventory))
    # new_product=cursor.fetchone()
    # new_product = model.Products(name=product.name, price=product.price, inventory=product.inventory)
    new_product = model.Products(**product.model_dump())
    dmb.add(new_product)
    dmb.commit()
    dmb.refresh(new_product)

    return  new_product 



# for delete product
@router.delete("/{id}")
def delete_product(id:int,dmb: session=Depends(get_db)):
    # cursor.execute(""" DELETE FROM public."Products" WHERE id = %s RETURNING * """,(id,))
    # deleted_product=cursor.fetchone()
    # conn.commit()
    deleted_product = dmb.query(model.Products).filter(model.Products.id == id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted_product.delete(synchronize_session=False)
    dmb.commit()
    return {"message": f"product is {deleted_product} deleted successfully"}

    
# for finding the individual product
@router.get("/{id}")
def find_product(id:int,dmb: session=Depends(get_db)):
    # cursor.execute(""" SELECT * FROM public."Products" WHERE id = %s """,(id,))
    # product=cursor.fetchone()
   
    product = dmb.query(model.Products).filter(model.Products.id == id).first()
    return   product 


#for updating the product
@router.put("/{id}")
def update_product(id:int, product:schema.productCreate,dmb: session=Depends(get_db)):
    # cursor.execute(""" UPDATE public."Products" SET name = %s, price = %s, inventory = %s WHERE id = %s RETURNING * """,(product.name, product.price, product.inventory, id))
    # updated_product=cursor.fetchone()
    # print(updated_product)
    # conn.commit()
    updated_querry=dmb.query(model.Products).filter(model.Products.id == id)
    producct=updated_querry.first()
    if producct is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    updated_querry.update(product.dict(),synchronize_session=False)
    dmb.commit()
    dmb.refresh(producct)
    return {"message":"Product updated successfully"}

