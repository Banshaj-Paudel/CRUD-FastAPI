from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()
students = {
    1:{
        "name": "John",
        "age": 20,
        "year": "1A"
    },
    2:{
        "name": "Mary",
        "age": 21,
        "year": "1B"
    }
}

# Class for new student
class Student(BaseModel):
    name : str
    age : int
    year : str

# Class for updating existing student's details
class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None

# Basic api route
@app.get("/")
def index():
    return {"message": "Hello World!!"}

# Api route wih path parameter
@app.get("/students/{student_id}")
def get_student(student_id: int = Path(None, description="ID of the student whose data is to be fetched", gt=0)):
    return students[student_id]

"""
THIS PART CONTAINS SOME ERROR WHICH WILL BE FIXED IN NEAR FUTURE
# Api route with query parameter
@app.get("/students-name")
def student_name(*, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]

    return {"Data":"Not Found, Please enter valid data"}

# Api route with path and query parameter
@app.get("/students-class/{student_id}")
def student_name(*, student_id: int, name: str):
    if students[student_id]["name"] == name:
        return students[student_id]["class"]
    
    else:
        return {"Data":"Not Found, Please enter valid data"}
"""

# Using POST method to enter data
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student:Student):
    if student_id in students:
        return {"Error" : "Student exists"}
    
    students[student_id] = student
    return students[student_id]

# Using PUT method to update the existing data
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error":"Student doesn't exists"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

# Using DELETE method to delete the existing data
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    del students[student_id]
    return {"Message":"Student deleted successfully"}