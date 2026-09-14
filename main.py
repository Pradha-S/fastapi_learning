#Importing the fastapi and other files
from fastapi import FastAPI
from Items import Items

from database import Session_local,base, connection
from fastapi import Depends
from sqlalchemy.orm import Session
from models import Item



base.metadata.create_all(bind=connection)

#creating the fastapi application to start working with it
app=FastAPI()

#db code

def get_db():
    db=Session_local()
    try:
        yield db
    finally:
        db.close()




items=[
    Items(id=1,name="Rice", price=240,quantity=4),
    Items(id=2,name="M_Dal", price=160,quantity=1),
    Items(id=3,name="Channa", price=350,quantity=2),
    Items(id=4,name="Almond", price=450,quantity=1),
    Items(id=5,name="Soya", price=230,quantity=3)

]


#used to run the function if user starts from / that is home in url 
#during get request

@app.get("/")
def greet():
    return {"msg": "WELCOME!!!"}


#1. To get or fetch the all items

@app.get("/items")
def items_all(db:Session= Depends(get_db)):
    return db.query(Item).all()


#2. get a specified product using path parameter

@app.get("/items/{id}")
def item_id(id:int, db:Session=Depends(get_db)):
    db_item = db.get(Item, id) # get from which table (Item) and then what?? id
    if(db_item):
        return db_item
        
    return "Item not found"

#3. to create new record or data using POST

@app.post("/items")
def add_item(Var:Items, db:Session=Depends(get_db)): #var parameter recieved from the user of Items(pydantic class) , items is the list
    db_item= Item(**Var.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#4. to update the record use put

@app.put("/items")
def update_item(id:int,U_var:Items, db:Session=Depends(get_db)):
    db_item =db.get(Item, id)

    if(db_item):
        db_item.name= U_var.name
        db_item.price = U_var.price
        db_item.quantity= U_var.quantity
        db.commit()
        return "Updated Successfully"

    else:
        return "Item not found"

#5. to delte a record using delete

@app.delete("/items/{id}")
def delete_item(id:int, db:Session=Depends(get_db)):
    db_item =db.get(Item, id)
    if(db_item):
        db.delete(db_item)
        db.commit()
        return "Item Deleted Sucessfully"
    else:

        return "Error occured while deletion"


