
#using pydantic model for data validation and initilization
from pydantic import BaseModel
#the class will inherit the basemodel

class Items(BaseModel):
    id:int
    name:str
    price:float
    quantity:int

    