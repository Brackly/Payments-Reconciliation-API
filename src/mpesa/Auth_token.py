import requests
import os
import datetime
from dotenv import load_dotenv
from sqlalchemy import false

#Loading environment variables.

class TokenAuth:
    # """" Class Variables """
    BASIC_AUTHORIZATION = os.getenv('BASIC_AUTHORIZATION')
    timestamp=None
    token=None
    baseUrl=os.getenv('BASEURL')
    url=baseUrl+'/oauth/v1/generate?grant_type=client_credentials'

    # """" Functions Definitions """

    def timestamp_difference(x,y):
        if x<y:
            return y-x
        else:
            return x-y

    def is_token_generated(timestamp)->bool:
            return timestamp!=None
        
    def is_token_valid(self,timestamp)->bool:
            new_timestamp=datetime.datetime.now().strftime("%M")
            diff=self.timestamp_difference(int(new_timestamp),int(timestamp))
            return diff<58
    def generate_token(self)->str:
            try:
                headers={ 'Authorization': 'Basic '+ self.BASIC_AUTHORIZATION }
                response = requests.request("GET",self.url, headers = headers)
                token=response.json()['access_token']
                timestamp=datetime.datetime.now().strftime("%M")
                return token
            except Exception as error:
                print(error)
                return error


    def mpesa_auth_token(self):
        if self.is_token_generated(self.timestamp)==True and self.is_token_valid()==True:
            print(self.token)
            return self.token
        else:
            token=self.generate_token()
            print(token)
            return token