from fastapi import APIRouter
from models.teachingMaterial import TeacherMaterials
from config.database import db, teaching_material_collection, teaching_material_collection_files
from schema.teachingMaterial import list_serial
from bson import ObjectId

import os
import gridfs
import pathlib

manageTeachingMaterialRouter = APIRouter()

from typing import Annotated
from fastapi import FastAPI, File, UploadFile

"""@manageTeachingMaterialRouter.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@manageTeachingMaterialRouter.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return [{"filename": file.filename}]"""

#@manageTeachingMaterialRouter.put("/upload_document_by_teacher/")
#async def create_upload_file(teacherId: str,assignment_file: UploadFile = File(...)):
@manageTeachingMaterialRouter.put("/upload_document_by_teacher/{teacherId, assignment_file}")
async def create_upload_file(teacherId: str, assignment_file: UploadFile = File(...)):
    #teacherId = "662787e05cd0fa6e2830618d"
    content_assignment = await assignment_file.read()
    # put file into mongodb
    fs = gridfs.GridFS(db, collection="teaching_material_collection")
    fs.put(content_assignment, filename=assignment_file.filename, teacher_id = teacherId)
    return {"filename": assignment_file.filename+" uploaded successfully"}
    #return teacherId
# Get Request Method
@manageTeachingMaterialRouter.get("/get_all_teacher_documents")
async def get_all_files(teacher_id: str):
    #return teaching_material_collection_files.find()
    allTeacherMaterials = list_serial(teaching_material_collection_files.find({"teacher_id": teacher_id}))
    #allTeacherMaterials = teaching_material_collection_files.find({"teacher_id": id})
    return allTeacherMaterials

@manageTeachingMaterialRouter.put("/download_teacher_document/{document_id}")
async def create_download_file(document_id: str):    
    data = teaching_material_collection_files.find_one({"_id": ObjectId(document_id)})    
    fs = gridfs.GridFS(db, collection="teaching_material_collection")
    out_data = fs.get(ObjectId(document_id)).read()
    download_filename = data.get('filename')    
    download_loc = os.path.join(os.path.expanduser("~") + "/downloads/", download_filename)
    #download_loc = pathlib.Path.home() / "downloads" / download_filename
    #download_loc = os.path.join(os.getcwd() + "/downloads/", download_filename)
    #download_loc = home_path
    #download_loc = os.path.expandvars(R"C:\Users\$USERNAME")
    #download_loc2 = os.path.expandvars(R"${TEMP}")
    #download_loc3 = os.path.expandvars(R"${MYHOME}")
    #download_loc4 = os.path.expandvars(R"% HOMEPATH %")
    #download_loc1 = os.path.expanduser("~") + ""
    #print(os.path.expandvars(path3) + "========================================")
    #print(pathlib.Path.home() / "Downloads---------------------------------------------------------")
    #return download_loc
    #with open("downloaded_files", 'wb') as output:
    #    output.write(out_data)
    #return {"status": download_filename+" :Download Completed!"}
    with open(download_loc, 'wb') as output:
        output.write(out_data)
    return {"status": download_loc+" :Download Completed!"}