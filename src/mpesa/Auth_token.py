import requests
import os
import datetime
from dotenv import load_dotenv
from sqlalchemy import false

#Loading environment variables.
load_dotenv()
class TokenAuth:
    # """" Class Variables """
    BASIC_AUTHORIZATION = os.getenv('BASIC_AUTHORIZATION')
    baseUrl=os.getenv('BASEURL')
    url=baseUrl+'/oauth/v1/generate?grant_type=client_credentials'

    # """" Functions Definitions """
    def mpesa_auth_token(self)->str:
        try:
            headers={ 'Authorization': 'Basic '+ self.BASIC_AUTHORIZATION }
            response = requests.request("GET",self.url, headers = headers)
            self.token=response.json()['access_token']
            self.timestamp=datetime.datetime.now().strftime("%M")
            print(self.token)
            return self.token
        except Exception as error:
            print(error)
            return error