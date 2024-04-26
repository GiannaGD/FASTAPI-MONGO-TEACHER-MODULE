from fastapi import APIRouter
from models.manageClasses import ManageClasses
from config.database import teacher_class_manage_collection
from schema.manageClasses import list_serial
from bson import ObjectId

manageClassesRouter = APIRouter()

# Post Request Method
@manageClassesRouter.post("/add_student")
async def add_student_in_teacher_class(manageClass: ManageClasses):
    teacher_class_manage_collection.insert_one(dict(manageClass))

# Get Request Method
@manageClassesRouter.get("/get_teacher_class_students")
async def get_teacher_students(teacher_id: str):
    teacherClasses = list_serial(teacher_class_manage_collection.find({"teacher_id": teacher_id}))
    return teacherClasses

# Delete Request Method
@manageClassesRouter.delete("/remove_student_from_class/{id}")
async def remove_class_student(student_class_mapping_id: str):
    teacher_class_manage_collection.find_one_and_delete({"_id": ObjectId(student_class_mapping_id)})