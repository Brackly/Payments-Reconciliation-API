from typing import Optional
from pydantic import BaseModel


class Payment(BaseModel):
    TransactionID:str
    DateTime:str
    Amount:int
    CustomerNumber:int
    CustomerName:str
    is_Checked: Optional[bool]= None

class Account(BaseModel):
    AccountID:str
    AccountBalance:int
    DateTime:str
    PaymentsCountToday:int
    PaymentsCountTotal:int
    
