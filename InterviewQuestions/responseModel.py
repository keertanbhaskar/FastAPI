'''
1. Security

Hide sensitive data like:
Password
OTP
Bank account number

2. Clean Responses
The client only gets the data they actually need.

3. Automatic Validation
FastAPI also validates the response before sending it.
'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentResponse(BaseModel):
  name:str
  age:int

@app.get("/students",response_model=StudentResponse)
def get_student():
  return{
    'name':"keertana",
    'age':21,
    "password":"abc123"
  }