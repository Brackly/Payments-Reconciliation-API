from sqlalchemy import Integer,String,Boolean
from sqlalchemy.sql.schema import Column
from database import Base

class Payment(Base):
    __tablename__='payments'
    TransactionType=Column(String,nullable=False)
    TransID=Column(String,primary_key=True)
    TransTime=Column(String,nullable=False)
    TransAmount=Column(String, nullable=False)
    BusinessShortCode=Column(String, nullable=False)
    BillRefNumber=Column(String, nullable=False)
    InvoiceNumber=Column(String, nullable=False)
    OrgAccountBalance=Column(String, nullable=False)
    ThirdPartyTransID=Column(String, nullable=False)
    MSISDN=Column(String, nullable=False)
    FirstName=Column(String, nullable=False)
    seen=Column(Boolean,default=False)
