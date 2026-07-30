## path parameter
- A path parameter is a value that is part of the URL itself. It lets the client specify which resource they want.

- example
```py
      https://example.com/students/101

Here:

students

is the route, and

101

is the path parameter.

It tells the server:

"I want the student whose ID is 101." 
```

- Example 2
```py
Example 2: Product API
from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "Product ID": product_id,
        "Name": "Laptop"
    }

Visit

/products/101

Output

{
   "Product ID":101,
   "Name":"Laptop"
}
Multiple Path Parameters

You can have more than one.

@app.get("/students/{student_id}/marks/{subject}")
def marks(student_id: int, subject: str):
    return {
        "Student": student_id,
        "Subject": subject
    }

Visit

/students/10/marks/python

FastAPI assigns:

student_id = 10

subject = "python"

Output

{
   "Student":10,
   "Subject":"python"
}
```


## Query Parameters
- A query parameter is a value that comes after the ? in the URL.
```py
Example:

/products?category=laptop

Here,

category=laptop

is the query parameter.

Unlike a path parameter, it is not part of the URL path. It is used to filter, search, sort, or customize the response.
```



