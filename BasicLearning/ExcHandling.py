from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()

students = {
  'S001':{'name':'kk','marks':85,'grade':'A'},
  'S002':{'name':'keertana','marks':95,'grade':'A+'},
  'S003':{'name':'priya','marks':70,'grade':'B'},

}

# input schema
class MarksSubmission(BaseModel):
  student_id:str
  marks:int
  subject:str

# create end point student and passing query student_id
@app.get('/student/{student_id}')
def get_student(student_id:str):
  if student_id not in students:
    raise HTTPException(
      status_code=404,
      detail=f'Student with ID {student_id} does not exists'
    )
  return students[student_id]



@app.post('/submit-marks')
def submit_marks(submission:MarksSubmission):

  # error1 student does not exists
  if submission.student_id not in students:
    raise HTTPException(
      status_code=404,
      detail='student not found'
    )

  # error2 valid range 0-100
  if submission.marks < 0 or submission.marks >100:
    raise HTTPException(
      status_code=400,
      detail={
        'error':'marks must be between 0 to 100',
        'marks_received':submission.marks,
        'fix':'enter a valid value between 0 to 100'
      }
    )

  #error3 subject name empty
  # strip => removes extra space
  if submission.subject.strip() =="":
    raise HTTPException(
          status_code=400,
          detail={
            'error':'enter the sub properly',
            
          }
    )

  try:
    students[submission.student_id]['marks'] = submission.marks

    return{
      'message':'marks submitted successfully',
      'student':students[submission.student_id]['name'],
      'subject':submission.subject,
    }

  except Exception as e:
    raise HTTPException(
      status_code=500,
      detail=str(e)
    )
  finally:
    print('Request completed')




