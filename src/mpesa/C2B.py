import os
import requests
from dotenv import load_dotenv

class C2B:

    # """" Class Variables """

    token=None
    BASIC_AUTHORIZATION = os.getenv('BASIC_AUTHORIZATION')
    confirmationUrl=os.getenv('CONFIRMATION_URL')
    validationUrl=os.getenv('VALIDATION_URL')
    responseType=os.getenv('RESPONSE_TYPE')
    shortcode=os.getenv('SHORTCODE')
    baseUrl=os.getenv('BASEURL')
    url=baseUrl+'/mpesa/c2b/v1/simulate'

    headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "+ token
        }

    # """" Functions Definitions """

    def C2B_register_url(self):

        payload = """
            {
            "ShortCode": %s,
            "ResponseType": "%s",
            "ConfirmationURL": "%s",
            "ValidationURL": "%s"
            }
        """%(self.shortcode,self.responseType,self.confirmationUrl,self.validationUrl)

        response = requests.request("POST", self.url, headers = self.headers, data = payload)

        return response.json()

    def C2B_lipa_na_mpesa(self,amount,phone_number,reference):

        payload = """
        {
        "ShortCode": %s,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "%s",
        "Msisdn": "%s",
        "BillRefNumber": "%s"
        }
        """%(self.shortcode,amount,phone_number,reference)

        response = requests.request("POST", self.url, headers = self.headers, data = payload)

        return response.json()