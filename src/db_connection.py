from db import Base,engine,hostname,password

from model import Payment,Account
print(hostname+" "+password)
try:
    print("Connectind....")
    Base.metadata.create_all(engine)
    print("success!!")
except Exception as e:
    print(e)