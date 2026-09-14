#to create connection to the data base
from sqlalchemy import create_engine
#declarative_base : to create tables or models, session maker is for fastapi interaction with the db
from sqlalchemy.orm import declarative_base, sessionmaker

#from models import Item


#to create conenction:
Database_url ="sqlite:///./items.db"
connection =create_engine(Database_url)

base= declarative_base()

Session_local = sessionmaker(autoflush=False, autocommit=False, bind=connection)


