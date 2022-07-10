from fastapi import FastAPI

app=FastAPI()

payments=[

]

@app.get('/')
def get_all_payments():
    return payments

    
