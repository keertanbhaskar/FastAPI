from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# a clear structure
class LoanApplication(BaseModel):
  name:str
  age:int
  income:float
  loan_amount : float
  emp_years:int


@app.post('/predict')
def predict_loan(application:LoanApplication):
  # model login
  approved = (
    application.income > 5000 and
    application.emp_years > 2 and
    application.age >= 20
  )

  return {
    'application':application.name,
    'loan_amount':application.loan_amount,
    'decision':"approved" if approved else "rejected",
    'age':application.age,

  }