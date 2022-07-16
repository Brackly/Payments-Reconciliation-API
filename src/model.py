from pydantic import BaseModel
class Payment(BaseModel):
    TransactionType: str
    TransactionID: int
    DateTime: str
    Amount: int
    BusinessShortCode: str
    BillRefNumber: str
    OrgAccountBalance: float
    ThirdPartyTransID: str
    MSISDN : int
    FirstName : str
    MiddleName  : str
    LastName  : str
    seen: bool

class Account(BaseModel):
    AccountBalance:int
    DateTime:str

