from urllib import request
from fastapi import FastAPI,Request,status
from db import SessionLocal
from model import Payment
import requests
from mpesa.C2B import C2B
from mpesa.Mpesa_Express import Mpesa_Express
from pydantic import BaseModel
#from .model import Account

app=FastAPI()
db=SessionLocal()

class Payment():
    TransactionType: str
    TransactionID: int
    DateTime: str
    Amount: int
    BusinessShortCode: str
    BillRefNumber: str
    OrgAccountBalance: float
    ThirdPartyTransID: str
    MSISDN : str
    FirstName : str
    MiddleName  : str
    LastName  : str

    class Config:
        orm_mode:True

def createpayment(payment):
    try:
        newpayment=Payment(
            TransactionType=payment["TransactionType"],
            TransactionID=payment["TransactionType"],
            DateTime=payment["TransactionType"],
            Amount=payment["TransactionType"],
            BusinessShortCode=payment["TransactionType"],
            BillRefNumber=payment["TransactionType"],
            OrgAccountBalance=payment["TransactionType"],
            ThirdPartyTransID=payment["TransactionType"],
            MSISDN=payment["TransactionType"],
            FirstName=payment["TransactionType"],
            MiddleName=payment["TransactionType"],
            LastName=payment["TransactionType"]) 
        db.add()
        return newpayment
    except Exception as error:
        return error

# <-- GET ALL PAYMENTS --> 
@app.get('/payments')
def get_all_payments():
    print('payments')
    return 'payments'
   
# <-- POST A PAYMENT --> 
@app.post('/payments/post')
def post_payment(payment:Payment):
    createpayment(payment)
    return {"payments added"}

# <-- TEST API CONFIRMATION URL --> 
@app.post('/payments/test')
def test_api(TransactionID):
    url = 'http://127.0.0.1:8000/mpesa/confirmation-url'
    myobj = {
            "TransactionID": "string",
            "DateTime": "string",
            "Amount": 0,
            "CustomerNumber": "string",
            "CustomerName": "string"}
    x = requests.post(url, json=myobj)
    return {"payment deleted"}


# <-- CHECK ACCOUNT STATUS -->   
@app.get('/account')
def get_account_details():
    return 'account'
   
# <-- MPESA URLS--> 
@app.get('/mpesa/register')
def register_url():
   register=C2B()
   register.C2B_register_url()
   return { "message":register.C2B_register_url()}

@app.get('/mpesa/pull-payments')
def pull_payments_url():
    register=C2B()
    register.C2B_lipa_na_mpesa(1,254705912645,'rent')
    return { "message":register.C2B_lipa_na_mpesa(1,254705912645,'rent')}

@app.get('/mpesa/stk-push')
def stk_push_url():
    push=Mpesa_Express()
    response=push.stk_push(1,"254741806859","milk","desc")
    return { "message":response}

@app.post('/mpesa/confirmation-url')
async def mpesa_confirmation_url(request:Request):
    try:
        print(await request.json())
        payment=await request.json()
        createpayment(payment)
        return await request.json()
    except Exception as error:
        return ({"error":error})
