def individual_serial(teachingMaterial) -> dict:
    return {
        "id": str(teachingMaterial["_id"]),
        "teacher_id": teachingMaterial["teacher_id"],
        "filename": teachingMaterial["filename"],
        "uploadDate": teachingMaterial["uploadDate"]
    }

def list_serial(teachingMaterials) -> list:
    return[individual_serial(teachingMaterial) for teachingMaterial in teachingMaterials]