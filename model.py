from typing import Optional
from pydantic import BaseModel


class Payment(BaseModel):
    TransactionID: str
    DateTime: str
    Amount: int
    CustomerNumber: str
    CustomerName: str

class Account(BaseModel):
    AccountID:str
    AccountBalance:int
    DateTime:str
    PaymentsCountToday:int
    PaymentsCountTotal:int

