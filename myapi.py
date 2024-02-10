from pyclbr import Class
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


students = {
    1:{
        "name": "Gimhana",
        "age": "27",
        "class":"grade 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str
    
class UpdateStudent(BaseModel):
    name: Optional[str]= None
    age: Optional[int]= None
    year: Optional[str]= None


# GET
@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def getStudent(student_id: int = Path(..., description= "Student id is required to view student", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name/{student_id}")
def getStudent(*, student_id:int, name: Optional[str]=None, test:int):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    return {"Data":"Not found"}    
    
# POST 

@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student already exists"}
    
    students[student_id] = student
    return students[student_id]
    
# PUT 

@app.put("update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    
    # students[student_id] =student
    
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id]

# DELETE
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist."}
    
    
    # deleted_student = students.pop(student_id)
    # return {"Message": "Student deleted successfully", "Data": deleted_student}
    del students[student_id]
    return {"Message": "Student deleted successfully"}
    

