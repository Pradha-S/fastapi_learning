#Importing the fastapi and other files
from fastapi import FastAPI

#creating the fastapi application to start working with it
app=FastAPI()

#used to run the function if user starts from / that is home in url 
#during get request

@app.get("/")
def greet():
    return {"msg": "WELCOME!!!"}


