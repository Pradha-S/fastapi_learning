#Importing the fastapi and other files
from fastapi import FastAPI
from Items import Items

#creating the fastapi application to start working with it
app=FastAPI()


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
def items_all():
    return items

#2. get a specified product using path parameter
@app.get("/items/{id}")
def item_id(id:int):
    for i in items:
        if i.id==id:
            return i
        
    return "Item not found"

#3. to create new record or data using POST

@app.post("/items")
def add_item(Var:Items): #var parameter recieved from the user of Items(pydantic class) , items is the list
    items.append(Var)
    return items

# to update the record use put

@app.put("/items")
def update_item(id:int,U_var:Items):
    for i in range(len(items)):
        if items[i].id==id:
            items[i]=U_var
            return "Updated sucessfully"
    return "Item not found"

#to delte a record using delete

@app.delete("/items/{id}")
def delete_item(id:int):
    for i in range(len(items)):
        if items[i].id==id:
            del items[i]
            return "Deleted Sucessfully"
    return "Error occured while deletion"