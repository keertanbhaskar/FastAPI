'''
Easy Definition (Interview)
HTTPException is used to return meaningful error messages and HTTP status codes when something goes wrong in an API.


--------- Syntax -----------
raise HTTPException(
    status_code=404,
    detail="Student not found"
)

status_code
This tells the client what type of error happened.
ex: status_code=404


detail
This is the error message.
ex: detail="Student not found"

'''

from fastapi import FastAPI,HTTPException

app = FastAPI()
students = {
  1:"keertana",
  2:"Sam"
}



@app.get('/students/{student_id}')
def get_student(student_id:int):
  if student_id not in students:
    raise HTTPException(
      status_code=404,
      detail='Student not Found'
    )
  return{
    "student":students[student_id]
  }
