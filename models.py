from sqlalchemy import Integer, Float, String, VARCHAR, Column

from database import base

class Item(base):
    __tablename__= "items"
    id= Column(Integer, primary_key=True)
    name=Column(String)
    price= Column(Float)
    quantity=Column(Integer)