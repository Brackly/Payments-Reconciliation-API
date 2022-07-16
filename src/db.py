import os
import datetime

from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

hostname=os.getenv('HOSTNAME')
database=os.getenv('DATABASE')
username=os.getenv('USERNAME')
password=os.getenv('PASSWORD')
port_id=os.getenv('PORTID')

engine = create_engine('postgresql://{}:{}@{}/{}'.format(username,password,hostname,database),
echo=True)

#print('postgresql://{}:{}@{}/{}'.format(username,password,hostname,database))

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)





