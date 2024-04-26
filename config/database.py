from pymongo import MongoClient

client = MongoClient("mongodb+srv://gd_atlas_user:Gdatlas123@cluster-gd.tdr7li6.mongodb.net/?retryWrites=true&w=majority")

#client = MongoClient("mongodb+srv://Simran:Simran@095@cluster-sk1.sx8umd5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-SK1")

db = client.teacher_db

collection_name = db["teacher_collection"]
teacher_class_manage_collection = db["teacher_class_manage_collection"]
teaching_material_collection = db["teaching_material_collection"]
teaching_material_collection_files = db["teaching_material_collection.files"]
teacher_student_work_collection = db["teacher_student_work_collection"]