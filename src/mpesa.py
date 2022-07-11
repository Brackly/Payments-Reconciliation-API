import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASIC_AUTHORIZATION = os.getenv('BASIC_AUTHORIZATION')
confirmationUrl=os.getenv('CONFIRMATION_URL')
validationUrl=os.getenv('VALIDATION_URL')
responseType=os.getenv('RESPONSE_TYPE')
shortcode=os.getenv('SHORTCODE')

def mpesa_auth_token():
    try:
        url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        headers={ 'Authorization': 'Basic '+ BASIC_AUTHORIZATION }
        response = requests.request("GET",url, headers = headers)
        token=response.json()['access_token']
        return token
    except Exception as error:
        print(error)
        return error

token=mpesa_auth_token()

def C2B_register_url():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+ token
    }
    payload = """
        {
        "ShortCode": %s,
        "ResponseType": "%s",
        "ConfirmationURL": "%s",
        "ValidationURL": "%s"
        }
    """%(shortcode,responseType,confirmationUrl,validationUrl)

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl', headers = headers, data = payload)
    return response.json()

def C2B_lipa_na_mpesa(amount,phone_number,reference):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+ token
    }
    
    payload = """
    {
    "ShortCode": %s,
    "CommandID": "CustomerPayBillOnline",
    "Amount": "%s",
    "Msisdn": "%s",
    "BillRefNumber": "%s"
    }
    """%(shortcode,amount,phone_number,reference)
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate', headers = headers, data = payload)
    return response.json()

def stk_push(amount,phone_number):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "+ token
    }
    payload = """
    {
    "BusinessShortCode": %s,
    "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjIwNzExMTkwOTUy",
    "Timestamp": "20220711190952",
    "TransactionType": "CustomerPayBillOnline",
    "Amount": %s,
    "PartyA": %s,
    "PartyB": %s,
    "PhoneNumber": %s,
    "CallBackURL": "%s",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X"
    }
    """%(shortcode,amount,phone_number,shortcode,phone_number,confirmationUrl)

    print(payload)
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    return response.json()






