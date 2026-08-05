from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Student(BaseModel):
  name:str
  age:int

@app.post('/student')
def create_Student(student:Student):
  print(student.name,student.age)
  return student

'''
student["name"] -> don't use Because student is not a dictionary.
It's a Pydantic model object.
'''


  