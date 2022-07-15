import os
import requests
from dotenv import load_dotenv

class Mpesa_Express:

    # """" Variable Definitions """

    baseUrl=os.getenv('BASEURL')
    url=baseUrl+'/mpesa/stkpush/v1/processrequest'
    token=None

    headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "+ token
        }
        
    # """" Functions Definitions """

    def stk_push(self,amount,phone_number):
    
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
        """%(self.shortcode,amount,phone_number,self.shortcode,phone_number,self.confirmationUrl)

        print(payload)
        response = requests.request("POST",self.url, headers = self.headers, data = payload)
        return response.json()