from urllib import request
from fastapi import FastAPI,Request
from model import Payment
import requests
from mpesa.C2B import C2B
from mpesa.Mpesa_Express import Mpesa_Express
#from .model import Payment
#from .model import Account

app=FastAPI()

payments=[]
account={
    "AccountID":"656119",
    "AccountBalance":0,
    "DateTime":"str",
    "PaymentsCountToday":0,
    "PaymentsCountTotal":0}

@app.get('/')
def home():
    return {"Message":"Welcome Home"}

@app.get('/payments')
def get_all_payments():
    print(payments)
    return payments
  
@app.get('/account')
def get_account_details():
    return account

@app.post('/payments/create')
def create_manual_payment():

    url = 'http://127.0.0.1:8000/mpesa/confirmation-url'
    myobj = {
            "TransactionID": "string",
            "DateTime": "string",
            "Amount": 0,
            "CustomerNumber": "string",
            "CustomerName": "string"}
    x = requests.post(url, json=myobj)
    return {"payments added"}

@app.delete('/payments/delete/{TransactionID}')
def delete_payment(TransactionID):
    for payment in payments:
        if payment["TransactionID"]==TransactionID:
            payments.remove(payment)
    return {"payment deleted"}


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
        payments.append( await request.json())
        return await request.json()
    except Exception as error:
        return ({"error":error})
