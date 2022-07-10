from fastapi import FastAPI

app=FastAPI()

payments=[]

@app.get('/')
def get_all_payments():
    return {"welcome to the payments API"}

@app.get('/payments')
def get_all_payments():
    return payments
  
@app.get('/payments/{paymentID}')
def get_all_payments(paymentID:str):
    return payments[paymentID]

@app.post('/payments/create-payment')
def get_all_payments():
    return {"PAYMENT CREATED SUCCESSFULLY"}



    
