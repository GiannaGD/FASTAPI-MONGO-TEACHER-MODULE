from fastapi import APIRouter
from models.assignStudentWork import AssignStudentWork
from config.database import teacher_student_work_collection
from schema.assignStudentWork import list_serial
from bson import ObjectId

assignStudentWorkRouter = APIRouter()

# Get Request Method
@assignStudentWorkRouter.get("/get_teacher_assigned_students")
async def get_teacher_students(teacher_id: str):
    teacherClasses = list_serial(teacher_student_work_collection.find({"teacher_id": teacher_id}))
    return teacherClasses

# Post Request Method
@assignStudentWorkRouter.post("/assign_marks_student")
async def post_teacher_student(assignStudentWork: AssignStudentWork):
    teacher_student_work_collection.insert_one(dict(assignStudentWork))