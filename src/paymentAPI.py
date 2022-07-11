from fastapi import FastAPI
from mpesa import mpesa_auth_token,C2B_register_url,C2B_lipa_na_mpesa,stk_push
from model import Payment
#from .model import Payment
#from .model import Account

app=FastAPI()

payments={
  "access_token": "SO4hig1BNmb4klJdfriVQBLSK49F",
  "expires_in": "3599"
}
account={
    "AccountID":"656119",
    "AccountBalance":0,
    "DateTime":"str",
    "PaymentsCountToday":0,
    "PaymentsCountTotal":0}

@app.get('/')
def home():
    return payments["access_token"]

@app.get('/payments')
def get_all_payments():
    return payments
  
@app.get('/account')
def get_account_details():
    return account

@app.post('/payments/create')
def create_manual_payment(payment: Payment):
    payments.append(payment.dict())
    return {"payments added"}

@app.delete('/payments/delete/{TransactionID}')
def delete_payment(TransactionID):
    for payment in payments:
        if payment["TransactionID"]==TransactionID:
            payments.remove(payment)
    return {"payment deleted"}


@app.get('/register')
def register_url():
    register_url=C2B_register_url()
    return { "message":register_url}

@app.get('/pull-payments')
def pull_payments_url():
    response=C2B_lipa_na_mpesa(1,254705912645,'rent')
    return { "message":response}

@app.get('/stk-push')
def stk_push_url():
    response=stk_push(1,254741806859)
    return { "message":response}






    
