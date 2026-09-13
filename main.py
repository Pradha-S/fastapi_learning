#Importing the fastapi and other files
from fastapi import FastAPI
from Items import Items

#creating the fastapi application to start working with it
app=FastAPI()


items=[
    Items(1,"Rice", 240,4),
    Items(3,"dal", 220,7)

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
@app.get("/items/{name}")
def item_name(name):
    return {"Item needed": f"{name}"}


