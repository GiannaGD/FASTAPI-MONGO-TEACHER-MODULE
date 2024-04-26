from fastapi import APIRouter
from models.teachers import Teacher
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# Get Request Method
@router.get("/")
async def get_teachers():
    teachers = list_serial(collection_name.find())
    return teachers

# Post Request Method
@router.post("/")
async def post_teacher(teacher: Teacher):
    collection_name.insert_one(dict(teacher))

# Put Request Method
@router.put("/{id}")
async def put_teacher(id: str, teacher: Teacher):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(teacher)})

# Delete Request Method
@router.delete("/{id}")
async def delete_teacher(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})