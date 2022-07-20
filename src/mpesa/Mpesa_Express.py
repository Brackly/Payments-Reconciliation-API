import os
import requests
from dotenv import load_dotenv
from .Auth_token import TokenAuth

class Mpesa_Express:

    load_dotenv()

    # """" Variable Definitions """

    baseUrl=os.getenv('BASEURL')
    password=os.getenv('PASSWORD')
    shortcode=os.getenv('SHORTCODE')
    confirmationUrl=os.getenv('CONFIRMATION_URL')
    url=baseUrl+'/mpesa/stkpush/v1/processrequest'
    token=TokenAuth()

    headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "+token.mpesa_auth_token()
        }
        
    # """" Functions Definitions """

    def stk_push(self,amount,phone_number,reference,desc):
    
        payload = """
        {
        "BusinessShortCode": %s,
        "Password": "%s",
        "Timestamp": "20220715193311",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": %s,
        "PartyA": %s,
        "PartyB": %s,
        "PhoneNumber": %s,
        "CallBackURL": "%s",
        "AccountReference": "%s",
        "TransactionDesc": "%s"
        }
        """%(self.shortcode,self.password,amount,phone_number,self.shortcode,phone_number,self.confirmationUrl,reference,desc)

        response = requests.request("POST",self.url, headers = self.headers, data = payload)
        
        return response.json()