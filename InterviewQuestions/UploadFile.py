'''
File Upload is a feature that allows the client to send files 
(such as CSV, images, PDFs, or Excel files) to the FastAPI server.

File(...)

Tells FastAPI:
"This parameter should come from a file upload."
Without File(...), FastAPI won't know the data is coming as a file.


What is the difference between UploadFile and File(...)?
A good answer is:
"UploadFile represents the uploaded file and provides 
information such as the filename and content type. 
File(...) tells FastAPI that the parameter should be received as a 
file in the request."



Why is UploadFile better than bytes?
You can answer:
"UploadFile is more memory efficient because it does not load the 
entire file into memory at once. In contrast, bytes reads the 
complete file into RAM, which can become inefficient for large files."

'''

from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post('/upload')
def upload(file:UploadFile = File(...)): #file => variable name, UploadFile => Type of object
  return{
    'filename':file.filename #resume.pdf
  }
