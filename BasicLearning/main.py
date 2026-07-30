from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
  return {"message":"my first API is working"}

@app.get('/About')
def about():
  return {'project':'loan risk model','version':'1.0'}

@app.get('/customer')
def customer(customer_id:int):
  return{
    "customer_id":customer_id,
    'name':'kk',
    'status':'active'
  }

# http://127.0.0.1:8000/customer?customer_id=100 => to this in url to take parameters & to separate multiple parameters

