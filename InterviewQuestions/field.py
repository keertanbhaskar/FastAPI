'''
Field => we can enforce business rules like:
Name must have at least 3 characters.
Age must be greater than 0.
Salary must be positive.
Email must follow a valid format (with specialized types).
Loan amount must be within an allowed range.
'''

from pydantic import BaseModel, Field

# single validation
class Student(BaseModel):
  name:str = Field(min_length=3)
  age:int = Field(gt=0) # gt > 0
  cgpa:float = Field(gt=0,le=0)


# multiple validation
class Application(BaseModel):
  name:str = Field(min_length=3,max_length=50)
  age : int = Field(ge=18,le=60)
  cgpa:float = Field(ge=0,le=10)

# Notice that each field can have more than one validation rule.
# Type hints validate the type.
# Field() validates the value according to your business rules.

