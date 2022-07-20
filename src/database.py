from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#Loading environment variables.
load_dotenv()


host=os.getenv("HOSTNAME")
database=os.getenv("DATABASE")
username=os.getenv("USERNAME")
password=os.getenv("PASSWORD")
port=os.getenv("PORTID")


SQL_ALCHEMY_DATABASE_URL=f"postgresql://{username}:{password}@{host}/{database}"

engine=create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,bind=engine)

Base=declarative_base()

def getdb():
    db=SessionLocal()
    try:
        yield db
    except:
        db.close()