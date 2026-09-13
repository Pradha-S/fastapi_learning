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


#used to run if we have to search by /home

@app.get("/items")
def items_all():
    return items

#use of path parameter
@app.get("/items/{id}")
def item_id(id:int):
    for i in items:
        if i.id==id:
            return items[id-1]
        
    return "Item not found"


