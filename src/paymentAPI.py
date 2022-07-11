from fastapi import FastAPI

from model import Payment
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
    return {"welcome to the payments API"}

@app.get('/payments')
def get_all_payments():
    return payments
  
@app.get('/account')
def get_account_details():
    return account

@app.post('/payments/create')
def create_payment(payment: Payment):
    payments.append(payment.dict())
    return {"payments added"}

@app.delete('/payments/delete/{TransactionID}')
def delete_payment(TransactionID):
    for payment in payments:
        if payment["TransactionID"]==TransactionID:
            payments.remove(payment)
    return {"payment deleted"}






    
