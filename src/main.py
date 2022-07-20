from fastapi import FastAPI,Request,Depends,status
from mpesa.C2B import C2B
from mpesa.Mpesa_Express import Mpesa_Express
from schema import PaymentRequest
from database import getdb
from model import Payment
from sqlalchemy.orm import Session

app=FastAPI()


def create_payment(payment,db)-> str:
    if payment:
        return "Payment already exists"
    try:
        new_payment=Payment(
            TransactionType=payment.TransactionType,
            TransID=payment.TransID,
            TransTime=payment.TransTime,
            TransAmount=payment.TransAmount,
            BusinessShortCode=payment.BusinessShortCode,
            BillRefNumber=payment.BillRefNumber,
            InvoiceNumber=payment.InvoiceNumber,
            OrgAccountBalance=payment.OrgAccountBalance,
            ThirdPartyTransID=payment.ThirdPartyTransID,
            MSISDN=payment.MSISDN,
            FirstName=payment.FirstName
        )
        
        db.add(new_payment)
        db.commit()
        return f"Success!! Payment with payment id {new_payment.TransID} added."
    except Exception as error:
        return error




# <-- GET ALL PAYMENTS --> 
@app.get('/payments')
def get_all_payments(db:Session=Depends(getdb)):
    return db.query(Payment).all()

@app.get('/payment/')
def get_a_payment(TransID: str,db:Session=Depends(getdb)):
    payment= db.query(Payment).filter(Payment.TransID==TransID).first()
    if payment is None:
        return{"Status":status.HTTP_404_NOT_FOUND,"message":"Payment not found"}
    return payment

@app.put('/payment/seen')
def mark_as_seen(TransID: str,db:Session=Depends(getdb)):
    payment=db.query(Payment).filter(Payment.TransID==TransID)
    if payment is None:
        return{"Status":status.HTTP_404_NOT_FOUND,"message":"Payment not found"}
    payment.seen=True
    db.add(payment)
    db.commit()
    print(payment.seen)
    return payment
  
@app.post('/payments/create')
def create_manual_payment(payment:PaymentRequest,db:Session=Depends(getdb)):
    response=create_payment(payment,db)
    return {"response":response}
    


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
        payment=await request.json()
        return await request.json()
    except Exception as error:
        return ({"error":error})
