from urllib import request
from fastapi import FastAPI,Request
from model import Payment
import requests
from mpesa.C2B import C2B
from mpesa.Mpesa_Express import Mpesa_Express
#from .model import Payment
#from .model import Account

app=FastAPI()


@app.get('/payments')
def get_all_payments():
    pass
  

@app.post('/payments/create')
def create_manual_payment():
    pass

@app.delete('/payments/delete/{TransactionID}')
def delete_payment(TransactionID):
    pass


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
        payment=await request.json()
        return await request.json()
    except Exception as error:
        return ({"error":error})
